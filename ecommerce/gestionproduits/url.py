
from django.urls import path
from.views import home,apropos,contact,detail,maillot,huile,seach,add_to_card,card,supprime_panier,supprime_produit

urlpatterns = [
   path('',home,name='home'),
   path('apropos',apropos,name='apropos'),
   path('contact',contact,name='contact'),
   path('detail/<int:my>',detail,name='detail'),
   path('maillot',maillot,name='maillot'),
   path('huile',huile,name='huile'),
   path('search',seach,name='search'),
   path('panier/add_to_cart_view<int:my>',add_to_card,name='add-to-card'),
  
     path('card',card,name='card'),
     path('supprime/<int:product_id>',supprime_produit, name='supprime_produit'),
  #    path('update/<int:my>',update_cart_view, name='update_cart'),
      path('supprime',supprime_panier, name='supprime')
   
]