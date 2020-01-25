from django.urls import path
from .rest_api import api_get_one_student, api_all_students,api_add_student

urlpatterns = [
    path('first/', api_get_one_student),
    path('all/', api_all_students),
    path('add/', api_add_student),

] 