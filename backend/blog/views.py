from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView, DetailView
from .models import Article


class ArticleList(ListView):
    def get_queryset(self):
        return Article.objects.filter(status=True)


class ArticleDetail(DetailView):
    def get_object(self, **kwargs):
        return get_object_or_404(
            Article.objects.filter(status=True),
            pk=self.kwargs.get("pk")
        )