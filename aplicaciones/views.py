from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import redirect
from .forms import Perfil_emprendedoraForm ,EmprendimientoForm ,ProductoForm, InsumoForm, CantidadForm, UsuarioForm
from .models import Emprendimiento ,Producto, Insumo, Cantidad, Perfil_emprendedora, User
from django.contrib import messages
from django.contrib.auth import authenticate, login
from urllib import request
# from user.models import Usuario


def home(request): 
    emprendedoras = Perfil_emprendedora.objects.all()
    
    data = {
        'emprendedoras': emprendedoras 
    }

    return render(request,'home.html', data)

def emprendimiento(request):
    if request.user.is_authenticated:
        emprendimientos = Emprendimiento.objects.all()
        emprendedora = Perfil_emprendedora.objects.values_list("id_perfil_emprendedora").filter(id_user=request.user.id)

        emprendimiento = Emprendimiento.objects.filter(id_perfil_emprendedora_id = emprendedora[0])

        print("este es el emprendedora:",emprendedora[0])
        print("este es el user.id:",request.user.id)


        data = {
            'form':EmprendimientoForm(),
            'emprendimientos': emprendimientos, #admin
            'emprendimiento': emprendimiento    #user
        }

        if request.method == 'POST':
            formulario = EmprendimientoForm(data=request.POST)
            if formulario.is_valid():
                post = formulario.save(commit=False)                                
                post.id_perfil_emprendedora_id = emprendedora
                post.id_comuna_id = request.POST["id_comuna"]
                post.id_industria_id = request.POST["id_industria"]                
                post.nombre = request.POST["nombre"]
                post.email = request.POST["email"]
                post.website = request.POST["website"]
                post.id_marketing_id = request.POST["id_marketing"]
                post.id_asesoria_contable_id = request.POST["id_asesoria_contable"]
                formulario.save()           

                messages.success(request, "#")
                # data["mensaje"] = "emprendimiento guardado"          
            else:
                data["mensaje"] = formulario

        return render(request,'app/emprendimiento/agregar_emprendimiento.html', data)
    else:
        return render(request,'app/emprendimiento/agregar_emprendimiento.html')


def producto(request):
    if request.user.is_authenticated:

        productos = Producto.objects.all()
        producto = Producto.objects.filter(id_user=request.user.id)
        print(producto)

        data = {
            'form':ProductoForm(),
            'productos': productos,
            'producto': producto
        }

        if request.method == 'POST':
            formulario = ProductoForm(data=request.POST)
            if formulario.is_valid():
                
                post = formulario.save(commit=False)                                
                post.id_emprendimiento_id = request.POST["id_emprendimiento"]                
                post.nombre = request.POST["nombre"]
                post.id_despacho_id = request.POST["id_despacho"]
                post.id_user_id = request.user.id
                formulario.save()

                messages.success(request, "#")
                # data["mensaje"] = "producto guardado"          
            else:
                data["mensaje"] = formulario

        return render(request,'app/emprendimiento/producto/agregar_producto.html', data)
    else:    
        return render(request,'app/emprendimiento/producto/agregar_producto.html')


def insumo(request):
    if request.user.is_authenticated:

        insumos = Insumo.objects.all()
        insumo = Insumo.objects.filter(id_user=request.user.id)
        print(insumo)

        data = {
            'form':InsumoForm(),
            # 'registros':registros,
            'insumos': insumos,
            'insumo': insumo
        }

        if request.method == 'POST':
            formulario = InsumoForm(data=request.POST)
            if formulario.is_valid():
                post = formulario.save(commit=False)
                post.nombre = request.POST["nombre"]                
                post.id_producto_id = request.POST["id_producto"]
                post.id_cantidad_id = request.POST["id_cantidad"]
                post.id_frecuencia_id = request.POST["id_frecuencia"]
                post.id_user_id = request.user.id
                formulario.save()
                data["mensaje"] = "insumo guardado"          
            else:
                data["mensaje"] = formulario

        return render(request,'app/emprendimiento/producto/insumo/agregar_insumo.html',data)
    else:    
        return render(request,'app/emprendimiento/producto/insumo/agregar_insumo.html')


def marketing(request):
    return render(request,'app/emprendimiento/marketing/marketing.html')


def asesoria_contable(request):
    return render(request,'app/emprendimiento/asesoria_contable/asesoria_contable.html')




# ****************------------FORMS Emprendedora------------*******************

def agregar_emprendedora(request):
    emprendedoras = Perfil_emprendedora.objects.all()

    data = {
        'form':Perfil_emprendedoraForm(),
        'emprendedoras': emprendedoras
    }
    print(emprendedoras)

    if request.method == 'POST':
        formulario = Perfil_emprendedoraForm(data=request.POST)
        if formulario.is_valid():
            formulario.save()
        
            messages.success(request, "Felicitaciones")
            # data["mensaje"] = "perfil_emprendedora guardado" 
            #return redirect(to='emprendimiento')       
        else:
            data["mensaje"] = formulario

    # return render(request,'',data)
    return render(request,'admin/emprendedora/agregar_emprendedora.html',data)

# -------------------------------------------------------------------------------    


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
        data["form"] = formulario
    return render(request, 'registration/registro.html', data)

# --------------------------------------------------------------------------------------------------------------------------------------------

def access_denied(request): 

    return render(request,'admin/access_denied.html')
    

def t_emprendimiento(request): 
    if request.user.is_staff:
        emprendimientos = Emprendimiento.objects.all()
            
        data = {
            'emprendimientos': emprendimientos 
        }

        return render(request,'admin/emprendimiento/tabla_emprendimientos.html', data)
    else:
        return render(request,'admin/access_denied.html')

def t_producto(request): 
    if request.user.is_staff:
        productos = Producto.objects.all()
            
        data = {
            'productos': productos 
        }

        return render(request,'admin/producto/tabla_productos.html', data)
    else:
        return render(request,'admin/access_denied.html')

def t_insumo(request): 
    if request.user.is_staff:
        insumos = Insumo.objects.all()
            
        data = {
            'insumos': insumos 
        }

        return render(request,'admin/insumo/tabla_insumos.html', data)
    else:
        return render(request,'admin/access_denied.html')
    




