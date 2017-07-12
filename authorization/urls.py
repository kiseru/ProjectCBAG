from django.conf.urls import url

from . import views


app_name = 'auth'

urlpatterns = [
    url(r'^log_in/$', views.log_in, name='log_in'),
]
