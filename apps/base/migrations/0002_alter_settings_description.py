# Generated by Django 5.1.1 on 2024-10-04 14:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='settings',
            name='description',
            field=models.TextField(default='Описание', verbose_name='Описание'),
        ),
    ]
