from django.shortcuts import render
from django.http import HttpResponse
from .models import Blog

def all_blogs(request):
	blogs = Blog.objects.all().order_by('date_created')
	return render(request, 'blog/all_blogs.html',{'blogs':blogs})