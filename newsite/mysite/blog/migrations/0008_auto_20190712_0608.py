# Generated by Django 2.1.5 on 2019-07-12 06:08

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0007_auto_20190712_0607'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2019, 7, 12, 6, 8, 48, 868854), verbose_name='published on'),
        ),
    ]
