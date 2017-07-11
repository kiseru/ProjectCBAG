from django.conf.urls import url

from . import views


app_name = 'authorization'

urlpatterns = [
    url(r'^$', views.log_in, name='log_in'),
]
