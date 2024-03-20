from audioop import reverse
from contextlib import nullcontext
from typing import Any
from django.utils import timezone

from django.db import models
from django.contrib.auth.models import User
from ecommerce.settings import AUTH_USER_MODEL

class Categorie(models.Model):
    nom_categorie=models.CharField(max_length=30)

    def __str__(self):
        return self.nom_categorie


class Produits(models.Model):
    nom_produit=models.CharField(max_length=30)
    prix=models.FloatField(default=0.0)
    description=models.TextField()
    quantite=models.IntegerField(null=True)
    image=models.ImageField(upload_to='%y%m%d')
    date=models.DateField(auto_now=True)
    categorie=models.ForeignKey(Categorie, on_delete=models.CASCADE)

    def __str__(self) -> str:
        return self.nom_produit
    
   

class Order(models.Model):
    user = models.ForeignKey(AUTH_USER_MODEL, on_delete=models.CASCADE)
    produit = models.ForeignKey(Produits, on_delete=models.CASCADE)
    quantity = models.IntegerField(default=1)
    ordered = models.BooleanField(default=False)
    order_date = models.DateTimeField(blank=True, null=True)

  

    def __str__(self):
        return self.produit.nom_produit
     
    

class Card(models.Model):
     user=models.OneToOneField(AUTH_USER_MODEL,on_delete=models.CASCADE)
     orders=models.ManyToManyField(Order)
   
     def __str__(self):
         return  f'{self.user.username}'
    
     def delete(self,*args, **kwargs):
         for order in self.orders.all():
             order.ordered=True
             order.order_date=timezone.now()
             order.save()

         self.orders.clear()
         super(Card, self).delete(*args, **kwargs)

# class Card(models.Model):
#     user=models.ForeignKey(AUTH_USER_MODEL,on_delete=models.CASCADE)
#     produit = models.ManyToManyField(Produits)

#     def __str__(self):
#         return self.user.username

# class CartItem(models.Model):
#     cart = models.ForeignKey(Card, on_delete=models.CASCADE)
#     product = models.ForeignKey(Produits, on_delete=models.CASCADE)
#     quantity = models.PositiveIntegerField()

class Contact(models.Model):
    nom=models.CharField(max_length=30)
    email=models.EmailField()
    suject=models.CharField(max_length=30)
    message=models.TextField()

    def __str__(self):
        return self.nom

class Commande(models.Model):
    orders = models.CharField(max_length=120)
    user = models.ForeignKey(AUTH_USER_MODEL, on_delete=models.CASCADE)
    total = models.IntegerField()
    adresse = models.CharField(max_length=30,null=True)
    date_commande = models.DateField(auto_now=True)
    livré = models.BooleanField(default=False)

    class META:
        ordering = ['date_commande']
    
    def __str__(self):
        return self.user.username
    
    # def delete(self,*args, **kwargs):
    #     if len(self.orders) ==0:
    #      self.orders.clear()
    #      super(Commande, self).delete(*args, **kwargs)



            
    
    
    
  
