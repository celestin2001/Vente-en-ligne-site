
from django.shortcuts import get_object_or_404, redirect, render
from django.contrib.auth.decorators import login_required

from gestionproduits.models import Card,Produits,Order,Categorie,Commande
from django.db.models.aggregates import Sum

from gestionproduits.models import Card,Produits




def card(request):
    nb=''
    order=''
    cart=''
 
    total_pricese=0
    prices = {}
    total_price=0
    total_prices=0
    commande = {}
    existe = ''
    categorie=Categorie.objects.all()
    
    if request.user.is_authenticated:
          user = request.user
          cart , created=Card.objects.get_or_create(user=request.user)
          existe = Card.user is None
          order=cart.orders.all()
          nb=cart.orders.count()
          
          for item in order:
             prices[item.produit.id] =item.quantity * item.produit.prix

        # Calcul du prix total des produits
          items = Order.objects.filter(user=request.user)
          total_price = sum(prices.values())
          total_prices = items.aggregate(
          total_pricese=Sum('produit__prix'))
          for item in order:
             commande[item.produit.nom_produit] =item.quantity
        #   if request.method == 'POST':
       
        #         orders = request.POST.get('orders')
        #         total = request.POST.get('total')
        #         adresse = request.POST.get('adresse')
        #         orders = commande
        #         total = total_price
        #         new = Commande.objects.create(
        #             orders = orders,
        #             total = total,
        #             adresse = adresse,
        #             user = request.user
        #         )
        #         new.save()
        #         user.card.delete()
        #         return redirect('home')
       
    else:
        nb=0
        # formulaire pour lancer la commande
    
  
        

    

    # calculer le prix total de chaque produit
    
    
    

    
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

        'prices':prices,
        'total_price':total_price,
        'total_pricese':total_pricese,
        'total_prices':total_prices,
        'categorie':categorie,
        'commande':commande,
        'existe':existe

     }

    return context 
