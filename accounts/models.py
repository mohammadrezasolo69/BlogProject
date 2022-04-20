from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    CHOOSE_IS_AUTHOR = (
        ('yes', 'yes'),
        ('no', 'no'),
    )
    is_author = models.CharField(default='no', null=True,choices=CHOOSE_IS_AUTHOR,max_length=10)
