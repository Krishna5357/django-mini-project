from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound
from .models import Student
# Create your views here.
def Student_list(request):
    lis= Student.objects.all()

    if lis:
        context={
            'Student':lis
        }
        return render(request, context)
    else:
        return HttpResponseNotFound('student not found')
