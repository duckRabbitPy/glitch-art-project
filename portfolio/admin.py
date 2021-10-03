from django.contrib import admin
from .models import Project
from .models import Admin_upload

# Register your models here.
admin.site.register(Project)

admin.site.register(Admin_upload)
