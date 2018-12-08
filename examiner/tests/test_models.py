from pathlib import Path

from django.db.utils import IntegrityError

import pytest

import responses

from examiner.models import ExamURL, FileBackup
from examiner.parsers import Language, Season
from dataporten.tests.factories import UserFactory
from semesterpage.tests.factories import CourseFactory


@pytest.mark.django_db
def test_derive_course_code_on_save():
    """The course code should be derived from the course foreign key."""
    url = 'http://www.example.com/TMA4130/2013h/oldExams/eksamen-bok_2006v.pdf'
    course = CourseFactory(course_code='TMA4130')
    exam_url = ExamURL(url=url, course=course)
    assert exam_url.course_code is None
    exam_url.save()
    assert exam_url.course_code == 'TMA4130'


@pytest.mark.django_db
def test_prevention_of_unique_url():
    """URLs should be unique."""
    url = 'http://www.example.com/TMA4130/2013h/oldExams/eksamen-bok_2006v.pdf'
    course = CourseFactory(course_code='TMA4130')
    exam_url1 = ExamURL(url=url, course=course)
    exam_url1.save()

    exam_url2 = ExamURL(url=url, course=course, year=2006)
    with pytest.raises(IntegrityError):
        exam_url2.save()


@pytest.mark.django_db
def test_parse_url():
    """The parse_url method should update model fields from url parsing."""
    url = 'http://www.example.com/TMA4130/2013h/oldExams/eksamen-bok_2006v.pdf'
    exam_url = ExamURL(url=url)
    exam_url.parse_url()
    exam_url.save()
    assert exam_url.url == url

    # At first, the course does not exist, so only the string is saved
    assert exam_url.course is None
    assert exam_url.course_code == 'TMA4130'

    # All other fields have been inferred
    assert exam_url.filename == 'eksamen-bok_2006v.pdf'
    assert exam_url.language == Language.BOKMAL
    assert exam_url.year == 2006
    assert exam_url.season == Season.SPRING
    assert exam_url.solutions is False
    assert exam_url.probably_exam is True
    assert exam_url.verified_by.count() == 0
    assert exam_url.created_at
    assert exam_url.updated_at

    # Now we create the course and reparse
    course = CourseFactory(course_code='TMA4130')
    course.save()
    exam_url.parse_url()

    # The course should now be properly set
    assert exam_url.course == course


@pytest.mark.django_db
def test_parse_url_of_already_verified_url():
    """Parsing a verified url should not mutate the object."""
    url = 'http://www.example.com/TMA4130/2013h/oldExams/eksamen-bok_2006v.pdf'
    exam_url = ExamURL(url=url)

    # First, the parser infers 2006 as the year
    exam_url.parse_url()
    exam_url.save()
    assert exam_url.year == 2006

    # Then the exam year is modified by a user
    exam_url.year = 2016

    # And thereafter verified by that user
    user = UserFactory(username='verifier')
    user.save()
    exam_url.verified_by.add(user)

    # On reparsing the url, attributes are not changed
    exam_url.parse_url()
    assert exam_url.year == 2016


@responses.activate
@pytest.mark.django_db
def test_file_backup(tmpdir, settings):
    # Create a trivial exam file
    tmpdir = Path(tmpdir)
    test_file = tmpdir / 'tmp_exam.txt'
    test_file.touch()
    test_file.write_text('Exam text')

    # This file is "hosted" at this URL
    url = 'http://www.example.com/TMA4130/2013h/oldExams/eksamen.txt'

    # Mock the file download from this URL
    responses.add(
        responses.GET,
        url,
        body=test_file.read_bytes(),
        status=200,
        content_type='text/plain',
        stream=True,
    )

    # We now backup this file
    exam_url = ExamURL(url=url)
    exam_url.backup_file()
    exam_url.refresh_from_db()

    # The downloaded file should be hashed and the result stored
    assert exam_url.dead_link is False
    expected_md5_hash = 'adc7a2fa473be1b091f7324aa4067c8a'
    file_backup = exam_url.file_backup
    assert file_backup.md5_hash == expected_md5_hash

    # And the stored file should be named according to its hash
    assert file_backup.file.name == 'examiner/FileBackup/' + expected_md5_hash

    # The directory for file backups should now contain one file
    backup_directory = Path(settings.MEDIA_ROOT / 'examiner/FileBackup/')
    assert len(list(backup_directory.iterdir())) == 1

    # Now we take a look at a new url
    new_url = 'http://example.com/ny_eksamen.txt'

    # But this url returns the same file as previous
    responses.add(
        responses.GET,
        new_url,
        body=test_file.read_bytes(),
        status=200,
        content_type='text/plain',
        stream=True,
    )
    new_exam_url = ExamURL(url=new_url)
    new_exam_url.backup_file()
    assert len(list(backup_directory.iterdir())) == 1
    assert ExamURL.objects.all().count() == 2
    assert FileBackup.objects.all().count() == 1
    assert exam_url.file_backup == new_exam_url.file_backup


@responses.activate
@pytest.mark.django_db
def test_file_backup_of_dead_link(tmpdir, settings):
    """A dead URL should be handled properly."""
    # This file was "hosted" at this URL
    url = 'http://www.example.com/TMA4130/2013h/oldExams/eksamen.txt'

    # But the URL now returns 404
    responses.add(
        responses.GET,
        url,
        body=b"404",
        status=404,
        content_type='text/plain',
        stream=True,
    )

    # We scrape this URL
    exam_url = ExamURL(url=url)
    exam_url.parse_url()
    assert exam_url.dead_link is None

    # And then unsucessfully try to backup the file
    exam_url.backup_file()
    exam_url.refresh_from_db()
    assert exam_url.dead_link is True