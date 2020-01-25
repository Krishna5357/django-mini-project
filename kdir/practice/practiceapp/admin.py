from django.contrib import admin
from .models import Customer

class CustomerDetail(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'dob', 'gender', 'address', 'email')
    search_fields = ('first_name', 'last_name', 'dob', 'email')

admin.site.register(Customer, CustomerDetail)
# Register your models here.
