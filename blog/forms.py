from django import forms
from blog.models import Article


class CreateArticleForm(forms.ModelForm):
    class Meta:
        model = Article
        fields = ('title', 'img', 'description', 'time_read', 'category')
