from django.contrib.auth.decorators import login_required
from django.http import HttpResponseForbidden, Http404
from django.shortcuts import render

from . import models


# Create your views here.
@login_required(login_url='/auth/log_in')
def students(request):
    user = request.user
    user_group = user.groups.get().name

    academic_group = user.academicgroup

    context = {
        'academic_group': academic_group,
    }

    if user_group == 'Starostas':
        return render(request, 'academic_groups/students.html', context=context)
    else:
        return HttpResponseForbidden()


@login_required(login_url='/auth/log_in')
def add_student(request):
    user = request.user

    if not user.groups.get().name == 'Starostas':
        return HttpResponseForbidden()

    if request.method == 'GET':

        academic_group = user.academicgroup

        context = {
            'academic_group': academic_group,
        }

        return render(request, 'academic_groups/add_student.html', context=context)
    elif request.method == 'POST':
        pass
    else:
        return Http404()
