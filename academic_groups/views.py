from django.contrib.auth.decorators import login_required
from django.http import HttpResponseForbidden, Http404
from django.shortcuts import render, redirect

from . import models


# Create your views here.
@login_required(login_url='/auth/log_in')
def students(request):
    user = request.user
    user_group = user.groups.get().name

    academic_group = user.academicgroup

    context = {
        'academic_group': academic_group,
        'name': '{0} {1}'.format(user.first_name, user.last_name),
    }

    if user_group == 'Starostas':
        return render(request, 'academic_groups/students.html', context=context)
    else:
        return HttpResponseForbidden()


@login_required(login_url='/auth/log_in')
def add_student(request):
    user = request.user
    academic_group = user.academicgroup

    if not user.groups.get().name == 'Starostas':
        return HttpResponseForbidden()

    if request.method == 'GET':

        context = {
            'academic_group': academic_group,
            'educational_forms': models.EducationalForm.objects.all(),
            'name': '{0} {1}'.format(user.first_name, user.last_name),
        }

        return render(request, 'academic_groups/add_student.html', context=context)
    elif request.method == 'POST':
        student = models.Student()

        student.name = '{0} {1} {2}'.format(
            request.POST['last_name'],
            request.POST['first_name'],
            request.POST['father_first_name'],
        )

        student.academic_group = academic_group

        student.educational_form = models.EducationalForm.objects.get(pk=request.POST["educational_form"])

        student.save()

        exams = academic_group.exams.all()

        for exam in exams:
            exam_score = models.ExamResult()
            exam_score.student = student
            exam_score.exam = exam
            exam_score.score = int(request.POST['{0}'.format(exam.id)])
            exam_score.save()

        return redirect('/academic_groups/students')
    else:
        return Http404()


@login_required(login_url='/auth/log_in')
def student(request, student_id):

    if not request.user.groups.get().name == 'Starostas':
        return HttpResponseForbidden()

    if request.method == 'GET':

        context = {
            'student': models.Student.objects.get(pk=student_id),
            'name': '{0} {1}'.format(request.user.first_name, request.user.last_name),
        }

        return render(request, 'academic_groups/student.html', context)
    elif request.method == 'POST':
        pass
    else:
        return Http404()
