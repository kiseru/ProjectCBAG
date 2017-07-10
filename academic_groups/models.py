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


class Exam(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    exam_name = models.CharField(max_length=50)
    score = models.IntegerField(default=0)


class Event(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    event_name = models.CharField(max_length=200)
    event_area = models.CharField(max_length=200, choices=[
        ('kmd', 'Культурно-массовая деятельность'),
        ('sd', 'Спортивная деятельность'),
        ('nd', 'Научная деятельность'),
        ('od', 'Общественная деятельность'),
    ])
