# Generated by Django 3.1 on 2020-11-09 15:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio', '0003_auto_20201103_1901'),
    ]

    operations = [
        migrations.CreateModel(
            name='Admin_upload',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('body', models.TextField()),
                ('image', models.ImageField(upload_to='portfolio/images/')),
            ],
        ),
    ]