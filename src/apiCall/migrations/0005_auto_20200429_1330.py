# Generated by Django 3.0.5 on 2020-04-29 08:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('apiCall', '0004_auto_20200429_1214'),
    ]

    operations = [
        migrations.AlterField(
            model_name='youtubemodel',
            name='publish_datetime',
            field=models.DateTimeField(),
        ),
    ]
