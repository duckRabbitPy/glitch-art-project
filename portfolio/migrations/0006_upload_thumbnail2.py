# Generated by Django 3.1 on 2020-11-10 23:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio', '0005_upload_thumbnail'),
    ]

    operations = [
        migrations.AddField(
            model_name='upload',
            name='thumbnail2',
            field=models.ImageField(default='thedefaultgiven', upload_to='images/'),
            preserve_default=False,
        ),
    ]
