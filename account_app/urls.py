from django.urls import path

from . import views

app_name = 'account_app'

urlpatterns = [
    path('login', views.UserLogin.as_view(), name='login'),
    path('register', views.RegisterView.as_view(), name='register'),
    path('checkotp', views.CheckOtpView.as_view(), name='check_otp'),
]