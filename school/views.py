from django.views.generic import ListView
from django.shortcuts import render

from .models import Student


def students_list(request):
    template = 'school/students_list.html'
    students = Student.objects.all()
    stud_dict = {}
    for student in students:
        stud_dict[student] = {
            'name': student.name,
            'group': student.group,
            'teacher': student.teacher
        }
    context = {'object_list': stud_dict}
    ordering = 'group'

    return render(request, template, context)