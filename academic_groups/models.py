from django.db import models


class AcademicGroup(models.Model):
    institute = models.CharField(max_length=200)
    course = models.PositiveSmallIntegerField()
    academic_group_name = models.CharField(max_length=6)
    starosta = models.CharField(max_length=50)
    starosta_email = models.CharField(max_length=50)
    starosta_phone_number = models.CharField(max_length=12)
    curator = models.CharField(max_length=50)
    student_count = models.IntegerField()

    def __str__(self):
        return self.academic_group_name


class Student(models.Model):
    academic_group = models.ForeignKey(AcademicGroup, on_delete=models.CASCADE)
    student_name = models.CharField(max_length=50)
    educational_form = models.CharField(max_length=8, choices=[
        ('b', 'бюджет'),
        ('k', 'контракт'),
    ])

    def __str__(self):
        return self.student_name


class Exam(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    exam_name = models.CharField(max_length=50)
    score = models.IntegerField(default=0)

    def __str__(self):
        return self.exam_name


class Event(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    event_name = models.CharField(max_length=200)
    event_area = models.CharField(max_length=200, choices=[
        ('kmd', 'Культурно-массовая деятельность'),
        ('sd', 'Спортивная деятельность'),
        ('nd', 'Научная деятельность'),
        ('od', 'Общественная деятельность'),
    ])

    def __str__(self):
        return self.event_name
