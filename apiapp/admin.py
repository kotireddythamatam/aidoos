from django.contrib import admin
from . models import Student
# Register your models here.

class Adminclass(admin.ModelAdmin):
    list_display = ['name','course','marks']

admin.site.register(Student,Adminclass)
