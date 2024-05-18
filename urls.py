"""system URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import to include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from system_mag import views

urlpatterns = [
    path('', views.startowa, name='strona_startowa'),
    path('lista_produktow/', views.lista_produktow, name='lista_produktow'),
    path('dodaj_produkt/', views.dodaj_produkt, name='dodaj_produkt'),
    path('aktualizuj_produkt/<str:pk>/', views.aktualizuj_produkt, name='aktualizuj_produkt'),
    path('usun_produkt/<str:pk>/', views.usun_produkt, name='usun_produkt'),
    path('admin/', admin.site.urls),
]