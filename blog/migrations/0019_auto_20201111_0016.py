# Generated by Django 3.1 on 2020-11-11 00:16

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0018_auto_20201111_0013'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blog',
            name='date_created',
            field=models.DateTimeField(default=datetime.datetime(2020, 11, 11, 0, 16, 7, 780931, tzinfo=utc), verbose_name='date_created'),
        ),
    ]
