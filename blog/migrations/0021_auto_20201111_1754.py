# Generated by Django 3.1 on 2020-11-11 17:54

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0020_auto_20201111_1335'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blog',
            name='date_created',
            field=models.DateTimeField(default=datetime.datetime(2020, 11, 11, 17, 54, 46, 428591, tzinfo=utc), verbose_name='date_created'),
        ),
    ]
