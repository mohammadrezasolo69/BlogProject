from django.urls import path
from blog import views

app_name = 'blog'
urlpatterns = [
    path('', views.HomePage.as_view(), name='home'),
    path('category/list/<slug>', views.CategoryList.as_view(), name='category_list'),
    path('detail/<pk>/<slug>', views.ArticleDetailView.as_view(), name='article_detail'),
    path('show-category-in-nav-render-partial/', views.ShowCategoryPartialView.as_view(), name='show_category_partial'),
]
