# Generated by Django 4.2.11 on 2024-04-15 20:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('themes', '0002_topic_subsection'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='body',
            field=models.TextField(verbose_name='Контент'),
        ),
        migrations.AlterField(
            model_name='topic',
            name='description',
            field=models.CharField(max_length=100, verbose_name='Описание'),
        ),
        migrations.AlterField(
            model_name='topic',
            name='title',
            field=models.CharField(max_length=50, verbose_name='Тема'),
        ),
    ]
