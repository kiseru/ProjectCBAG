from django.conf.urls import url

from . import views

app_name = 'groups'

urlpatterns = [
    url(r'^students/$', views.students, name='students'),
    url(r'^add_student/$', views.add_student, name='add_student'),
    url(r'^add_exam/$', views.add_exam, name='add_exam'),
    url(r'^student/(?P<student_id>[0-9]+)/$', views.student_show, name='student'),
    url(r'^student/(?P<student_id>[0-9]+)/edit_student_exams/$', views.edit_student_exams, name='edit_student_exams'),
    url(r'^student/(?P<student_id>[0-9]+)/delete_student/$', views.delete_student, name='delete_student'),
]
