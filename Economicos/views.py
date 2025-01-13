from django.shortcuts import render
from django.contrib import messages
import plotly.express as px
from Economicos.models import *
from Economicos.forms import *

# Create your views here.

def grafico(request):
    datos = Economicos.objects.all()
    buscar = request.GET.get('producto')
    start = request.GET.get('comienzo')
    end = request.GET.get('termino')
    
    chart = None
    producto = None
    pais = None
    ciudad = None
    precio_bajo = None
    precio_alto = None
    precio_promedio = None
    
    if request.GET:
        if not buscar or not start or not end:
            messages.warning(request,"Indique los parámetros para realizar la búqueda")
        else:
            if buscar:
                datos = datos.filter(productos__istartswith = buscar)
            if start:
                datos = datos.filter(fecha__gte = start)
            if end:
                datos = datos.filter(fecha__lte = end)
    
            fig = px.line(
                x=[d.fecha for d in datos],
                y=[d.precios for d in datos],
                title= "Stock Market",
                labels={'x':'Date','y':'Value'},
            )
        
            fig.update_layout(
                title ={
                    'font_size':22,
                    'xanchor':'center',
                    'x': 0.5
                }
            )
            chart = fig.to_html()
        
            if datos.exists():
                precio_bajo = datos.order_by('precios').first().precios
                precio_alto = datos.order_by('-precios').first().precios
                precio_promedio = datos.first().promedio
                producto = datos.first().productos
                pais = datos.first().pais
                ciudad = datos.first().ciudades
    
       
    
    context = {
        'chart': chart,
        'form': FechasForm(),
        'precio_bajo': precio_bajo,
        'precio_alto' : precio_alto,
        'precio_promedio' : precio_promedio,
        'producto' : producto,
        'pais' : pais,
        'ciudad' : ciudad,
        'buscar' : buscar
        }
    
    return render(request,'economico.html',context)
    
