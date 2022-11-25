from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('page1/', include('Application1.urls')),
    path('admin/', admin.site.urls),
]