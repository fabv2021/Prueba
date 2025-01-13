from django.shortcuts import render

# Create your views here.

def llamada(request):
    return render(request,'softphone_launch.html')

def soft(request):
    return render(request,'softphone.html')
    
def reunion(request):
    return render(request,'reuniones.html')

def moodle(request):
    return render(request,'moodle.html')    

def agenda(request):
    return render(request,'ContactosFinal.html')

def editar_contacto(request):
    return render(request,'Editar.html')

def chat_agenda(request):
    return render(request,'chat.html')
