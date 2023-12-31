from django.contrib import admin
from .models import Categorie,Produits,Card,CartItem,Contact


class liste(admin.ModelAdmin):
    list_display=('nom_produit','prix','date','categorie')
    search_fields=('categorie','nom_produit')
    ordering=('date','categorie')

    def aperçue_description(self,produit):
        text=Produits.description[:40]
        if len(produit.description)>40:
            return '{}...'.format(text)
        else: return text

admin.site.register(Produits,liste)
admin.site.register(Categorie)
# admin.site.register(Order)
admin.site.register(Card)
admin.site.register(CartItem)
admin.site.register(Contact)

    



