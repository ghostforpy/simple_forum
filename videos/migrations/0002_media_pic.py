# Generated by Django 4.2.11 on 2024-04-15 19:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('videos', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='media',
            name='pic',
            field=models.ImageField(blank=True, null=True, upload_to='pics'),
        ),
    ]
