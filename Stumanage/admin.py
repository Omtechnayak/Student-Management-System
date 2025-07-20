from django.contrib import admin
from .models import *

# Register your models here.

@admin.register(Students)
class Studentsadmin(admin.ModelAdmin):
    list_display = ('name','age','profilePic','resume','email','is_active')
    search_fields = ('name','age','is_active')
    
