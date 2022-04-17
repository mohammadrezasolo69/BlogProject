from django.urls import path
from blog import views

app_name = 'blog'
urlpatterns = [
    # path('', views.ArticleList.as_view(), name='article_list')
    path('', views.test, name='article_list')
]
