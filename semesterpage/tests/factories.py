from django.contrib.auth.models import User

import factory
from dataporten.tests.factories import DataportenUserFactory

from ..models import (
        Contributor,
        Course,
        CourseLink,
        CourseUpload,
        CustomLinkCategory,
        Link,
        LinkList,
        MainProfile,
        Options,
        ResourceLink,
        ResourceLinkList,
        Semester,
        StudyProgram,
)


class StudyProgramFactory(factory.django.DjangoModelFactory):
    full_name = 'Fysikk og Mattematikk'
    display_name = 'Fysmat'
    has_archive = True
    published = True

    class Meta:
        model = StudyProgram


class MainProfileFactory(factory.django.DjangoModelFactory):
    full_name = 'Industriell matematikk'
    display_name = 'InMat'
    study_program = factory.SubFactory(StudyProgramFactory)

    class Meta:
        model = MainProfile


class SemesterFactory(factory.django.DjangoModelFactory):
    number = 1
    study_program = factory.SubFactory(StudyProgramFactory)
    main_profile = factory.SubFactory(MainProfileFactory)
    published = True

    class Meta:
        model = Semester


class CourseFactory(factory.django.DjangoModelFactory):
    full_name = 'Prosedyre- og Objektorientert Programmering'
    display_name = 'C++'
    course_code = factory.Sequence(lambda n: f'TDT{4101 + n}')

    class Meta:
        model = Course

    @factory.post_generation
    def semesters(self, create, extracted, **kwargs):
        if not create:
            # Simple build, do nothing
            return

        if extracted:
            # A list of parents were passed in, use them
            # in the many-to-many relationship
            for semester in extracted:
                self.semesters.add(semester)


class CourseUploadFactory(factory.django.DjangoModelFactory):
    course = factory.SubFactory(CourseFactory)
    file = factory.django.FileField(filename='user_upload.pdf')
    author = factory.SubFactory(DataportenUserFactory)
    display_name = ''

    class Meta:
        model = CourseUpload


class ResourceLinkListFactory(factory.django.DjangoModelFactory):
    full_name = 'Ressurser'
    display_name = 'Ressurser'
    default = True

    class Meta:
        model = ResourceLinkList

    @factory.post_generation
    def study_programs(self, create, extracted, **kwargs):
        if not create:
            # Simple build, do nothing
            return

        if extracted:
            # A list of parents were passed in, use them
            # in the many-to-many relationship
            for study_program in extracted:
                self.study_programs.add(study_program)


class CourseLinkFactory(factory.django.DjangoModelFactory):
    url = 'http://ntnu.no/emne/TDT4102/'
    category = 'Informasjon'
    title = 'Course homepage'
    course = factory.SubFactory(CourseFactory)

    class Meta:
        model = CourseLink


class ResourceLinkFactory(factory.django.DjangoModelFactory):
    url = 'http://wolframalpha.com/'
    category = 'Informasjon'
    title = 'Wolfram Alpha'
    resource_link_list = factory.SubFactory(ResourceLinkListFactory)

    class Meta:
        model = ResourceLink


class ContributorFactory(factory.django.DjangoModelFactory):
    user = factory.SubFactory(DataportenUserFactory, contributor=None)
    access_level = 1

    class Meta:
        model = Contributor


class OptionsFactory(factory.django.DjangoModelFactory):
    user = factory.SubFactory(DataportenUserFactory, options=None)

    class Meta:
        model = Options
