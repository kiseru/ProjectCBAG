from django.db import models
from django.contrib.auth.models import User


class Curator(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name


class EducationalForm(models.Model):
    name = models.CharField(max_length=8)

    def __str__(self):
        return self.name


class Exam(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name


class PrizeWinningPlace(models.Model):
    place = models.CharField(max_length=7)

    def __str__(self):
        return self.place


class EventArea(models.Model):
    name = models.CharField(max_length=31)

    def __str__(self):
        return self.name


class EventLevel(models.Model):
    name = models.CharField(max_length=23)

    def __str__(self):
        return self.name


class AcademicGroup(models.Model):
    institute = models.CharField(max_length=200)
    course = models.PositiveSmallIntegerField()
    name = models.CharField(max_length=6)
    starosta = models.OneToOneField(User)
    starosta_phone_number = models.CharField(max_length=12)
    exams = models.ManyToManyField(Exam)
    curator = models.ForeignKey(Curator, on_delete=models.CASCADE)
    student_count = models.IntegerField()

    def __str__(self):
        return self.name


class Student(models.Model):
    name = models.CharField(max_length=50)
    educational_form = models.ForeignKey(EducationalForm, on_delete=models.CASCADE)
    academic_group = models.ForeignKey(AcademicGroup, on_delete=models.CASCADE)
    student_exam = models.ManyToManyField(Exam, through='ExamResult', through_fields=('student', 'exam'))

    def __str__(self):
        return self.name


class ExamResult(models.Model):
    score = models.PositiveSmallIntegerField(default=0)
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    exam = models.ForeignKey(Exam, on_delete=models.CASCADE)

    def __str__(self):
        return self.score


class EventGroup(models.Model):
    name = models.CharField(max_length=30)
    prize_winning_place = models.ForeignKey(PrizeWinningPlace, on_delete=models.CASCADE)
    student_event = models.ManyToManyField(Student)

    def __str__(self):
        return self.name


class Event(models.Model):
    name = models.CharField(max_length=200)
    event_group = models.ForeignKey(EventGroup)
    event_area = models.ForeignKey(EventArea, on_delete=models.CASCADE)
    event_level = models.ForeignKey(EventLevel, on_delete=models.CASCADE)

    def __str__(self):
        return self.name
