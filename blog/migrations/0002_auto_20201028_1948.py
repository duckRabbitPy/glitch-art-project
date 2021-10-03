# Generated by Django 3.1 on 2020-10-28 19:48

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='blog',
            name='url',
        ),
        migrations.AddField(
            model_name='blog',
            name='date_created',
            field=models.DateTimeField(default=datetime.datetime(2020, 10, 28, 19, 48, 16, 334501, tzinfo=utc), verbose_name='date_created'),
        ),
    ]
