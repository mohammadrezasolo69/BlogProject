from django.urls import reverse
from django.db import models
from ckeditor.fields import RichTextField
from django.conf import settings
from blog.utile.slug_generate import unique_slug_generator
from django.db.models.signals import pre_save


class Category(models.Model):
    title = models.CharField(max_length=200)
    slug = models.SlugField(unique=True, null=True)
    description = RichTextField(blank=True, null=True)
    active = models.BooleanField(default=False, verbose_name='active: Y/N')

    class Meta:
        ordering = ('-id',)
        verbose_name = 'Category'
        verbose_name_plural = 'Categories'

    def __str__(self):
        return self.title


class Article(models.Model):
    title = models.CharField(max_length=200)
    slug = models.SlugField(unique=True, null=True, blank=True)
    img = models.ImageField(upload_to='img/')
    description = RichTextField()
    time_read = models.PositiveIntegerField()
    created = models.DateTimeField(auto_now_add=True)
    update = models.DateTimeField(auto_now=True)
    publish = models.DateTimeField(auto_now=True)
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='articles')
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='articles')
    active = models.BooleanField(default=False, verbose_name='active: Y/N')

    class Meta:
        ordering = ('-id',)
        verbose_name = 'Article'
        verbose_name_plural = 'Articles'

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('blog:article_detail', args=[self.id, self.slug])


def article_pre_save_receiver(sender, instance, *args, **kwargs):
    if not instance.slug:
        instance.slug = unique_slug_generator(instance)


pre_save.connect(article_pre_save_receiver, Article)
