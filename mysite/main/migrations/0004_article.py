# Generated by Django 3.2.5 on 2022-08-08 16:17

from django.db import migrations, models
import tinymce.models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0003_auto_20220808_1940'),
    ]

    operations = [
        migrations.CreateModel(
            name='Article',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('article_title', models.CharField(max_length=200)),
                ('article_published', models.DateTimeField(verbose_name='date published')),
                ('article_image', models.ImageField(upload_to='images/')),
                ('article_content', tinymce.models.HTMLField()),
                ('article_slug', models.SlugField()),
            ],
        ),
    ]
