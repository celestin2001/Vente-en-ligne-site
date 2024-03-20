from django.shortcuts import get_object_or_404, redirect, render
from django.contrib.auth.decorators import login_required
from gestionproduits.models import Card,Produits,Order,Categorie,Commande
from Compte.models import Utilisateur
from django.db.models.aggregates import Sum


def space_admin(request):
    produit = Produits.objects.count()
    utilisateur = Utilisateur.objects.count()
    commande = Commande.objects.count()
    commande_livre = Commande.objects.filter(livré=True).count()
    visiteur = Utilisateur.objects.all()
    commandes = Commande.objects.all()
    user = request.user
    context = {
        'produit':produit,
        'utilisateur':utilisateur,
        'commande':commande,
        'commande_livre':commande_livre,
        'user':user,
         'visiteur':visiteur,
         'commandes':commandes
    }
    return context