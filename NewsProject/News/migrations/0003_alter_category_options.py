# Generated by Django 5.0.1 on 2024-01-16 10:07

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('News', '0002_category_alter_news_options_alter_news_content_and_more'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='category',
            options={'ordering': ['title'], 'verbose_name': 'Категория', 'verbose_name_plural': 'Категории'},
        ),
    ]