from django.shortcuts import render
from django.contrib import messages


# Create your views here.
def mercado(request):
    return render(request,'marketmp.html')

def products(request):
    return render(request,'marketproducts.html')

def services(request):
    return render(request,'marketservices.html')

def cooperative(request):
    return render(request,'marketcoop.html')

            