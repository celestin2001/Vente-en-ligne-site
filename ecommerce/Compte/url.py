from django.urls import path,include
from.views import *
from django.views import generic
from django.contrib.auth import views 
from django.contrib.auth.views import PasswordChangeView,PasswordChangeDoneView,PasswordResetView,PasswordResetDoneView,PasswordResetConfirmView,PasswordResetCompleteView

urlpatterns = [
path('signup',signup,name='signup'),
path('connexion',connexion,name='connexion'),
path('change_password',change_password,name='change_pass'),
path('change',PasswordChangeView.as_view(template_name='account/change_password.html',
                                             
          success_url='confirme'),name='change_password'),
    path('confirme',PasswordChangeDoneView.as_view(template_name='account/password_change_done.html'),name='confirme'),
path('deconnexion',deconnexion,name='deconnexion'),
 path('reset_password',views.PasswordResetView.as_view(template_name='Compte/password_reset.html'),name='reset_password'),
 path('password_reset_send',views.PasswordResetDoneView.as_view(template_name='Compte/password_reset_done.html'),name='password_reset_done'),
 path('reset/<uidb64>/<token>',views.PasswordResetConfirmView.as_view(template_name='Compte/password_confirme.html'),name='password_reset_confirm'),
 path('reset_password_complete',views.PasswordResetCompleteView.as_view(template_name='Compte/password_reset.html'),name='password_complete'),
 path('profil',profil,name='profil'),
 path('recupere_password',reset_password,name="reset_password"),
 path('password/<str:token>',modifier_password,name='password')

]
