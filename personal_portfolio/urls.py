"""personal_portfolio URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings
from portfolio import views

urlpatterns = [

    path('admin/', admin.site.urls),
    path('blog/', include('blog.urls')),
    path('', views.upload_image_view, name = 'image_upload'),
    path('about', views.about, name='about'),
    path('image_upload', views.upload_image_view, name = 'image_upload'), 
    path('upload_error', views.error_page, name='upload_error'),
    path('processed_images', views.display_upload_images, name = 'processed_images'),
    path('processed_imagesB', views.display_upload_imagesB, name = 'processed_imagesB'),
    path('processed_imagesC', views.display_upload_imagesC, name = 'processed_imagesC'),
    path('processed_images_inverted', views.display_upload_images_inverted, name = 'processed_images_inverted'),
    path('processed_images_dull', views.display_upload_images_dull, name = 'processed_images_inverted'),
    path('display_admin_images', views.display_admin_images, name = 'admin_images'),
    path('community_gallery', views.dislay_community, name='community_gallery'),

]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)