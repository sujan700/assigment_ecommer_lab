from django.contrib import admin

# Register your models here.
from .models import LabExam

# Registering the sites for lab exam
admin.site.register(LabExam)