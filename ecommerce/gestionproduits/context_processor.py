
from django.shortcuts import get_object_or_404, redirect, render
from django.contrib.auth.decorators import login_required
from gestionproduits.models import Card,Produits



def card(request):
    nb=''
    order=''
    cart=''
    
    if request.user.is_authenticated:
          
          cart , created=Card.objects.get_or_create(user=request.user)
          order=cart.orders.all()
          nb=cart.orders.count()
        
    else:
        nb=0
   
    
    context={
        'order': order,
        'nb': nb,
        'cart':cart,
        
     }

    return context