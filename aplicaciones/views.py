from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import redirect
from .forms import Perfil_emprendedoraForm ,EmprendimientoForm ,ProductoForm, InsumoForm, CantidadForm, UsuarioForm
from .models import Emprendimiento ,Producto, Insumo, Cantidad, Perfil_emprendedora
from django.contrib import messages
from django.contrib.auth import authenticate, login
from urllib import request


def home(request): 
    return render(request,'home.html')

def emprendimiento(request):
    if request.user.is_authenticated:

        # emprendimiento = Emprendimiento.objects.filter(usuario=request.user)
        emprendimientos = Emprendimiento.objects.all()
        data = {
            'form':EmprendimientoForm(),
            'emprendimientos': emprendimientos, #admin
            'emprendimiento': emprendimiento    #user
        }

        if request.method == 'POST':
            formulario = EmprendimientoForm(data=request.POST)
            if formulario.is_valid():
                formulario.save()           

                messages.success(request, "#")
                # data["mensaje"] = "emprendimiento guardado"          
            else:
                data["mensaje"] = formulario

        return render(request,'app/emprendimiento/agregar_emprendimiento.html', data)
    else:
        return render(request,'app/emprendimiento/agregar_emprendimiento.html')


def producto(request):
    productos = Producto.objects.all()

    data = {
        'form':ProductoForm(),
        'productos': productos
    }

    if request.method == 'POST':
        formulario = ProductoForm(data=request.POST)
        if formulario.is_valid():
            formulario.save()

            messages.success(request, "#")
            # data["mensaje"] = "producto guardado"          
        else:
            data["mensaje"] = formulario

    return render(request,'app/emprendimiento/producto/agregar_producto.html', data)


def insumo(request):
    insumos = Insumo.objects.all()

    data = {
        'form':InsumoForm(),
        'insumos': insumos
    }

    if request.method == 'POST':
        formulario = InsumoForm(data=request.POST)
        if formulario.is_valid():
            formulario.save()
            data["mensaje"] = "insumo guardado"          
        else:
            data["mensaje"] = formulario

    return render(request,'app/emprendimiento/producto/insumo/agregar_insumo.html',data)


def marketing(request):
    return render(request,'app/emprendimiento/marketing/marketing.html')


def asesoria_contable(request):
    return render(request,'app/emprendimiento/asesoria_contable/asesoria_contable.html')




# ****************------------FORMS Emprendedora------------*******************

def emprendedora(request):
    
    data = {
        'form': Perfil_emprendedoraForm(), 
        'emprendedoras': emprendedoras
        
    }

    if request.method == 'POST':
        formulario = Perfil_emprendedoraForm(data=request.POST)
        if formulario.is_valid():
            formulario.save()
            
            # messages.success(request, "Felicitaciones")
            data["mensaje"] = "perfil_emprendedora guardado"
            # aca poner funcion redirect to emprendimiento    --------------------------------
            return redirect(to='emprendimiento')
            
        else:
            data["mensaje"] = formulario

    return render(request,'app/emprendedora/agregar_emprendedora.html', data)


def cantidad(request):
    cantidads = Cantidad.objects.all()

    data = {
        'form':CantidadForm(),
        'cantidads': cantidads
    }

    if request.method == 'POST':
        formulario = CantidadForm(data=request.POST)
        if formulario.is_valid():
            formulario.save()

            messages.success(request, "#")         
        else:
            data["mensaje"] = formulario

    return render(request,'app/emprendimiento/producto/insumo/cantidad/agregar_cantidad.html',data)
# --------------------------------------------------------------------------------------------------------------------------------------------
def registro(request):
    data = {
        'form': UsuarioForm()   
    }
    if request.method == 'POST':
        formulario = UsuarioForm(data=request.POST)
        if formulario.is_valid():
            formulario.save()
            #crea un usuario autenticado
            user =authenticate(username=formulario.cleaned_data["username"], password=formulario.cleaned_data["password"])
            #loguea al usuario
            login(request,  user)
            # messages.success(request, "creado correctamente!")
            data["mensaje"] = "creado correctamente!"
            #redirigir al home
            if user.is_staff():
                return redirect(to="adminhome")
            if user.is_active():
                return redirect(to="home")
        data["form"] = formulario
    return render(request, 'registration/registro.html', data)

# --------------------------------------------------------------------------------------------------------------------------------------------

def adminhome(request): 
    emprendedoras = Perfil_emprendedora.objects.all()
    data = {
        'emprendedoras': emprendedoras
    }
    return render(request,'admin/adminhome.html', data)

def t_emprendimiento(request): 
    return render(request,'admin/emprendimiento/tabla_emprendimientos.html')

def t_emprendedora(request): 
    return render(request,'admin/emprendedora/tabla_emprendedoras.html')

def t_producto(request): 
    return render(request,'admin/producto/tabla_productos.html')

def t_insumo(request): 
    return render(request,'admin/insumo/tabla_insumos.html')




