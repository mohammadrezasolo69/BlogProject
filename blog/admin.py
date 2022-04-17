from django.contrib import admin
from blog.models import Category, Article


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('title','active')
    list_editable = ('active',)

@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    list_display = ('title', 'time_read', 'created', 'update', 'publish', 'active', 'author', 'category')
    list_editable = ('active',)
    list_filter = ('category', 'author', 'active',)
