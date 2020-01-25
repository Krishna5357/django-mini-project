from rest_framework import serializers
from .models import Student

class Studentserializers(serializers.ModelSerializer):
    class meta:
        model = Student
        fields = ('name','subject','marks')
        # depth = 2