# Generated by Django 3.1 on 2020-11-11 18:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio', '0008_upload_created_at'),
    ]

    operations = [
        migrations.AddField(
            model_name='upload',
            name='thumbnail6',
            field=models.ImageField(default=-1990, upload_to='images/'),
            preserve_default=False,
        ),
    ]
