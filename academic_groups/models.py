from django.db import models
from django.contrib.auth.models import User


class Exam(models.Model):
    """
    List of exam
    """
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name


class PrizeWinningPlace(models.Model):
    """
    Level of Prize - 1st, 2nd, 3rd, grand-pris
    """
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
    course = models.PositiveSmallIntegerField(default=1)
    name = models.CharField(max_length=6)
    starosta = models.OneToOneField(User)

    #validator
    starosta_phone_number = models.CharField(max_length=12)
    exams = models.ManyToManyField(Exam)
    curator = models.CharField(max_length=50)

    def __str__(self):
        return self.name


class Student(models.Model):
    name = models.CharField(max_length=50)
    educational_form = models.CharField(max_length=8)
    academic_group = models.ForeignKey(AcademicGroup, on_delete=models.CASCADE)
    student_exam = models.ManyToManyField(Exam, through='ExamResult', through_fields=('student', 'exam'))
    average_score = models.PositiveSmallIntegerField(default=0)

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
