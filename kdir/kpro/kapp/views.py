from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound
from .models import Article

# Create your views here.

def greet(request):
    return HttpResponse("<H1> Fan of Allu Arjun </H1>")


def get_first_article(request):
    obj = Article.objects.first()

    if obj:
        context = {
            'article': obj
        }
        return render(request, 'one.html', context)
    else:
        return HttpResponseNotFound("Article not found")

def get_all_articles(request):
    objs = Article.objects.all()

    if objs:
        context = {
            'all_articles': objs
        }
        return render(request, 'all.html', context)
    else:
        return HttpResponseNotFound("Article not found")


