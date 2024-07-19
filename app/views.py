from pyexpat.errors import messages
from django.shortcuts import render, redirect, get_object_or_404
from .forms import ContactoForm, TiendaForm, CustomUserCteationForm
from django.contrib.auth import authenticate, login

# Create your views here.
def base(request):
    return render(request, 'app/base.html')

def inicio(request):
    return render(request, 'app/tienda.html')

def carrito(request):
    return render(request, 'app/carrito.html')

def contacto(request):
    data = {
        'form': ContactoForm()
    }

    if request.method == 'POST':
        
        formulario = ContactoForm(data= request.POST)
        if formulario.is_valid():
            formulario.save()
            data["mensaje"] = "contacto guardado"
        else:
            data["form"] = formulario
    
    return render(request, 'app/contacto.html', data)

def home(request):
    return render(request, 'app/home.html')

def login(request):
    return render(request, 'app/login.html')

def quienessomos(request):
    return render(request, 'app/quienes-somos.html')

def registro(request):
    data = {
        'form': CustomUserCteationForm()
    }
    if request.method == 'POST':
        formulario = CustomUserCteationForm(data=request.POST)
        if formulario.is_valid():
            formulario.save()
            user = authenticate(username = formulario.cleaned_data["username"], password =formulario.cleaned_data["password1"])
            login(request, user)
            messages.success(request, "Te has registrado")
            return redirect(to="home")
        data['form'] = formulario

    return render(request, 'registration/registro.html', data)


def agregar_producto(request):

    data ={
        'form': TiendaForm()
    }
    if request.method == 'POST':
        formulario = TiendaForm(data=request.POST, files=request.FILES)
        if formulario.is_valid():
            formulario.save()
            data["mensaje"] = "guardado correctamente" 
        else:
         data["form"] = formulario

    return render(request, 'app/producto/agregar.html', data)

def listar_producto(request):
    producto = producto.objects.all()

    data = { 
        'tienda': inicio 
    }
    return render(request, 'app/producto/listar.html', data)


def modificar_producto(request , id):
   tienda = get_object_or_404(tienda, id=id) 

   data = {
       'form': TiendaForm(instance=tienda) 
   }
   if  request.method == 'POST':
        formulario = TiendaForm(data=request.POST, instance=tienda, files=request.FILES)
        if formulario.is_valid():
            formulario.save()
            return redirect(to="listar_producto")
        data["form"] = formulario
        
        return render(request, 'app/producto/modificar.html') 
   
def  eliminar_producto(request, id):
    producto =  get_object_or_404(producto, id=id)
    producto.delete()
    return redirect(to="listar_producto")
    