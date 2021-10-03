from django import forms 
from .models import *


class uploadForm(forms.ModelForm): 
    class Meta: 
        model = Upload 
        fields = ['name', 'upload_Main_Img',]