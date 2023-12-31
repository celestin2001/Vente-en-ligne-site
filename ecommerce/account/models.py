from django.db import models
from django.contrib.auth.models import AbstractUser

class Utilisateur(AbstractUser):
    phone=models.IntegerField(null=True,blank=True)
    image=models.ImageField(null=True,blank=True)
    password2=models.CharField(max_length=30,default=1234)
    last_name=models.CharField(max_length=30,default='Kamano')
    first_name=models.CharField(max_length=30,default='David')
    


