from django.shortcuts import render,redirect
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required
from .forms import *
from django.contrib import messages
from django.contrib.auth.models import User
from django.db import IntegrityError

# Create your views here.

def registro(request):
    if request.method =='GET':
        return render(request,'registro.html',{'form': UserRegistrationForm})
    else:
        if request.POST['password1'] == request.POST['password2']:
            try:
                user = User.objects.create_user(request.POST['username'],request.POST['email'], password =request.POST['password1'])
                user.save()
                return redirect('/login')
            except IntegrityError:
                return render (request,'registro.html',{'form': UserCreationForm,'error':'El nombre de usuario ya existe'})
        else:
            return render(request,'registro.html',{'form':UserCreationForm, 'error':'Las contraseñas no coinciden'})
                
                
            
        """user_form = UserRegistrationForm(request.POST)
        if user_form.is_valid:
            user_form.save()
            username = user_form.cleaned_data.get('username') 
            messages.success(request,f'Usuario {username} creado exitosamente')
            return redirect('/registro')
    else:
        user_form = UserRegistrationForm()
    return render(request, 'registro.html',{'user_form':user_form})"""

def user_login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request,user)
            return redirect('/home')
        else:
            messages.error(request,'Nombre de usuario o contraseña no válidos')
    return render(request,'login.html')

@login_required
def user_logout(request):
    logout(request)
    return redirect('login')

"""def recuperar(request):
    return render(request,'recuperarclave.html')"""

def advertencia(request):
    return render(request, 'advertencia.html')

def empresaFormal(request):
    return render(request, 'dueñoEmpresaRegistro.html')

def contratoPer(request):
    return render(request, 'contratoPersonas.html')

def contratoSer(request):
    return render(request, 'contratoServicio.html')

def empresaHabla(request):
    return render(request, 'hablanosEmpresa.html')

def personaRegis(request):
    return render(request, 'personaRegistro.html')

def regisEmpresa(request):
    return render(request, 'registrarEmpresa.html')

def registrarse(request):
    return render(request, 'registrarse.html')

def empresaInformal(request):
    return render(request, 'registroempresainformal.html')

def producto(request):
    return render(request, 'producto.html')

def servicio(request):
    return render(request, 'servicio.html')

def asesor(request):
    return render(request, 'asesor.html')

