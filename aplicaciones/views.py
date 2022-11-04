from django.shortcuts import render
from django.http import HttpResponse

def home(request): 
    return render(request,'app/home.html')

def emprendimiento(request):
    return render(request,'app/emprendimiento/emprendimiento.html')

def producto(request):
    return render(request,'app/emprendimiento/producto/producto.html')


def insumo(request):
    return render(request,'app/emprendimiento/producto/insumo/insumo.html')


def marketing(request):
    return render(request,'app/emprendimiento/marketing/marketing.html')


def asesoria_contable(request):
    return render(request,'app/emprendimiento/asesoria_contable/asesoria_contable.html')