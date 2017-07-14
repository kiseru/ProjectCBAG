from django.conf.urls import url

from . import views

app_name = 'groups'

urlpatterns = [
    url(r'^students/$', views.students, name='students'),
    url(r'^add_student/$', views.add_student, name='add_student'),
    url(r'^student/(?P<student_id>[0-9]+)/$', views.student, name='student'),
]