from django.contrib import admin
from .models import Todo
# Register your models here.
class tododetails(admin.ModelAdmin):
    list_display=('title',)
admin.site.register(Todo ,tododetails)