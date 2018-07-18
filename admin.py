from django.contrib import admin
from django import forms
from .models import Register


# Register your models here.







class Registerinfo(admin.ModelAdmin):
    list_display = ['id', 'email', 'mobilenumber', 'name','postalcode']


admin.site.register(Register, Registerinfo)







