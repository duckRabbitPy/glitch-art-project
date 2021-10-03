from django.db import models
from django import forms
from PIL import Image 
from .thumb import make_thumbnail
from .thumb import make_thumbnail2
from .thumb import make_thumbnail3
from .thumb import make_thumbnail4
from .thumb import make_thumbnail5
from .thumb import make_thumbnail6

# Create your models here.
class Project(models.Model):
    title = models.CharField(max_length=100)
    description = models.CharField(max_length=250)
    image = models.ImageField(upload_to='portfolio/images/')
    url = models.URLField(blank=True)


class Upload(models.Model): 
    name = models.CharField(max_length=50) 
    #potentially try RGB conversion with pillow here
    upload_Main_Img = models.ImageField(upload_to='images/')
    created_at = models.DateTimeField(auto_now_add=True,)
    thumbnail = models.ImageField(upload_to='images/')
    thumbnail2 = models.ImageField(upload_to='images/')
    thumbnail3 = models.ImageField(upload_to='images/')
    thumbnail4 = models.ImageField(upload_to='images/')
    thumbnail5 = models.ImageField(upload_to='images/')
    thumbnail6 = models.ImageField(upload_to='images/')

    def save(self, *args, **kwargs):
        im = Image.open(self.upload_Main_Img)
        im = im.convert('RGB')
        self.thumbnail = make_thumbnail(im, size=(500, 500))
        self.thumbnail2 = make_thumbnail2(im, size=(500, 500))
        self.thumbnail3 = make_thumbnail3(im, size=(500, 500))
        self.thumbnail4 = make_thumbnail4(im, size=(500, 500))
        self.thumbnail5 = make_thumbnail5(im, size=(500, 500))
        self.thumbnail6 = make_thumbnail6(im, size=(500, 500))
        super().save(*args, **kwargs)


class Admin_upload(models.Model):
    title = models.CharField(max_length=100)
    body = models.TextField()
    image = models.ImageField(upload_to='portfolio/images/')
  

