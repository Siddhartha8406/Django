from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('login', views.login, name='login'),
    path('signup', views.signup, name='signup'),
    path('delete', views.delete, name='delete'),
    path('logout', views.logoutUser, name='logout'),
    path('viewusers', views.viewusers, name='viewusers'),
]
