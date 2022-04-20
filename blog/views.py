from django.shortcuts import render, Http404, redirect
from django.views.generic import ListView, DetailView, TemplateView, CreateView, UpdateView, DeleteView
from blog.models import Article, Category
from blog.forms import CreateArticleForm
from django.urls import reverse


class HomePage(ListView):
    model = Article
    paginate_by = 12
    template_name = 'blog/home_page.html'

    def get_queryset(self):

        return Article.objects.get_queryset().filter(active=True, category__active=True)


class ArticleDetailView(DetailView):
    model = Article
    template_name = 'blog/article_detail.html'


class CreateArticleView(CreateView):
    form_class = CreateArticleForm
    template_name = 'blog/create_article.html'

    def form_valid(self, form):
        article = form.save(commit=False)
        article.author = self.request.user
        form.save(commit=True)
        return super().form_valid(form)

    def get_success_url(self):
        return reverse('accounts:profile')


class UpdateArticleView(UpdateView):
    model = Article
    fields = ('title', 'img', 'description', 'time_read', 'category')
    template_name = 'blog/create_article.html'

    def get_success_url(self):
        return reverse('blog:home')


class DeleteArticleView(DeleteView):
    model = Article
    template_name = 'blog/article_confirm_delete.html'

    def get_success_url(self):
        return reverse('blog:home')


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


class ShowArticleListAuthor(ListView):
    model = Article
    template_name = 'blog/show_article_list_author.html'

    def get_queryset(self):
        user = self.kwargs['user']
        queryset = Article.objects.get_queryset().filter(active=True, category__active=True,
                                                         author__username=self.kwargs['user'],
                                                         author_id=self.kwargs['pk'])
        if queryset is None:
            raise Http404
        return queryset

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data()
        context['user'] = Article.objects.get_queryset().filter(author_id=self.kwargs['pk']).first()

        return context
