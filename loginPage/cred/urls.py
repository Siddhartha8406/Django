from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='Home Page'),
    path('login/', views.login, name='LoginPage'),
    path('signup/', views.signup, name='SignupPage'),
    path('signup/create', views.create, name='SignUpPage'),
    path('logout', views.logout, name='LogoutPage'),
]
