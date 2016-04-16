from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
from article.models import Article


def get_article(request):
    article = Article.objects.get(id=1)
    s = 'title: %s, content: %s' % (article.title, article.content)
    return HttpResponse(s)