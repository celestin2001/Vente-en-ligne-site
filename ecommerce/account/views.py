from django.shortcuts import render,redirect
from.models import Utilisateur
from gestionproduits.models import Card,Order
from django.contrib.auth import login,logout,authenticate
from django.contrib.auth.decorators import login_required
from django.contrib import messages
import random as rd

def connexion(request):
    errors=''
    
    if request.method=='POST':
        username=request.POST['username']
        password=request.POST['password']
        user=authenticate(request,username=username,password=password)
        if user is not None:
            login(request,user)
            
            return redirect('home')
        else:
            errors='Vos informations ne sont pas conformes'
            return render(request,'account/connexion.html',{'errors':errors})
    return render(request,'account/connexion.html',{'errors':errors})

def signup(request):
    if request.method =='POST':
        username=request.POST.get('username')
        last_name=request.POST.get('lastname')
        first_name=request.POST.get('firstname')
        email=request.POST.get('email')
        phone=request.POST.get('phone')
        image=request.FILES.get('image')
        password=request.POST.get('password')
        password2=request.POST.get('password2')
        user_name=Utilisateur.objects.filter(username=username)
        if user_name:
             errors="Cet identifiant existe deja esssayer un autre"
             return render(request,'account/signup.html',{'errors':errors})
        if password != password2:
            errors="vos mots de passes ne sont pas conformes"
            return render(request,'account/signup.html',{'errors':errors})
        if len(password)<=7:
            errors="le mot de passe doit contenir au moins huit caractères"
            return render(request,'account/signup.html',{'errors':errors})
        email_exist=Utilisateur.objects.filter(email=email)
        if email_exist:
            errors="cet email existe deja entrez autre email"
            return render(request,'account/signup.html',{'errors':errors})
        user=Utilisateur.objects.create_user(
            username,
            email,
            password
        )
        # user.save()
        login(request,user)
        return redirect('connexion')
        # return render(request,'account/connexion.html')
    return render(request,'account/signup.html')



# @login_required
def deconnexion(request):
    logout(request)
    return redirect('home')
