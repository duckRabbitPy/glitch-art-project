# Generated by Django 3.1 on 2020-10-28 19:49

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_auto_20201028_1948'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blog',
            name='date_created',
            field=models.DateTimeField(default=datetime.datetime(2020, 10, 28, 19, 49, 51, 305211, tzinfo=utc), verbose_name='date_created'),
        ),
    ]
