from django.urls import path
from .views import *
urlpatterns = [
 path('space_admin',space_admin,name="space_admin"),
 path('supprime/<int:my_id>',supprimer,name='suppression'),
 path('supprime_commande/<int:my_id>',supprime_commande,name='supprime_commande'),
 path('search',searche,name='searche'),
 path('produit',produit,name='produit'),
  path('supprime_produit/<int:my_id>',supprimer_produit,name='supprime_commande'),
  path('connexion',connexion,name="connexion"),
  path('deconnexion',deconnexion,name="deconnexion")
]