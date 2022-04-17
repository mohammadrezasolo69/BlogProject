from django.shortcuts import render
from django.views.generic import ListView


# class ArticleList(ListView):
#     template_name = 'blog/article_list.html'

def test(request):
    request.user.is_authenticated
    return render(request,'blog/article_list.html')