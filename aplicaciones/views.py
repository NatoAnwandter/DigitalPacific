from django.shortcuts import render
from django.http import HttpResponse
from .forms import Perfil_emprendedoraForm

def home(request): 
    return render(request,'home.html')

def emprendimiento(request):
    return render(request,'app/emprendimiento/agregar_emprendimiento.html')

def producto(request):
    return render(request,'app/emprendimiento/producto/agregar_producto.html')


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
        else:
            data["mensaje"] = formulario

    return render(request,'app/emprendedora/agregar_emprendedora.html', data)