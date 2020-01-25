from django.contrib import admin

from .models import Student
# class Studentregister(admin.ModelAdmin):
#     list_display=('name','subject','marks')
#     search_display=('name','subject','marks')

admin.site.register(Student)