from rest_framework import serializers
from .models import Article, Reporter

class ReporterSerializer(serializers.ModelSerializer):
    class Meta:
        model = Reporter
        fields = ('id', 'name', 'n_articles')
        depth = 2

class ArticleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Article
        fields = ('id', 'heading', 'body', 'created', 'reporter')
        depth = 2