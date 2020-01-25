from django.urls import path
from .rest_api import api_all_Customers
from .rest_api import api_add_Customer,api_put_Customer, api_delete_Customer, api_patch_Customer

urlpatterns = [
    path('all/', api_all_Customers),
    path('add/', api_add_Customer),
    path('update/',api_put_Customer),
    path('delete/',api_delete_Customer),
    path('patch/',api_patch_Customer),
]