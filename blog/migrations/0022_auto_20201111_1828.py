# Generated by Django 3.1 on 2020-11-11 18:28

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0021_auto_20201111_1754'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blog',
            name='date_created',
            field=models.DateTimeField(default=datetime.datetime(2020, 11, 11, 18, 26, 3, 183833, tzinfo=utc), verbose_name='date_created'),
        ),
    ]