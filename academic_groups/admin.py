from django.contrib import admin

from . import models


class StudentInline(admin.TabularInline):
    model = models.Student
    extra = 0


@admin.register(models.AcademicGroup)
class AcademicGroupAdmin(admin.ModelAdmin):
    list_display = [
        'name',
        'course',
        'institute',
    ]

    search_fields = [
        'name',
    ]

    list_filter = [
        'course',
        'institute',
    ]

    inlines = [
        StudentInline,
    ]


class ExamResultInline(admin.TabularInline):
    model = models.ExamResult
    extra = 0


@admin.register(models.Student)
class StudentAdmin(admin.ModelAdmin):
    list_display = [
        'name',
        'academic_group',
        'educational_form',
    ]

    search_fields = [
        'name',
    ]

    list_filter = [
        'academic_group',
        'educational_form',
    ]

    inlines = [
        ExamResultInline,
    ]


@admin.register(models.Exam)
class ExamAdmin(admin.ModelAdmin):
    search_fields = ('name',)


@admin.register(models.EventGroup)
class EventGroupAdmin(admin.ModelAdmin):
    list_display = ('name', 'event', 'academic_group', 'prize_winning_place')
    list_filter = ('prize_winning_place',)
    search_fields = ('name',)


@admin.register(models.Event)
class EventAdmin(admin.ModelAdmin):
    list_display = ('name', 'area', 'level')
    list_filter = ('area', 'level')
    search_fields = ('name',)
