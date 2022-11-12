from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import redirect
from .forms import Perfil_emprendedoraForm ,EmprendimientoForm ,ProductoForm
from .models import Emprendimiento ,Producto



def home(request): 
    return render(request,'home.html')

def emprendimiento(request):
    # registros = Perfil_emprendedora.objects.filter(usuario=request.user)
    emprendimientos = Emprendimiento.objects.all()
    
    data = {
        'form':EmprendimientoForm(),
        'emprendimientos': emprendimientos
    }

    if request.method == 'POST':
        formulario = EmprendimientoForm(data=request.POST)
        if formulario.is_valid():
            formulario.save()
            data["mensaje"] = "emprendimiento guardado"          
        else:
            data["mensaje"] = formulario

    return render(request,'app/emprendimiento/agregar_emprendimiento.html', data)


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
            data["mensaje"] = "producto guardado"          
        else:
            data["mensaje"] = formulario

    return render(request,'app/emprendimiento/producto/agregar_producto.html', data)


def insumo(request):
    return render(request,'app/emprendimiento/producto/insumo/agregar_insumo.html')


def marketing(request):
    return render(request,'app/emprendimiento/marketing/marketing.html')


def asesoria_contable(request):
    return render(request,'app/emprendimiento/asesoria_contable/asesoria_contable.html')




# ****************------------FORMS------------*******************

def emprendedora(request):
    data = {
        'form': Perfil_emprendedoraForm()
    }

    if request.method == 'POST':
        formulario = Perfil_emprendedoraForm(data=request.POST)
        if formulario.is_valid():
            formulario.save()
            
            data["mensaje"] = "perfil_emprendedora guardado"
            # aca poner funcion redirect to emprendimiento    --------------------------------
            return redirect(to='emprendimiento')
            
        else:
            data["mensaje"] = formulario

    return render(request,'app/emprendedora/agregar_emprendedora.html', data)