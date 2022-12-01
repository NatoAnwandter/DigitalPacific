from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import redirect
from .forms import Perfil_emprendedoraForm ,EmprendimientoForm ,ProductoForm, InsumoForm, CantidadForm, UsuarioForm
from .models import Emprendimiento ,Producto, Insumo, Cantidad, Perfil_emprendedora, User, Industria
from django.contrib import messages
from django.contrib.auth import authenticate, login
from urllib import request
from django.db.models import Count, Sum
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
                post.id_industria_id = request.POST["id_industria"]                
                post.nombre = request.POST["nombre"]
                post.email = request.POST["email"]
                post.website = request.POST["website"]
                post.comuna = request.POST["comuna"]
                post.provincia = request.POST["provincia"]
                post.region = request.POST["region"]
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
        ins_producto = Insumo.objects.values_list()
        emprendimiento = Producto.objects.values_list("id_emprendimiento_id", flat=True).filter(id_user=request.user.id)
        print("emprendimiento: ",emprendimiento)
        print("insumo, prod'_id: ",ins_producto)
        # print("insumo,productoid: ", emprendimiento[0])

        data = {
            'form':InsumoForm(),
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
                post.id_emprendimiento_id = request.POST["id_emprendimiento"]
                # post.id_emprendimiento_id = emprendimiento
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

    
# --------------------------------------METRICAS MENU-----------------------------------------------
def reporte(request): 
    if request.user.is_staff:
        emprendimientos = Emprendimiento.objects.all()
        
            
        data = {
            'emprendimientos': emprendimientos            
        }

        return render(request,'admin/1_reporte_menu/reporte.html', data)
    else:
        return render(request,'admin/access_denied.html')


def analisis(request): 
    if request.user.is_staff:
        emprendimientos = Emprendimiento.objects.all()
            
        data = {
            'emprendimientos': emprendimientos 
        }

        return render(request,'admin/analisis/analisis.html', data)
    else:
        return render(request,'admin/access_denied.html')


def otros(request): 
    if request.user.is_staff:
        
        emprendimientos = Emprendimiento.objects.all()

        

        return render(request,'admin/otros/otros.html', data)
    else:
        return render(request,'admin/access_denied.html')





# --------------------------------------------REPORTES-------------------------------------------------------------------------

def reporte_geografico(request):
    
    if request.user.is_staff:
        emprendedoras = Perfil_emprendedora.objects.all()
        emprendedora_count = Perfil_emprendedora.objects.values("comuna").annotate(Count("comuna"))
        comuna1 = Perfil_emprendedora.objects.values("comuna")
        
        emprendimientos = Emprendimiento.objects.all()
        emprendimiento_count= Emprendimiento.objects.values("comuna").annotate(Count("comuna"))
        
        
        productos = Producto.objects.all()
        
        cant_productoXemprendimiento= Producto.objects.values("id_emprendimiento_id").annotate(cant_prod=Count("nombre"))
        emprendimiento_com = Emprendimiento.objects.values("id_emprendimiento","comuna")        
        cant_insumoXemprendimiento= Insumo.objects.values("id_emprendimiento_id").annotate(cant_insum=Count("nombre"))
        
        

        data = {            
            'emprendedoras': emprendedoras,            
            'comuna1': comuna1,            
            'emprendedora_count': emprendedora_count,

            'emprendimientos' : emprendimientos,
            'emprendimiento_count': emprendimiento_count,


            'productos' : productos,
            'cant_productoXemprendimiento' : cant_productoXemprendimiento,
            'emprendimiento_com' : emprendimiento_com,
            'cant_insumoXemprendimiento' : cant_insumoXemprendimiento
        }

        return render(request,'admin/1_reporte_menu/r_geografico/r_geografico.html', data)
    else:
        return render(request,'admin/1_reporte_menu/r_geografico/r_geografico.html')


def reporte_asesoria(request):
    if request.user.is_staff:
        marketing_sis = Emprendimiento.objects.values("id_marketing")
        marketing_si = Emprendimiento.objects.values("id_marketing_id").filter(id_marketing_id=1).count()
        marketing_no = Emprendimiento.objects.values("id_marketing_id").filter(id_marketing_id=2).count()
        marketing_ns = Emprendimiento.objects.values("id_marketing_id").filter(id_marketing_id=3).count()
        contable_si = Emprendimiento.objects.values("id_asesoria_contable_id").filter(id_asesoria_contable_id=1).count()
        contable_no = Emprendimiento.objects.values("id_asesoria_contable_id").filter(id_asesoria_contable_id=2).count()
        
        print("mark_ns: ",marketing_ns)
        data = {
            'marketing_si': marketing_si,
            'marketing_no': marketing_no,
            'marketing_ns': marketing_ns,
            'contable_si': contable_si,
            'contable_no': contable_no,
            
        }
        return render(request,'admin/1_reporte_menu/r_asesoria/r_asesoria.html', data)
    else:
        return render(request, 'admin/access_denied.html')

def reporte_industria(request):
    if request.user.is_staff:      
        emprendimiento = Emprendimiento.objects.all()
        industria = Industria.objects.all()
        emprendimiento2_count = Emprendimiento.objects.values("id_industria_id").annotate(cantidad=Count("id_industria_id"))
        
        data = {
            'emprendimiento' : emprendimiento, 
            'emprendimiento2_count' : emprendimiento2_count,
            'industria' : industria 
        }
        return render(request,'admin/1_reporte_menu/r_industria/r_industria.html',data)
    else:
        return render(request, 'admin/access_denied.html')