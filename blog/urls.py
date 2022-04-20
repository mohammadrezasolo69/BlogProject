from django.urls import path
from blog import views

app_name = 'blog'
urlpatterns = [
    path('', views.HomePage.as_view(), name='home'),
    path('category/list/<slug>', views.CategoryList.as_view(), name='category_list'),
    path('detail/<pk>/<slug>', views.ArticleDetailView.as_view(), name='article_detail'),
    path('show-category-in-nav-render-partial/', views.ShowCategoryPartialView.as_view(), name='show_category_partial'),
    path('author/list/<pk>/<user>', views.ShowArticleListAuthor.as_view(), name='show_article_list_author'),

    path('create/', views.CreateArticleView.as_view(), name='create_article'),
    path('update/<pk>/<slug>', views.UpdateArticleView.as_view(), name='update_article'),
    path('delete/<pk>/<slug>', views.DeleteArticleView.as_view(), name='delete_article'),

]
