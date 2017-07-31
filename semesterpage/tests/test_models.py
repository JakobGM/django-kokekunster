from django.contrib.auth.models import Group, User
from django.test import TestCase

import pytest

from dataporten.models import DataportenUser
from ..apps import create_contributor_groups
from .factories import SemesterFactory


class TestUser(TestCase):
    def setUp(self):
        create_contributor_groups()

    def test_new_user_permissions(self):
        new_user = User.objects.create(username='provided_username')

        # Assert that the post_save signal listener has added the user.is_staff
        # permission, such that all user can have access to the admin back-end
        self.assertIs(new_user.is_staff, True)

        # All new users are added to the students group
        students_group = Group.objects.get(name='students')
        self.assertIn(students_group, new_user.groups.all())

        # Assert that the contributor and options objects have been attached
        new_user.contributor
        new_user.options


class TestStudyProgram:
    @pytest.mark.django_db
    def test_study_program_factory(self, study_program):
        assert study_program.display_name == 'Fysmat'


class TestMainProfile:
    @pytest.mark.django_db
    def test_main_profile_factory(self, main_profile):
        assert main_profile.display_name == 'InMat'


class TestSemester:
    @pytest.mark.django_db
    def test_creation_of_semester_with_factory(self, semester):
        assert semester.number == 1
        assert semester.main_profile.display_name == 'InMat'


class TestCourse:
    @pytest.mark.django_db
    def test_creation_of_course_with_many_to_many_field(self, course):
        assert course.display_name == 'C++'
        assert course.semesters.all()[0].number == 1


class TestResourceLinkList:
    @pytest.mark.django_db
    def test_resource_link_list_factory_with_many_to_many_field(self, resource_link_list):
        assert resource_link_list.full_name == 'Ressurser'
        assert resource_link_list.study_programs.all()[0].display_name == 'Fysmat'


class TestCourseLink:
    @pytest.mark.django_db
    def test_basic_properties_of_course_link(self, course_link):
        assert course_link.url == 'http://ntnu.no/emne/TDT4102/'


class TestResourceLink:
    @pytest.mark.django_db
    def test_resource_link_factory(self, resource_link):
        assert resource_link.url == 'http://wolframalpha.com/'


class TestContributor:
    @pytest.mark.django_db
    def test_contributor_factory(self, contributor):
        assert type(contributor.user) is DataportenUser
        assert contributor.access_level == 1


class TestOptions:
    @pytest.mark.django_db
    def test_options_factory(self, options):
        assert type(options.user) is DataportenUser
