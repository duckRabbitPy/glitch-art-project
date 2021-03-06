from django.db import models
from django.utils import timezone


# Create your models here.
class Blog(models.Model):
    title = models.CharField(max_length=100)
    body = models.TextField()
    image = models.ImageField(upload_to='blog/images/')
    date_created = models.DateTimeField('date_created', default=timezone.now(), blank=False)
   