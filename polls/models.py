from django.db import models

# Create your models here.

class user(models.Model):
    user_name = models.CharField(max_length=200,default="")
    age = models.IntegerField(default=0)
    phone = models.CharField(max_length=11,default="")
