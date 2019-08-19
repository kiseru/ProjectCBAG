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
    name = models.CharField(max_length=50, verbose_name='Название')

    class Meta:
        verbose_name = 'Экзамен'
        verbose_name_plural = 'Экзамены'

    def __str__(self):
        return self.name


class AcademicGroup(models.Model):
    institute = models.CharField(max_length=200, verbose_name='Институт')
    course = models.PositiveSmallIntegerField(default=1, verbose_name='Курс')
    name = models.CharField(max_length=6, verbose_name='Название')
    starosta = models.OneToOneField(User, on_delete=models.CASCADE, verbose_name='Староста')
    starosta_phone_number = models.CharField(max_length=12, validators=[validate_telephone_number],
                                             verbose_name='Номер старосты')
    # exams = models.ManyToManyField(Exam, blank=True, verbose_name='Экзамены')
    curator = models.CharField(max_length=50, verbose_name='Куратор')

    class Meta:
        verbose_name = 'Академическая группа'
        verbose_name_plural = 'Академические группы'

    def __str__(self):
        return self.name


class AcademicGroupExam(models.Model):
    academic_group = models.ForeignKey(AcademicGroup, on_delete=models.CASCADE, verbose_name='Академическая группа')
    exam = models.ForeignKey(Exam, on_delete=models.CASCADE, verbose_name='Экзамен')

    class Meta:
        verbose_name = 'Экзамен академической группы'
        verbose_name_plural = 'Экзамены академичских групп'
        unique_together = ('academic_group', 'exam')

    def __str__(self):
        return f'{self.academic_group.name} - {self.exam.name}'


class EducationalFormChoices(djchoices.DjangoChoices):
    budget = djchoices.ChoiceItem(0, 'Бюджет')
    contract = djchoices.ChoiceItem(1, 'Контракт')


class Student(models.Model):
    name = models.CharField(max_length=50, verbose_name='ФИО')
    educational_form = models.PositiveSmallIntegerField(choices=EducationalFormChoices.choices,
                                                        verbose_name='Форма обучения')
    academic_group = models.ForeignKey(AcademicGroup, on_delete=models.CASCADE, verbose_name='Академическая группа')
    student_exam = models.ManyToManyField(Exam, through='ExamResult', through_fields=('student', 'exam'))

    class Meta:
        verbose_name = 'Студент'
        verbose_name_plural = 'Студенты'

    @property
    def average_score(self):
        average_score = self.student_exam.aggregate(average_score=Avg('examresult__score'))['average_score']
        if average_score is not None:
            return average_score
        else:
            return 0.0

    def __str__(self):
        return self.name


class ExamResult(models.Model):
    score = models.PositiveSmallIntegerField(default=0, verbose_name='Баллы')
    student = models.ForeignKey(Student, on_delete=models.CASCADE, verbose_name='Студент')
    exam = models.ForeignKey(Exam, on_delete=models.CASCADE, verbose_name='Экзамен')

    class Meta:
        verbose_name = 'Результат экзамена'
        verbose_name_plural = 'Результаты экзаменов'

    def __str__(self):
        return str(self.score)


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


class Event(models.Model):
    name = models.CharField(max_length=200, verbose_name='Название мероприятия')
    area = models.PositiveSmallIntegerField(choices=EventAreaChoices,
                                            verbose_name='Область мероприятия')
    level = models.PositiveSmallIntegerField(choices=EventLevelChoices,
                                             verbose_name='Уровень мероприятия')

    class Meta:
        verbose_name = 'Мероприятие'
        verbose_name_plural = 'Мероприятия'

    def __str__(self):
        return self.name


class WinningPlaceChoices(djchoices.DjangoChoices):
    first = djchoices.ChoiceItem(1, '1 место')
    second = djchoices.ChoiceItem(2, '2 место')
    third = djchoices.ChoiceItem(3, '3 место')
    participation = djchoices.ChoiceItem(0, 'участие')


class EventGroup(models.Model):
    name = models.CharField(max_length=30, verbose_name='Название')
    prize_winning_place = models.PositiveSmallIntegerField(choices=WinningPlaceChoices.choices,
                                                           verbose_name='Призовое место')
    students = models.ManyToManyField(Student, blank=True, verbose_name='Студенты')
    academic_group = models.ForeignKey(AcademicGroup, on_delete=models.CASCADE,
                                       verbose_name='Академическая группа')
    event = models.ForeignKey(Event, on_delete=models.CASCADE, verbose_name='Мероприятие')

    class Meta:
        verbose_name = 'Группа мероприятия'
        verbose_name_plural = 'Группы мероприятий'

    def __str__(self):
        return self.name
