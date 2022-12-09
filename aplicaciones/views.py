from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.shortcuts import redirect
from .forms import Perfil_emprendedoraForm ,EmprendimientoForm ,ProductoForm, InsumoForm, CantidadForm, UsuarioForm
from .models import Emprendimiento ,Producto, Insumo, Cantidad, Perfil_emprendedora, User, Industria, Sala_chat, Message_chat
from django.contrib import messages
from django.contrib.auth import authenticate, login
from urllib import request
from django.db.models import Count, Sum, Subquery
from django.contrib.auth.decorators import login_required
from .DBHelperChat import DBHelper
from django.shortcuts import get_object_or_404
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

        return render(request,'admin/2_analisis/analisis.html')
    else:
        return render(request,'admin/access_denied.html')




# --------------------------------------------REPORTES-------------------------------------------------------------------------

def reporte_geografico(request):
    
    if request.user.is_staff:
        emprendedoras = Perfil_emprendedora.objects.all()
        emprendedora_count = Perfil_emprendedora.objects.values("comuna").annotate(Count("comuna"))
        # comuna1 = Perfil_emprendedora.objects.values("comuna")
        
        emprendimientos = Emprendimiento.objects.all()
        emprendimiento_count= Emprendimiento.objects.values("comuna").annotate(Count("comuna"))

        

        emprendimiento_com = Emprendimiento.objects.values("id_emprendimiento","comuna")       
        
        

        tab3 = set()

        for e in Producto.objects.filter(id_emprendimiento_id=1).select_related('id_emprendimiento'):
            tab3.add(e.nombre)

        emp1 = Producto.objects.all().select_related('id_emprendimiento')
        emp2 = Insumo.objects.all().select_related('id_emprendimiento')
        
#  ---------------------------------CREACION DE UN DICCIONARIO A PARTIR DE UN JOIN DE TABLAS------------------------------------------
        
        c = 0  
        productosCount = {}      
        for u in emp1:
            c += 1            
            if u.id_emprendimiento.comuna in productosCount:

                productosCount[u.id_emprendimiento.comuna]+=1
            else:
                productosCount[u.id_emprendimiento.comuna]=1
                
        print(productosCount)        
#  ---------------------------------CREACION DE UN DICCIONARIO A PARTIR DE UN JOIN DE TABLAS------------------------------------------
        r = 0
        insumosCount ={}
        for l in emp2:
            r += 1

            if l.id_emprendimiento.comuna in insumosCount:

                insumosCount[l.id_emprendimiento.comuna]+=1
            else:
                insumosCount[l.id_emprendimiento.comuna]=1
        print(insumosCount)

        data = {
            'emprendedora_count': emprendedora_count,
            'emprendimiento_count': emprendimiento_count,
            'emprendimiento_com' : emprendimiento_com,            
            'productosCount': productosCount, 
            'insumosCount': insumosCount
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

# --------------------------------------------Chat------------------------------------------------------------------------
#funcion para ver una lista de los usuarios con lo que puedes hablar
def chat(request): 
    #traigo funcion creada en dbhelper.py
    db = DBHelper()
    #Traigo todas las room que tiene el uario logiado
    rooms  = Sala_chat.objects.filter(users = request.user.id)
    #Creo un diccionario vacio
    dicc_users = {}
    #Recorro las rooms
    for r in rooms:
        #Inicializo la consulta select__user
        ff = db.select_user(r.name, request.user.username)
        #Recorro los registro de la consulta
        for f in ff:
            #Guardo en el diccionario como keys las id de las rooms y guardo como value el nombre los usuarios con lo que de deseo hablar
            dicc_users[f[0]] = f[1]

    #Guardo las keys
    clave_users = dicc_users.keys()
    #Guardo los valores
    valor_users = dicc_users.values()
    #Guardo la cantidad de registros
    cantidad_users = dicc_users.items()

    data = {
        "rooms": rooms,
        "clave_users":clave_users,
        "valor_users":valor_users,
        "cantidad_users":cantidad_users,
    } 
    
    return render(request,'chat/mi_chat.html', data)
   

#Sala que contiene los mensajes de un chat
@login_required
def room(request, room):
    username = request.GET.get('username')
    #Traigo la sala en la cual su nombre sea igual al parametro room
    room_details = get_object_or_404(Sala_chat, name=room)
    #room_details = Room.objects.get(name=room)
    
    data = {
        'username': username,
        'room':room,
        'room_details': room_details,

    }

    return render(request, 'chat/room.html',data)
    


#Funcion para entrar a un chat especifico
def entrar_chat(request, room):
        #Nombre del usuario logiado
        username = request.user.username
        return redirect('/'+room+'/?username='+username)
            

#Funcion para enviar mensajes
def send(request):
    #Entro los campos por formulario
    message = request.POST['message']      
    username = request.POST['username']    
    room_id = request.POST['room_id']      
    #Creo un mensaje
    new_message = Message_chat.objects.create(value=message, user=username, room=room_id)
    #Guardo el mensaje
    new_message.save()
    return HttpResponse('Message send Successfully')


#Funcion para mostar los mensajes 
def getMessages(request, room):
    print("Estoy en getMessages")
    #Traigo el Room que tiene el mismo nombre que el parametro room
    room_details = Sala_chat.objects.get(name = room)
    #Traigo los mensajes filtrando por el room
    messages = Message_chat.objects.filter(room = room_details.id)
    print("los mensajes son:", messages)
    #Retorno un archivo JSON con los mensajes
    return JsonResponse({"messages":list(messages.values())})
