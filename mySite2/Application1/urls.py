from django.urls import path
from . import views

urlpatterns = [
    path("", views.viewTables, name='index'),
    path("add/", views.addRecord, name='add'),

]