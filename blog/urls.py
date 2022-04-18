from django.urls import path
from blog import views

app_name = 'blog'
urlpatterns = [
    path('', views.ArticleListView.as_view(), name='article_list'),
    path('detail/<pk>/<slug>', views.ArticleDetailView.as_view(), name='article_detail')
]
