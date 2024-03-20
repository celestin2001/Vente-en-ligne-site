from django.shortcuts import render,redirect

from ecommerce import settings
from.models import Utilisateur
from gestionproduits.models import Card,Order
from django.contrib.auth import login,logout,authenticate
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.contrib.auth.hashers import check_password
import secrets
from django.core.mail import EmailMessage

# from django.contrib.auth.hashers import check_password
# from django.contrib.auth.hashers import check_password
import random 


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
            errors="nom d'utilisateur ou mot de passe incorecte"
            return render(request,'Compte/connexion.html',{'errors':errors})
    return render(request,'Compte/connexion.html',{'errors':errors})

def signup(request):
    error=''
    formate='### ## ## ##'
    email_exist=""
    if request.method =='POST':
        username=request.POST.get('username')
        nom=request.POST.get('lastname')
        prenom=request.POST.get('firtname')
        email=request.POST.get('email')
        phone=request.POST.get('phone')
        image=request.FILES.get('image')
        password=request.POST.get('password')
        password2=request.POST.get('password2')
        user_name=Utilisateur.objects.filter(username=username)
        if user_name:
            #  choix=f"{username}{random.randint(1,999)}"
             errors=f"Cet identifiant existe deja voici une option pour vous {username}{random.randint(1,999)} "
             return render(request,'Compte/signup.html',{'errors':errors})
        email_exist=Utilisateur.objects.filter(email=email)
        if email_exist:
            errors=f"un utilisateur avec l'email {email} existe deja"
            return render(request,'Compte/signup.html',{'errors':errors})
        if password != password2:
            errors="vos mots de passes ne sont pas conformes"
            return render(request,'Compte/signup.html',{'errors':errors})
        if len(password)<4:
            errors="le mot de passe doit contenir au moins huit caractères"
            return render(request,'Compte/signup.html',{'errors':errors})
        if len(phone) <9 or len(phone) >9:
            errors =f"mauvais format de telephone le numero {phone} de telephone doit être au format guinneen"
            formate="premier"
            print(phone)
            return render(request,'Compte/signup.html',{'errors':errors,'formate':formate})
        if phone[1] !=str(6) and phone[1] != str(2):
            errors =f"mauvais format de telephone le numero de telephone doit être au format guinneen"
            formate="deuxieme"
            return render(request,'Compte/signup.html',{'errors':errors,'formate':formate})
        token = secrets.token_urlsafe(32)
        user=Utilisateur.objects.create_user(
            username=username,
            email=email,
            password=password,
            image=image,
            first_name=prenom,
            last_name=nom,
            phone=str(phone),
            password2=password2,
            token = token
        )
        # user.save()
        login(request,user)
        return redirect('connexion')
        # return render(request,'account/connexion.html')
    return render(request,'Compte/signup.html')



# @login_required
def deconnexion(request):
    logout(request)
    return redirect('home')

def profil(request):
    user=request.user
    if request.method =='POST':
   
        last_name=request.POST.get('lastname')
        first_name=request.POST.get('firstname')
        email=request.POST.get('email')
        phone=request.POST.get('phone')
        # image=request.FILES.get('image')
        modifie=Utilisateur.objects.update(
            
            last_name=last_name,
            first_name=first_name,
            email=email,
            # image=image,
            phone=phone
            
        )

        return redirect('home')
        
    return render(request,'Compte/profil.html',{"user":user})

def change_password(request):
    errors=''
    user=request.user
    
    if request.method =='POST':
        ancien_password=request.POST.get('password')
        nouveau_password=request.POST.get('nouveau')
        confirme_password=request.POST.get('confirme')
        
            
            
        if not user.check_password(ancien_password):
        
            messages.error(request,'le mot de passe entrer est erroné')
            errors='le mot de passe entrez est erroné'
            return render(request,'Compte/change_mot_de_pass.html',{'errors':errors})
        if nouveau_password !=confirme_password:
            
            messages.error(request,'vot mot de passe ne sont pas conforme')
            errors='vos mot de passe ne sont pas conforme'
            return render(request,'Compte/change_mot_de_pass.html',{'errors':errors})
        user.set_password(nouveau_password)
        user.save()
        login(request,user)
        return redirect('home')

    return render(request,'Compte/change_mot_de_pass.html')

def reset_password(request):
    info =''
    errors = ''
    context = {}
    if request.method == 'POST':
        email = request.POST.get('email')
        user = Utilisateur.objects.filter(email=email)
        if user:
            token = user[0].token
            suject = "recuperation de mot de passe"
            message = f"coucou{user[0].username} ne vous enfaite pas vous n'avez qu'a cliquer sur ce lien pour obtenir un nouveau mot de passe http://localhost:8000/Compte/password/{token}"
            from_email = settings.EMAIL_HOST_USER
            to_email = email
            email = EmailMessage(suject,message,from_email,[to_email])
            email.send()
            info ="un lien vient d'être envoyer sur votre boite mail merci de cliquer sur le lient afin de proceder à la recuperation du mot de passe"
            context={
                'errors':errors,
                'info':info
            }
            return render(request,'Compte/reset_password.html',context)
        else:
            errors =f"desole l'utilisateur avec l'email {email} n'existe pas entrez votre vrai email"
            context={
                'errors':errors,
                'info':info
            }
            return render(request,'Compte/reset_password.html',context)
    return render(request,'Compte/reset_password.html',context)

def modifier_password(request,token):
    info = ''
    errors = ''
    if request.method == 'POST':
        password = request.POST.get('password')
        password2 = request.POST.get('password2')
        if len(password)<4:
            errors = "le mot de passe doit contenir au moins  cinq caractères"
            return render(request,'Compte/password.html',{'errors':errors})
        if password != password2:
            errors = "vos mot de passe sont differents"
            return render(request,'Compte/password.html',{'errors':errors})
        user = Utilisateur.objects.filter(token=token)
        users = user[0]
        users.set_password(password)
        users.save()
        info = "felicitation votre mot de passe à été modifier avec succès connectez vous donc"
        return redirect('connexion')
    return render(request,'Compte/password.html')

        
    




    
    

