from django.urls import path

from authorization import views

app_name = 'auth'

urlpatterns = [
    path('login/', views.LoginFormView.as_view(), name='login'),
    path('logout/', views.LogoutView.as_view(), name='logout'),
]
