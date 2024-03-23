
from django.contrib import admin
from django.urls import path,include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include('gestionproduits.url')),
    path('Compte/',include('Compte.url')),
    path('accounts/', include('allauth.urls')),
    path('app_admin/',include('app_admin.url')),
    
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
