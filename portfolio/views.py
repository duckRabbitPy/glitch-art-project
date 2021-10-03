from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Project
from .forms import *
from PIL import Image
from PIL.ImageFilter import (
    BLUR, CONTOUR, DETAIL, EDGE_ENHANCE, EDGE_ENHANCE_MORE,
    EMBOSS, FIND_EDGES, SMOOTH, SMOOTH_MORE, SHARPEN
)


# Create your views here.

def about(request):
	return render(request, 'portfolio/about.html')


def upload_image_view(request): 
  
    if request.method == 'POST': 
        form = uploadForm(request.POST, request.FILES) 
        if form.is_valid(): 
            try:
                form.save()
                return redirect('processed_images') 
            except ValueError as error:
                return redirect('upload_error')
        
    else: 
        form = uploadForm() 
        return render(request, 'portfolio/upload_image_form.html', {'form' : form})


def error_page(request):
    return render(request, 'portfolio/upload_error.html')
 

def display_upload_images(request): 
    if request.method == 'GET':

            # getting all the objects of Upload.
            # uploads = Upload.objects.all()
            #made to be a list so uploads is iterable in template
            uploads = [Upload.objects.latest('created_at')]
            return render(request, 'portfolio/display_upload_images.html', {'uploads':uploads})


def display_upload_imagesB(request):
    if request.method == 'GET': 
        uploads = [Upload.objects.latest('created_at')]
        return render(request, 'portfolio/display_upload_imagesB.html', {'uploads':uploads})

def display_upload_imagesC(request):
    if request.method == 'GET': 
        uploads = [Upload.objects.latest('created_at')]
        return render(request, 'portfolio/display_upload_imagesC.html', {'uploads':uploads})

def display_upload_images_inverted(request):
    if request.method == 'GET': 
        uploads = [Upload.objects.latest('created_at')]
        return render(request, 'portfolio/display_upload_images_invert.html', {'uploads':uploads})

def display_upload_images_dull(request):
    if request.method == 'GET': 
        uploads = [Upload.objects.latest('created_at')]
        return render(request, 'portfolio/display_upload_images_dull.html', {'uploads':uploads})

def dislay_community(request): 
    if request.method == 'GET': 
        # getting all the objects of Upload.
        uploads = Upload.objects.all()
        return render(request, 'portfolio/community_gallery.html', {'uploads':uploads})


def display_admin_images(request):
    admin_uploads = Admin_upload.objects.all()
    # getting all the objects of admin_uploads. 
    return render(request, 'portfolio/display_admin_images.html',{'admin_uploads':admin_uploads})



''' How to clear the objects uploads = Upload.objects.all().uploads.delete() in display community view'''






