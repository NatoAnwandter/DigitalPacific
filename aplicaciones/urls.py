from django.contrib import admin
from django.urls import path,include
from django.conf import settings
# from .views import home, emprendimiento, producto, insumo, marketing, asesoria_contable, emprendedora, cantidad, registro 
from .views import *


urlpatterns = [
    path('', home, name = 'home'),
    path('emprendimiento/', emprendimiento, name = 'emprendimiento'),
    path('producto/', producto, name = 'producto'),
    path('insumo/', insumo, name = 'insumo'),
    path('marketing/', marketing, name = 'producto'),
    path('asesoria_contable/', asesoria_contable, name = 'asesoria_contable'),
    path('cantidad/', cantidad, name = 'cantidad'),
    path('accounts/',include('django.contrib.auth.urls')),
    path('registro/', registro, name = 'registro'),
# -----------------------------ADMIN--------------------------------        
    path('access_denied/', access_denied, name = 'access_denied'),
    path('agregar_emprendedora/', agregar_emprendedora, name = 'agregar_emprendedora'),
    path('t_emprendimiento/', t_emprendimiento, name = 't_emprendimiento'),
    path('t_producto/', t_producto, name = 't_producto'),
    path('t_insumo/', t_insumo, name = 't_insumo'),

    path('reporte/', reporte, name = 'reporte'),
    path('reporte_geografico/', reporte_geografico, name = 'reporte_geografico'),
    path('reporte_asesoria/', reporte_asesoria, name = 'reporte_asesoria'),
    path('reporte_industria/', reporte_industria, name = 'reporte_industria'),

    path('analisis/', analisis, name = 'analisis'),
    
    
    #---------------------------- chat -------------------------------------------------
    #tempalte principal de chats
    path('chat/', chat, name = 'chat'),
    #template de un chat en especifico
    path('<str:room>/', room, name='room'),
    #redirecciona aun chat con los parametros especificados
    path('entrar_chat/<room>', entrar_chat, name ='entrar_chat'),
    #Enviar mensaje
    path('send', send, name='send'),
    #mostrar mensajes
    path('getMessages/<str:room>/', getMessages, name='getMessages'),

]