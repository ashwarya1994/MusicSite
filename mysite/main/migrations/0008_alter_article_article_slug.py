# Generated by Django 3.2.5 on 2022-08-09 06:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0007_profile'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='article_slug',
            field=models.SlugField(unique=True),
        ),
    ]
