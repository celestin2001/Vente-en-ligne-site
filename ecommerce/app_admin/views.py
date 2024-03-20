from django.shortcuts import redirect, render
from gestionproduits.models import *
from Compte.models import *
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required

@login_required(login_url="connexion")
def space_admin(request):
    user = request.user
    context = {
        'user':user
    }
 
    
    return render(request,'app_admin/index.html',context)

def supprimer(request,my_id):
    user = Utilisateur.objects.get(id=my_id)
    user.delete()
    return redirect('space_admin')

def supprime_commande(request,my_id):
    commande = Commande.objects.get(id=my_id)
    commande.delete()
    return redirect('space_admin')

def searche(request):
    if request.method == 'GET':
        seach = request.GET.get('searche')
        donnee=Produits.objects.filter(nom_produit__icontains=seach) | Produits.objects.filter(categorie__nom_categorie__icontains=seach)
        context = {
            'donnee':donnee
        }
        return render(request,'app_admin/searche.html',context)
    return render(request,'app_admin/searche.html')

def produit(request):
    donnee = Produits.objects.all()
    all_categorie = Categorie.objects.all()
    context = {
        'donnee':donnee,
        'all_categorie':all_categorie
    }
    if request.method == 'POST':
        nom = request.POST.get('nom')
        prix = request.POST.get('prix')
        quantite = request.POST.get('quantite')
        description = request.POST.get('description')
        categorie = request.POST.get('categorie')
        image = request.FILES.get('image')
        new = Produits.objects.create(
            nom_produit = nom,
            prix = prix,
            quantite = quantite,
            description = description,
            categorie = categorie,
            image = image
        )
        new.save()
    return render(request,'app_admin/produit.html',context)

def supprimer_produit(request,my_id):
    user = Produits.objects.get(id=my_id)
    user.delete()
    return redirect('produit')

def connexion(request):
    errors=''
    
    if request.method=='POST':
        username=request.POST['username']
        password=request.POST['password']
        user=authenticate(request,username=username,password=password)
        if user is not None:
            login(request,user)
            
            return redirect('space_admin')
        else:
            errors="nom d'utilisateur ou mot de passe incorecte"
            return render(request,'Compte/connexion.html',{'errors':errors})
    return render(request,'app_admin/login.html',{'errors':errors})

def deconnexion(request):
    logout(request)
    return redirect('connexion')