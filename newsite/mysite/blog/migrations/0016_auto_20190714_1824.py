# Generated by Django 2.1.5 on 2019-07-14 18:24

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0015_auto_20190714_1816'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2019, 7, 14, 18, 24, 3, 173429), verbose_name='published on'),
        ),
        migrations.AlterField(
            model_name='post',
            name='thumb',
            field=models.ImageField(blank=True, null=True, upload_to=''),
        ),
    ]
