from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.http import Http404
from django.shortcuts import render, redirect
from django.urls import reverse, reverse_lazy
from django.views import generic

from academic_groups.models import Exam, ExamResult, Student, AcademicGroup, EventGroup


class AcademicGroupDetailView(LoginRequiredMixin,
                              UserPassesTestMixin,
                              generic.DetailView):
    model = AcademicGroup

    def test_func(self):
        return self.request.user.groups.get().name == 'headman'


class StudentDetailView(LoginRequiredMixin,
                        generic.DetailView):
    model = Student


class StudentCreateView(LoginRequiredMixin,
                        generic.CreateView):
    model = Student
    fields = ('name', 'academic_group', 'educational_form', 'student_exam')
    success_url = reverse_lazy('home')


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
