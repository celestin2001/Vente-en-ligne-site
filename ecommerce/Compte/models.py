from typing import Iterable
from django.db import models
from django.contrib.auth.models import AbstractUser
from django.forms import ValidationError


class Utilisateur(AbstractUser):
    phone = models.CharField(max_length=30)
    image = models.ImageField(upload_to='image',blank=True)
    password2 = models.CharField(max_length=30,default=1234)
    last_name = models.CharField(max_length=30)
    first_name = models.CharField(max_length=30)
    token = models.CharField(max_length=100)

    # def save(self,*args, **kwargs):
    #     if len(self.phone) <9 or len(self.phone) >9:
    #         raise ValidationError("le numero de telephone doit être au format guinneenn ### ## ## ##")
    #     if self.phone[0] != 6 :
    #         raise ValidationError("ce numero n'est pas au format guinneen")
    #     if self.phone[1] !=6 or self.phone[1] != 2:
    #         raise ValidationError("ce numero n'est pas au format guinneen")
    #     super(Utilisateur,self).save(*args, **kwargs)

    def __str__(self):
        return self.username


