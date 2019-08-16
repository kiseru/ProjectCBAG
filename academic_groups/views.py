from django.http import Http404
from django.shortcuts import render, redirect
from django.urls import reverse

from academic_groups.models import Exam, ExamResult, Student, AcademicGroup, EventGroup


# Create your views here.
def students(request):
    user = request.user
    academic_group = user.academicgroup

    context = {
        'academic_group': academic_group,
        'exams': Exam.objects.all(),
        'name': '{0} {1}'.format(user.first_name, user.last_name),
    }

    return render(request, 'academic_groups/students.html', context=context)


def add_student(request):
    user = request.user
    academic_group = user.academicgroup

    if request.method == 'GET':

        context = {
            'academic_group': academic_group,
            'name': '{0} {1}'.format(user.first_name, user.last_name),
        }

        return render(request, 'academic_groups/add_student.html', context=context)
    elif request.POST:
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


def student_show(request, student_id):
    student = Student.objects.get(pk=student_id)

    context = {
        'student': student,
        'student_exams': student.examresult_set.filter(student=student),
        'name': '{0} {1}'.format(request.user.first_name, request.user.last_name),
    }

    return render(request, 'academic_groups/student.html', context)


def edit_student_exams(request, student_id):
    if request.POST:
        student = Student.objects.get(pk=student_id)

        student_exams = list(filter(lambda exam_result: exam_result.student == student, student.examresult_set.all()))

        for student_exam in student_exams:
            student_exam.score = request.POST['exam{0}'.format(student_exam.exam_id)]
            student_exam.save()

        return redirect(reverse("groups:student", args={
            student_id: student.id,
        }))
    else:
        return Http404()


def delete_student(request, student_id):
    if request.POST:
        student = Student.objects.get(pk=student_id)
        student.delete()
        return redirect(reverse('groups:students'))

    return Http404()


def add_exam(request):
    if request.POST:
        exam = Exam.objects.get(pk=request.POST['exam_id'])

        request.user.academicgroup.exams.add(exam)

        for student in request.user.academicgroup.student_set.all():
            exam_result = ExamResult()
            exam_result.exam = exam
            exam_result.student = student
            exam_result.score = 0
            exam_result.save()

        return redirect(reverse('home'))


def delete_exam(request):
    if request.POST:
        academic_group = request.user.academicgroup
        academic_group.exams.remove(request.POST['exam_id'])
        academic_group.save()

        for student in academic_group.student_set.all():
            student_exam = ExamResult.objects.filter(student_id=student.id, exam_id=request.POST['exam_id'])
            student_exam.delete()

        return redirect(reverse('groups:students'))

    return Http404()


def events(request):
    context = {
        'academic_group': request.user.academicgroup,
        'name': '{0} {1}'.format(request.user.first_name, request.user.last_name),
    }

    return render(request, 'academic_groups/events.html', context)


def add_event(request):
    if request.POST:
        event_group = EventGroup()
        event_group.name = request.POST['group_name']
        event_group.event_name = request.POST['event_name']
        event_group.event_area = request.POST['event_area']
        event_group.event_level = request.POST['event_level']
        event_group.prize_winning_place = request.POST['place']
        event_group.academic_group = request.user.academicgroup
        event_group.save()
        return redirect(reverse('groups:events'))


def event_add_student(request):
    if request.POST:
        event_group = EventGroup.objects.get(pk=request.POST['event_group_id'])
        student = Student.objects.get(pk=request.POST['student'])
        event_group.student_event.add(student)
        event_group.save()

        return redirect(reverse('groups:events'))


def edit_event_group(request):
    if request.POST:
        event_group = EventGroup.objects.get(pk=request.POST['event_id'])
        event_group.name = request.POST['group_name']
        event_group.event_name = request.POST['event_name']
        event_group.event_level = request.POST['event_level']
        event_group.prize_winning_place = request.POST['place']
        event_group.save()

        return redirect(reverse('groups:events'))


def delete_event_group(request):
    if request.POST:
        event_group = EventGroup.objects.get(pk=request.POST['event_group_id'])
        event_group.delete()

        return redirect(reverse('groups:events'))


def jury(request):
    context = {
        'academic_groups': AcademicGroup.objects.all(),
        'name': '{0} {1}'.format(request.user.first_name, request.user.last_name),
    }

    return render(request, 'academic_groups/jury.html', context)
