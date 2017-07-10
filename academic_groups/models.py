from django.db import models


class AcademicGroup(models.Model):
    institute = models.CharField(max_length=200)
    course = models.PositiveSmallIntegerField()
    academic_group = models.CharField(max_length=6)
    starosta = models.CharField(max_length=50)
    curator = models.CharField(max_length=50)
    student_count = models.IntegerField()


class Student(models.Model):
    application = models.ForeignKey(Application, on_delete=models.CASCADE)
    name = models.CharField(max_length=50)
    educational_form = models.CharField([
        'бюджет',
        'контракт',
    ])
    average_score = models.FloatField()


class Exam(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    exam_name = models.CharField(max_length=50)
    score = models.IntegerField(default=0)
