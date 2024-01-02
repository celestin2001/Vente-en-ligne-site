# importation des modules et package
from django.shortcuts import redirect, render,get_object_or_404
from django.urls import reverse
from .models import Produits,Categorie,Card,Contact,Order
from django.contrib.auth.decorators import login_required

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

# Vue pour la categorie maillot
def maillot(request):
    user_authenticated=request.user.is_authenticated
    maillot=Produits.objects.filter(categorie__nom_categorie='Maillots')
   
    context={
        'maillot':maillot,
        'user_authenticated':user_authenticated,
         }
   
   
    return render (request,'gestionproduits/maillot.html',context)

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



def supprime_panier(request):
     user=request.user
     card=get_object_or_404(Card,user=user)
     if card:
         card.delete()
     return redirect('card')

def supprime_produit(request, produc_id):
    user=request.user
    produit=get_object_or_404(Produits,id=produc_id)
    cart=Order.objects.get(user=user,produit=produit)
    cart.delete()




    return redirect('card')

# # def supprime_produit(request,my):
# #     produit=get_object_or_404(Produits,id=my)

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




    


    
    




