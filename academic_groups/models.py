import djchoices
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
from django.db import models
from django.db.models import Avg


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

    class Meta:
        verbose_name = 'Экзамен'
        verbose_name_plural = 'Экзамены'

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

    class Meta:
        verbose_name = 'Академическая группа'
        verbose_name_plural = 'Академические группы'

    def __str__(self):
        return self.name


class EducationalFormChoices(djchoices.DjangoChoices):
    budget = djchoices.ChoiceItem(0, 'Бюджет')
    contract = djchoices.ChoiceItem(1, 'Контракт')


class Student(models.Model):
    name = models.CharField(max_length=50)
    educational_form = models.PositiveSmallIntegerField(choices=EducationalFormChoices.choices)
    academic_group = models.ForeignKey(AcademicGroup, on_delete=models.CASCADE)
    student_exam = models.ManyToManyField(Exam, through='ExamResult', through_fields=('student', 'exam'))

    class Meta:
        verbose_name = 'Студент'
        verbose_name_plural = 'Студенты'

    @property
    def average_score(self):
        return self.student_exam.aggregate(average_score=Avg('examresult__score'))['average_score']

    def __str__(self):
        return self.name


class ExamResult(models.Model):
    score = models.PositiveSmallIntegerField(default=0)
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    exam = models.ForeignKey(Exam, on_delete=models.CASCADE)

    class Meta:
        verbose_name = 'Результат экзамена'
        verbose_name_plural = 'Результаты экзаменов'

    def __str__(self):
        return str(self.score)


class WinningPlaceChoices(djchoices.DjangoChoices):
    first = djchoices.ChoiceItem(1, '1 место')
    second = djchoices.ChoiceItem(2, '2 место')
    third = djchoices.ChoiceItem(3, '3 место')
    participation = djchoices.ChoiceItem(0, 'участие')


class EventAreaChoices(djchoices.DjangoChoices):
    scientific = djchoices.ChoiceItem(0, 'Научная')
    cultural = djchoices.ChoiceItem(1, 'Культурная')
    sports = djchoices.ChoiceItem(2, 'Спортивная')
    social = djchoices.ChoiceItem(4, 'Общественная')


class EventLevelChoices(djchoices.DjangoChoices):
    international = djchoices.ChoiceItem(0, 'Международный')
    all_russian = djchoices.ChoiceItem(1, 'Всероссийский')
    regional = djchoices.ChoiceItem(2, 'Региональный')
    urban = djchoices.ChoiceItem(3, 'Городской')
    university = djchoices.ChoiceItem(4, 'Университетский')


class EventGroup(models.Model):
    name = models.CharField(max_length=30)
    prize_winning_place = models.PositiveSmallIntegerField(choices=WinningPlaceChoices.choices)
    student_event = models.ManyToManyField(Student, blank=True)
    event_name = models.CharField(max_length=200)
    event_area = models.PositiveSmallIntegerField(choices=EventAreaChoices)
    event_level = models.PositiveSmallIntegerField(choices=EventLevelChoices)
    academic_group = models.ForeignKey(AcademicGroup, on_delete=models.CASCADE)

    class Meta:
        verbose_name = 'Группа события'
        verbose_name_plural = 'Группы событий'

    def __str__(self):
        return self.name
