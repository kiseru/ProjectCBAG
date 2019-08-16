from django.core.exceptions import ValidationError
from django.db import models
from django.contrib.auth.models import User


def validate_telephone_number(telephone_number):
    if telephone_number[0] != '+':
        return ValidationError(
            '%(telephone_number) is not a telephone number',
            params={'telephone_number': telephone_number},
        )


class Exam(models.Model):
    """
    List of exam
    """
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name


class AcademicGroup(models.Model):
    institute = models.CharField(max_length=200)
    course = models.PositiveSmallIntegerField(default=1)
    name = models.CharField(max_length=6)
    starosta = models.OneToOneField(User, on_delete=models.CASCADE)
    starosta_phone_number = models.CharField(max_length=12, validators=[validate_telephone_number])
    exams = models.ManyToManyField(Exam, blank=True)
    curator = models.CharField(max_length=50)

    def __str__(self):
        return self.name


class Student(models.Model):
    name = models.CharField(max_length=50)
    educational_form = models.CharField(max_length=1, choices=[
        ('b', 'Бюджет'),
        ('k', 'Контракт'),
    ])
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

    prize_winning_place = models.CharField(max_length=1, choices=[
        ('0', 'участие'),
        ('1', '1 место'),
        ('2', '2 место'),
        ('3', '3 место'),
    ])
    student_event = models.ManyToManyField(Student, blank=True)
    event_name = models.CharField(max_length=200)
    event_area = models.CharField(max_length=1, choices=[
        ('n', 'Научная'),
        ('k', 'Культурно-массовая'),
        ('s', 'Спортивная'),
        ('o', 'Общественная')
    ])
    event_level = models.CharField(max_length=1, choices=[
        ('m', 'Международный'),
        ('v', 'Всероссийский'),
        ('r', 'Региональный'),
        ('g', 'Городской'),
        ('u', 'Университетский'),
    ])

    academic_group = models.ForeignKey(AcademicGroup, on_delete=models.CASCADE)

    def __str__(self):
        return self.name
