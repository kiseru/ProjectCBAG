from django.conf.urls import include
from django.contrib import admin
from django.urls import path

from ProjectCBAG import views

urlpatterns = [
    path('', views.HomeView.as_view(), name='home'),
    path('admin/', admin.site.urls),
    path('auth/', include('authorization.urls')),
    path('groups/', include('academic_groups.urls')),
]
