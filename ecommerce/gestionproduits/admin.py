from django.contrib import admin
<<<<<<< HEAD
from .models import Categorie,Produits,Card,Order,Contact,Commande
=======
from .models import Categorie,Produits,Card,Order,Contact
>>>>>>> 491e159427bfe34e5cab555ac31faebd4d15c889


class liste(admin.ModelAdmin):
    list_display=('nom_produit','prix','date','categorie')
    search_fields=('categorie','nom_produit')
    ordering=('date','categorie')

    def aperçue_description(self,produit):
        text=Produits.description[:40]
        if len(produit.description)>40:
            return '{}...'.format(text)
        else: return text

class liste2(admin.ModelAdmin):
    list_display=('username','phone')


class liste3(admin.ModelAdmin):
    list_display=('user','total','date_commande')

admin.site.register(Produits,liste)
admin.site.register(Categorie)
# admin.site.register(Order)
admin.site.register(Card)
admin.site.register(Order)
admin.site.register(Contact)
admin.site.register(Commande,liste3)

    



