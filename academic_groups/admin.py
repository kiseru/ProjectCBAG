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


class ExamResultInline(admin.TabularInline):
    model = models.ExamResult
    extra = 0


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


class CuratorAdmin(admin.ModelAdmin):
    inlines = [
        StudentInline,
    ]


admin.site.register(models.AcademicGroup, AcademicGroupAdmin)
admin.site.register(models.Student, StudentAdmin)
admin.site.register(models.Exam)
admin.site.register(models.Event)
admin.site.register(models.EventGroup)
admin.site.register(models.EventArea)
admin.site.register(models.EventLevel)
admin.site.register(models.PrizeWinningPlace)
