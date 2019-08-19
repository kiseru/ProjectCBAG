from django.conf.urls import url
from django.urls import path

from . import views

app_name = 'groups'

urlpatterns = [
    path('academic_groups/<int:pk>', views.AcademicGroupDetailView.as_view(), name='academicgroup_detail'),
    path('students/new', views.StudentCreateView.as_view(), name='student_create'),
    path('students/<int:pk>/delete', views.StudentDeleteView.as_view(), name='student_delete'),
    path('students/<int:pk>', views.StudentDetailView.as_view(), name='student_detail'),
    path('exams/', views.AcademicGroupExamListView.as_view(), name='exam_list'),
    path('exams/new', views.AcademicGroupExamCreateView.as_view(), name='exam_create'),
    path('exams/<int:pk>/delete', views.AcademicGroupExamDeleteView.as_view(), name='exam_delete'),
    url(r'^student/(?P<student_id>[0-9]+)/edit_student_exams/$', views.edit_student_exams, name='edit_student_exams'),
    url(r'^students/delete_exam/', views.delete_exam, name='delete_exam'),
    url(r'^events/$', views.events, name='events'),
    url(r'^add_event/$', views.add_event, name='add_event'),
    url(r'^event/add_student/$', views.event_add_student, name='event_add_student'),
    url(r'^edit_event_group/$', views.edit_event_group, name='edit_event_group'),
    url(r'^delete_event_group/$', views.delete_event_group, name='delete_event_group'),
    url(r'^jury/$', views.jury, name='jury'),
]
