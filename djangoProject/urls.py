"""djangoProject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, re_path
from . import views
from django.conf.urls import include



urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home_page, name="home_page"),
    path('repertuar/', views.repertuar, name = "repertuar"),
    path('cennik/', views.cennik, name = "cennik"),
    path('about/', views.about, name = "about"),
    path('kontakt/', views.kontakt, name = "kontakt"),
    path('registration/', views.rejestracja, name="rejestracja"),
    path('registration/registered/', views.zarejestrowany, name="registered"),
    re_path(r'^repertuar/rezerwacja$', views.rezerwacja, name = "rezerwacja"),
    path('repertuar/zarezerwowano', views.zarezerwowano, name="zarezerwowano"),
    path('registered/', views.finalZarejestrowany, name="finalZarejestrowany"),
    path('konto/', views.konto, name="konto"),
    path('zmien', views.zmien, name="zmien")
]

#handler404 = 'views.handler404'

#Add Django site authentication urls (for login, logout, password management)

urlpatterns += [
    path('accounts/', include('django.contrib.auth.urls')),
    path('accounts/login',views.logowanie, name = "logowanie" ),
    path('accounts/logout', views.wylogowany, name = "wylogowanie")
]