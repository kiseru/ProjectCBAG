from django.http import HttpResponseForbidden, Http404
from django.shortcuts import render, redirect
from django.urls import reverse

from academic_groups.models import Exam, ExamResult, Student

from pages.decorators import should_be_starosta


# Create your views here.
@should_be_starosta
def students(request):
    user = request.user
    user_group = user.groups.get().name

    academic_group = user.academicgroup

    context = {
        'academic_group': academic_group,
        'exams': Exam.objects.all(),
        'name': '{0} {1}'.format(user.first_name, user.last_name),
    }

    if user_group == 'Starostas':
        return render(request, 'academic_groups/students.html', context=context)
    else:
        return HttpResponseForbidden()


@should_be_starosta
def add_student(request):
    user = request.user
    academic_group = user.academicgroup

    if not user.groups.get().name == 'Starostas':
        return HttpResponseForbidden()

    if request.method == 'GET':

        context = {
            'academic_group': academic_group,
            'name': '{0} {1}'.format(user.first_name, user.last_name),
        }

        return render(request, 'academic_groups/add_student.html', context=context)
    elif request.method == 'POST':
        student = Student()

        student.name = '{0} {1} {2}'.format(
            request.POST['last_name'],
            request.POST['first_name'],
            request.POST['father_first_name'],
        )

        student.academic_group = academic_group

        student.educational_form = request.POST['educational_form']

        student.save()

        exams = academic_group.exams.all()

        for exam in exams:
            exam_score = ExamResult()
            exam_score.student = student
            exam_score.exam = exam
            exam_score.score = int(request.POST['{0}'.format(exam.id)])
            exam_score.save()

        return redirect(reverse("groups:students"))
    else:
        return Http404()


@should_be_starosta
def add_exam(request):
    if not request.user.groups.get().name == 'Starostas':
        return HttpResponseForbidden()

    if request.method == 'POST':
        exam = Exam.objects.get(pk=request.POST['exam_id'])

        request.user.academicgroup.exams.add(exam)

        for student in request.user.academicgroup.student_set.all():
            exam_result = ExamResult()
            exam_result.exam = exam
            exam_result.student = student
            exam_result.score = 0
            exam_result.save()

        return redirect(reverse('home'))
