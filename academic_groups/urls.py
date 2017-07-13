from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^students/$', views.students, name='students'),
]