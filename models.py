from django.db import models
from django.utils import timezone


# Create your models here

class Register(models.Model):
  id = models.AutoField(primary_key=True)
  created = models.DateTimeField(auto_now_add=True, editable=False)
  email = models.CharField(max_length=100, null=True, blank=True)
  mobilenumber = models.CharField(max_length=200, null=True, blank=True)
  postalcode =  models.CharField(max_length=200, null=True, blank=True)
  name = models.CharField(max_length=200, null=True, blank=True)











