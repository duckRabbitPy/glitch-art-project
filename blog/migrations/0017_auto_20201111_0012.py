# Generated by Django 3.1 on 2020-11-11 00:12

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0016_auto_20201110_2338'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blog',
            name='date_created',
            field=models.DateTimeField(default=datetime.datetime(2020, 11, 11, 0, 12, 25, 143715, tzinfo=utc), verbose_name='date_created'),
        ),
    ]
