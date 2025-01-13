"""
URL configuration for NETGOcios project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
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
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from Buscador.views import *
from Login.views import *
from Marketplace.views import *
from Mercadillo.views import *
from Economicos.views import *
from Llamada.views import *
from Tutoriales.views import *
from django.shortcuts import redirect
from django.urls import path

def home_redirect(request):
    return redirect('http://127.0.0.1/NuevoInicio/public/')




urlpatterns = [
    path('admin/', admin.site.urls),
    path('',user_login,name='login'),
    path('home/', home_redirect, name='home'),
    path('resultados/',resultados, name='resultados'),
    path('buscador/',buscar, name='buscador'),
    path('registro/',registro, name='registro'),
    path('login/', user_login, name='login'),
    path('logout/',user_logout, name='logout'),
    path('advertencia/',advertencia,name='advertencia'),
    path('marketplace/', mercado, name='marketplace'),
    path('productos/',products, name='productos'),
    path('servicios/',services, name='servicios'),
    path('cooperativo/',cooperative, name='cooperativo'),
    path('mercadillo/', mercadillo, name='mercadillo'),
    path('rebaja/', onevalue, name='rebaja'),
    path('gratis/', all_free,name='gratis'),
    path('llamada/',llamada, name='llamada'),
    path('reunion/',reunion, name='reunion'),  #Cambiar path archivo - softphone_launcher
    path('soft/',soft, name='soft'),
    path('economico',grafico,name='economico'),
    path('agenda/',agenda,name='agenda'),
    path('editar/',editar_contacto, name='editar'),
    path('chat/',chat_agenda,name='chat'),
    path('moodle/',moodle,name='moodle'),
    path('contratoPer/',contratoPer,name='contratoPer'),
    path('contratoSer/',contratoSer,name='contratoSer'),
    path('registrarEmpresa/',regisEmpresa,name='registrarEmpresa'),
    path('empresaInformal/',empresaInformal,name='empresaInformal'),
    path('empresaHabla/',empresaHabla,name='empresaHabla'),
    path('registrarse/',registrarse,name='registrarse'),
    path('personaRegis/',personaRegis,name='personaRegis'),
    path('producto/',producto,name='producto'),
    path('empresaFormal/',empresaFormal,name='empresaFormal'),
    path('configuracion/',configuracion,name='configuracion'),
    path('servicio/',servicio,name='servicio'),
    path('tutoriales/',tutoriales,name='tutoriales'),
    path('asesor/',asesor,name='asesor'),
       
] + static(settings.STATIC_URL,document_root=settings.STATIC_ROOT)
