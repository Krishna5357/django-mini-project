from django.contrib import admin
from django.urls import path
from .views import Student_list

urlpatterns = [
    path('admin/', admin.site.urls),
    path('print/',Student_list)
]
