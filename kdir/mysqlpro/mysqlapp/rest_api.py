from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.db.models import Q

from .serializers import Studentserializers
from .models import Student

@api_view(['GET'])
def api_get_one_student(request):
    obj = Student.objects.first()

    if obj:
    	serialized = Studentserializers(obj)
    	return Response(serialized.data)
    else:
    	return Response({"Message": 'student Not Foud'})


@api_view(['GET'])
def api_all_students(request):
    all_students = Student.objects.all()
    if all_students:
    	serializer = Studentserializers(all_students, many=True)
    	return Response(serializer.data)
    else:
    	return Response({"Message": 'student Not Foud'})

@api_view(['POST'])
def api_add_student(request):
    name = request.POST.get("name", None)
    student = request.POST.get("student", None)
    marks = request.POST.get("marks", None)
    

    return Response({'message': 'student fail'})

