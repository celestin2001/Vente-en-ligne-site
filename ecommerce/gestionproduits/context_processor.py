
from django.shortcuts import get_object_or_404, render
from django.contrib.auth.decorators import login_required
from gestionproduits.models import Card



def cart_view(request):
    products=''
    cart=''
    if request.user.is_authenticated:
        cart = Card.objects.get(user=request.user)
        product_count=cart.produit.count
        products = cart.produit.all()
        
    else:
       product_count=0

    context={
       'products': products,
       'product_count': product_count,
       'cart':cart
    }

    return context