
from django.urls import path
from .views import greet, get_first_article, get_all_articles


urlpatterns = [
    path('home/', greet),
    path('first/', get_first_article),
    path('all/', get_all_articles),
]

