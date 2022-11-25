from django.urls import path
from . import views

urlpatterns = [
    path("", views.viewTables, name='index'),
    path("add/", views.add, name='add1'),
    path("add/addrecord/", views.addrecord, name='postSummit'),
    path("delete/<int:id>", views.delete, name='delete'),
    path('update/<int:id>', views.update, name='update'),
    path('update/updaterecord/<int:id>', views.updateRecord, name='updateRecord'),
]