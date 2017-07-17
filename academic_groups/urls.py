from django.conf.urls import url

from . import views

app_name = 'groups'

urlpatterns = [
    url(r'^students/$', views.students, name='students'),
    url(r'^add_student/$', views.add_student, name='add_student'),
    url(r'^students/add_exam/$', views.add_exam, name='add_exam'),
    url(r'^student/(?P<student_id>[0-9]+)/$', views.student_show, name='student'),
    url(r'^student/(?P<student_id>[0-9]+)/edit_student_exams/$', views.edit_student_exams, name='edit_student_exams'),
    url(r'^student/(?P<student_id>[0-9]+)/delete_student/$', views.delete_student, name='delete_student'),
    url(r'^students/delete_exam/', views.delete_exam, name='delete_exam'),
    url(r'^events/$', views.events, name='events'),
    url(r'^add_event/$', views.add_event, name='add_event'),
    url(r'^event/add_student/$', views.event_add_student, name='event_add_student'),
    url(r'^edit_event_group/$', views.edit_event_group, name='edit_event_group'),
    url(r'^delete_event_group/$', views.delete_event_group, name='delete_event_group')
]
