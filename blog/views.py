from django.shortcuts import render
from django.views.generic import ListView,DetailView
from blog.models import Article


# todo: 1.ListArticle
# todo: 2.DetailArticle


class ArticleListView(ListView):
    model = Article
    paginate_by = 9


class ArticleDetailView(DetailView):
    model = Article
