from django.shortcuts import render, Http404
from django.views.generic import ListView, DetailView, TemplateView
from blog.models import Article, Category


# todo: 1.ListArticle
# todo: 2.DetailArticle


class HomePage(ListView):
    model = Article
    paginate_by = 12
    template_name = 'blog/home_page.html'


class ArticleDetailView(DetailView):
    model = Article
    template_name = 'blog/article_detail.html'


class ShowCategoryPartialView(TemplateView):
    template_name = 'blog/show_category_partial.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['category'] = Category.objects.get_queryset().filter(active=True)
        return context


class CategoryList(ListView):
    model = Category
    template_name = 'blog/category_list.html'
    context_object_name = 'category'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        category = Category.objects.get_queryset().filter(slug=self.kwargs['slug']).first()

        if category is None:
            raise Http404

        category_list = category.articles.all()
        context['category'] = category
        context['category_list'] = category_list

        return context
