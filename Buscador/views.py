from django.shortcuts import render
from django.db.models import Q
from .models import *


# Create your views here.

def home(request):
    return render(request,'home.html')


def buscar (request): 
   
    
    if request.method == 'POST':
       
        nombre = request.POST.get('noem')
        giro = request.POST.get('rubro')
        producto = request.POST.get('prod')
        servicio = request.POST.get('serv')
        descripcion = request.POST.get('descr')
       
        pais = request.POST.get('pais')
        estado = request.POST.get('est')
        region = request.POST.get('reg')
        comuna = request.POST.get('ciud')
        ciudad = request.POST.get('ciud')

        empresa = Empresas.objects.all()
        
        if nombre:
            empresa = empresa.filter(empresa__istartswith = nombre).distinct().values()
        elif descripcion:
            empresa = empresa.filter(actividad__istartswith = descripcion).distinct()
        elif giro:
            empresa = empresa.filter(rubro__istartswith = giro).distinct()
        elif producto:
            empresa = empresa.filter(actividad__istartswith = producto).distinct()
        elif servicio:
            empresa = empresa.filter(actividad__istartswith = servicio).distinct()
        elif comuna:
            empresa = empresa.filter(Q(ciudad__istartswith = ciudad)|Q(comuna__istartswith = comuna)).values()
        elif pais:
            empresa = empresa.filter(Q(pais__exact = "usa")&Q(estado__exact = estado)| Q(pais__exact = "chile")&Q(region__exact = region)).values()
        
        context ={
            'empresa':empresa,
            }
           
        return render(request,'resultados.html',context)
    return render(request,'buscador.html')

def resultados(request):
    return render(request,'resultados.html')

def configuracion(request):
    return render(request,'config.html')


