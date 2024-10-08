# Generated by Django 5.1.1 on 2024-10-08 13:44

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='News',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='news_images/')),
                ('title', models.CharField(max_length=155, verbose_name='Заголовок')),
                ('description', models.TextField(default='Описание', verbose_name='Описание')),
            ],
            options={
                'verbose_name': '',
                'verbose_name_plural': 'Новости',
            },
        ),
    ]
