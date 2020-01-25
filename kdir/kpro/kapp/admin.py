from django.contrib import admin
# Register your models here.
from .models import Article, Reporter

class ArticleDetail(admin.ModelAdmin):
    list_display = ('id', 'heading', 'created', 'reporter')
    search_fields = ('heading', 'created', 'reporter__name')

admin.site.register(Article, ArticleDetail)
# Register your models here.
class ReporterDetail(admin.ModelAdmin):
    list_display = ('id', 'n_articles')
    search_fields = ('name',)

admin.site.register(Reporter, ReporterDetail)
# Register your models here.
