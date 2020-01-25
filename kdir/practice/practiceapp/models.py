from django.db import models
from django.utils import timezone
class Customer(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    dob = models.CharField(max_length=10)
    gender = models.CharField(max_length=10)
    address = models.CharField(max_length=100)
    email = models.CharField(max_length=30)