# Generated by Django 3.2 on 2022-04-17 11:51

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_alter_category_sub_category'),
    ]

    operations = [
        migrations.AddField(
            model_name='category',
            name='active',
            field=models.BooleanField(default=False, verbose_name='active: Y/N'),
        ),
        migrations.AlterField(
            model_name='article',
            name='active',
            field=models.BooleanField(default=False, verbose_name='active: Y/N'),
        ),
        migrations.AlterField(
            model_name='article',
            name='publish',
            field=models.DateTimeField(default=datetime.datetime(2022, 4, 17, 11, 51, 43, 74983, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='article',
            name='update',
            field=models.DateTimeField(default=datetime.datetime(2022, 4, 17, 11, 51, 43, 74966, tzinfo=utc)),
        ),
    ]
