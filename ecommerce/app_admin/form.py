from django import forms
from gestionproduits.models import *
from Compte.models import *

class Rowform(forms.ModelForm):
    class Meta:
        model = Produits
        fields = ['nom_produit','image','prix','quantite','description','categorie']

class UserForm(forms.ModelForm):
    class Meta:
        model = Utilisateur
        fields = ['username','email','phone','first_name','image']