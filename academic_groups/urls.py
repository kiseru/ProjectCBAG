from django.conf.urls import url

from . import views

app_name = 'groups'

urlpatterns = [
    url(r'^students/$', views.students, name='students'),
    url(r'^add_student/$', views.add_student, name='add_student'),
    url(r'^add_exam/$', views.add_exam, name='add_exam'),
]
