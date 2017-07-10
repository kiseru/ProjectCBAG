from django.contrib import admin

from . import models


class StudentInline(admin.TabularInline):
    model = models.Student
    extra = 0


class ExamInline(admin.TabularInline):
    model = models.Exam
    extra = 0


class EventInline(admin.TabularInline):
    model = models.Event
    extra = 0


class AcademicGroupAdmin(admin.ModelAdmin):
    list_display = [
        'academic_group_name',
        'course',
        'institute',
        'student_count'
    ]

    list_filter = [
        'institute',
    ]

    search_fields = [
        'academic_group_name',
    ]

    inlines = [
        StudentInline,
    ]


class StudentAdmin(admin.ModelAdmin):
    list_display = [
        'student_name',
        'academic_group',
        'educational_form',
    ]

    list_filter = [
        'academic_group',
        'educational_form',
    ]

    search_fields = [
        'student_name',
        'academic_group',
    ]

    inlines = [
        ExamInline,
        EventInline,
    ]


admin.site.register(models.AcademicGroup, AcademicGroupAdmin)
admin.site.register(models.Student, StudentAdmin)
