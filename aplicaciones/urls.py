from django.urls import path
from .views import home, emprendimiento, producto, insumo, marketing, asesoria_contable, emprendedora

urlpatterns = [
    path('', home, name = 'home'),
    path('emprendimiento/', emprendimiento, name = 'emprendimiento'),
    path('producto/', producto, name = 'producto'),
    path('insumo/', insumo, name = 'insumo'),
    path('marketing/', marketing, name = 'producto'),
    path('asesoria_contable/', asesoria_contable, name = 'asesoria_contable'),
    path('emprendedora/', emprendedora, name = 'emprendedora'),
    
]