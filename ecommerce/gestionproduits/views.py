# importation des modules et package
from django.shortcuts import redirect, render,get_object_or_404
from django.urls import reverse
from .models import Produits,Categorie,Card,Contact,Order,Commande
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.views.decorators.http import require_http_methods
from django.db.models.aggregates import Sum

# Vue pour la page d'aceuille
def home(request):
    user_authenticated=request.user.is_authenticated
    produits=Produits.objects.all()
    
    context={
        'produits':produits,
        'user_authenticated':user_authenticated,
         }
   
    
         
    return render (request,'gestionproduits/index.html',context)

def apropos(request):
   
    return render(request,'gestionproduits/about.html')


# vue pour la page de contact

def contact(request):
    if request.method == 'POST':
         nom=request.POST['nom']
         email=request.POST['email']
         suject=request.POST['suject']
         message=request.POST['message']
         new=Contact.objects.create(
             nom=nom,
             email=email,
             suject=suject,
             message=message
         )

    return render(request,'gestionproduits/contact-us.html')

# Vue pour l'affichage de detail d'un produit spécifique
def detail(request,my):
    user_authenticated=request.user.is_authenticated
    produit=get_object_or_404(Produits,id=my)
    
    context={
        'user_authenticated':user_authenticated,
        
         "produit":produit }
    return render(request,'gestionproduits/shop-detail.html',context)

def categorie(request,my_id):
    detail=Categorie.objects.get(id=my_id).produits_set.all()
    context={
        'detail':detail
    }

    return render(request,'gestionproduits/categories.html',context)

# Vue pour la categorie maillot
# def maillot(request):
#     user_authenticated=request.user.is_authenticated
#     maillot=Produits.objects.filter(categorie__nom_categorie='Maillots')
   
#     context={
#         'maillot':maillot,
#         'user_authenticated':user_authenticated,
#          }
   
   
#     return render (request,'gestionproduits/maillot.html',context)

# Vue pour la categorie huile
def huile(request):
    user_authenticated=request.user.is_authenticated
    huile=Produits.objects.filter(categorie__nom_categorie='Huiles')
   
    context={
        'huile':huile,
        'user_authenticated':user_authenticated,
       }
   
   
    return render (request,'gestionproduits/huile.html',context)


# Vue pour page de recherche d'un produit
def seach(request):
    user_authenticated=request.user.is_authenticated
    
    if request.method =='GET':
        seach=request.GET.get('search')
        donnee=Produits.objects.filter(nom_produit__icontains=seach) | Produits.objects.filter(categorie__nom_categorie__icontains=seach)
        context={
            'donnee':donnee,
            'user_authenticated':user_authenticated
        }
        return render (request,'gestionproduits/searche.html',context)

    return render (request,'gestionproduits/searche.html')

# Vue pour ajout d'un produit au panier
def add_to_card(request,my):
      user=request.user
      produit=get_object_or_404(Produits,id=my)
      card, _=Card.objects.get_or_create(user=user)
      order , created=Order.objects.get_or_create(user=user,ordered=False,produit=produit)
   
      if created:
          card.orders.add(order)
          card.save()
      else:
          order.quantity +=1
          order.save()

      return redirect('home')

def card(request):
    # user = request.user
    # cart= get_object_or_404(Card,user=user)
    # order=cart.orders.all()
    # nb=cart.orders.count()

    return render(request,'gestionproduits/cart.html')


# def add_to_cart(request, my):
#     user = request.user
#     product = Produits.objects.get(id=my)

#     order, created = Order.objects.get_or_create(
#         user=user, product=product
#     )

#     if created:
#         order.quantity = 1
#     else:
#         order.quantity += 1

#     order.save()

#     return redirect('home')


#vue pour supprimer le panier
def supprime_panier(request):
     user=request.user
     card=get_object_or_404(Card,user=user)
     if card:
         card.delete()
     return redirect('card')

# def supprime_produit(request, produc_id):
#     """Supprime un produit du panier de l'utilisateur ou décrémente la quantité."""

#     product = get_object_or_404(Produits, id=produc_id)
#     cart = request.user.card

#     # Trouver la commande associée au produit dans le panier
#     order = cart.orders.filter(produit=product, ordered=False).first()

#     if order:
#         # Si la quantité est supérieure à 1, décrémentez simplement la quantité
#         if order.quantity > 1:
#             order.quantity -= 1
#             order.save()
#             messages.success(request, f"La quantité de {product.nom_produit} a été réduite.")
#         else:
#             # Si la quantité est 1, supprimez complètement la commande
#             cart.orders.remove(order)
#             messages.success(request, f"{product.nom_produit} a été supprimé de votre panier.")
#     else:
#         # Si le produit n'est pas trouvé dans le panier, créez une nouvelle commande
#         Order.objects.create(user=request.user, produit=product, quantity=1)
#         messages.success(request, f"{product.nom_produit} a été ajouté à votre panier.")

#     return redirect('card')
def supprime_produit(request,my):
    card = Card.objects.get(user=request.user)
    order = card.orders.all()
    produits = Produits.objects.get(id=my)
    if produits in order:
        card.order.remove(produits)
    return redirect('card')
    
def commande(request):
    order=''
    cart=''
    total_pricese=0
    prices = {}
    total_price=0
    total_prices=0
    commande = {}
    context={}
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
          if request.method == 'POST':
       
                orders = request.POST.get('orders')
                total = request.POST.get('total')
                adresse = request.POST.get('adresse')
                orders = commande
                total = total_price
                new = Commande.objects.create(
                    orders = orders,
                    total = total,
                    adresse = adresse,
                    user = request.user
                )
                new.save()
                user.card.delete()
                return redirect('home')
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

    return render(request,'gestionproduits/commande.html',context)      

def historique(request):
   
    commande = Commande.objects.filter(user=request.user)
    return render(request,'gestionproduits/historique.html',{'commande':commande})

    


# def header(request):
#     card=get_object_or_404(Cart,user=request.user)
#     nb=card.orders.count

#     return render(request,'gestionproduits/cart.html',{"order":card.orders.all(),"nb":nb})

# @login_required
# def add_to_cart_view(request, my):
#     product = Produits.objects.get(id=my)
#     cart, created = Card.objects.get_or_create(user=request.user)
#     cart.produit.add(product)
#     cart.save()

#     return redirect('home')


# def cart_view(request):
    # cart = Card.objects.get(user=request.user)
    # if cart is None:
    #     return render(request, 'gestionproduits/no_cart.html')
    # products = cart.produit.all()
    # total = 0
    # for product in products:
    #     total += product.prix * product.quantite
    # context={
    #    'products': products,
    #    'product_count': cart.produit.count(),
    #    'total':total
    # }
    
    # return render(request, 'gestionproduits/cart.html')

# @login_required
# def supprime_produit(request, my):
#     product = Produits.objects.get(id=my)
#     cart = Card.objects.get(user=request.user)
    
#     cart.produit.remove(product)
#     cart.save()
#     return redirect('cart')

# @login_required
# def update_cart_view(request, my):
#     product = Produits.objects.get(id=my)
#     cart = Card.objects.get(user=request.user)
#     quantity = int(request.POST.get('quantity'))

#     if quantity > product.quantite:
#         quantity = product.quantite

#     cart.produit.update(quantite=quantity)
#     cart.save()

#     return redirect('cart')


# def nocart(request):

#     return render(request,'gestionproduits/no_cart.html')




    


    
    




