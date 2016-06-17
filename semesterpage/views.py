from django.shortcuts import render
from .models import StudyProgram, Semester, Course


def semester(request, program_code, semester_number):
    study_program = StudyProgram.objects.get(program_code__iexact=program_code)
    all_semesters = semester = study_program.semesters.all()
    semester = all_semesters.get(number=semester_number)
    courses = semester.courses.all()

    return render(request, 'semesterpage/courses.html',
                  {'semester_number': semester.number,
                   'courses': courses,
                   'semesters': all_semesters})
