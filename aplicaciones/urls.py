from django.contrib import admin
from django.urls import path,include
from django.conf import settings
from .views import home, emprendimiento, producto, insumo, marketing, asesoria_contable, emprendedora, cantidad 
 


urlpatterns = [
    path('', home, name = 'home'),
    path('emprendimiento/', emprendimiento, name = 'emprendimiento'),
    path('producto/', producto, name = 'producto'),
    path('insumo/', insumo, name = 'insumo'),
    path('marketing/', marketing, name = 'producto'),
    path('asesoria_contable/', asesoria_contable, name = 'asesoria_contable'),
    path('emprendedora/', emprendedora, name = 'emprendedora'),
    path('cantidad/', cantidad, name = 'cantidad'),
    path('accounts/',include('django.contrib.auth.urls')),
    
    
    
]