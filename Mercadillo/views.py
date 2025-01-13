from django.shortcuts import render

# Create your views here.

def mercadillo(request):
    return render(request,'mercadillo.html')

def onevalue(request):
    return render(request,'mercadillouno.html')

def all_free(request):
    return render(request,'mercadillozero.html')