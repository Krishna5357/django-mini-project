from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import Todo
from django.contrib.auth.forms import UserCreationForm

# Create your views here.

def home(request):
    todos = Todo.objects.all()
    context = {'todos':todos}
    return render(request,'work/home.html',context)


def register(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)

        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            return redirect('login')

    else:
        form = UserCreationForm()
    return render(request, 'registration/register.html',{'form':form})