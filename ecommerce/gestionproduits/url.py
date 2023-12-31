
from django.urls import path
from.views import home,apropos,contact,detail,maillot,huile,seach,add_to_cart_view,cart_view,supprime_produit,update_cart_view,nocart

urlpatterns = [
   path('',home,name='home'),
   path('apropos',apropos,name='apropos'),
   path('contact',contact,name='contact'),
   path('detail/<int:my>',detail,name='detail'),
   path('maillot',maillot,name='maillot'),
   path('huile',huile,name='huile'),
   path('search',seach,name='search'),
  path('panier/add_to_cart_view<int:my>',add_to_cart_view,name='add-to-card'),
  
    path('cart',cart_view,name='cart'),
    path('supprime/<int:my>',supprime_produit, name='supprime'),
     path('update/<int:my>',update_cart_view, name='update_cart'),
      path('nocart',nocart, name='nocart')
   
]