# Generated by Django 3.1 on 2020-11-10 15:56

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0012_auto_20201110_1123'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blog',
            name='date_created',
            field=models.DateTimeField(default=datetime.datetime(2020, 11, 10, 15, 56, 2, 282285, tzinfo=utc), verbose_name='date_created'),
        ),
    ]