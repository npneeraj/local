# Generated by Django 2.1.5 on 2019-07-11 09:36

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='post',
            old_name='body',
            new_name='content',
        ),
        migrations.RemoveField(
            model_name='post',
            name='date',
        ),
        migrations.AddField(
            model_name='post',
            name='published',
            field=models.DateTimeField(default=datetime.datetime(2019, 7, 11, 9, 36, 49, 7962), verbose_name='date published'),
        ),
    ]
