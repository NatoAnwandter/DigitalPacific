from django.contrib import admin
from .models import *
from django.contrib.auth.models import User
from django.contrib.auth.models import AbstractUser 
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin 
from import_export import resources
from import_export.admin import ImportExportModelAdmin

class ProductoResource(resources.ModelResource):
    class Meta:
        model = Producto

class ProductoAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    list_display= ["nombre", "id_despacho"]
    search_fields = ["nombre"]
    list_filter = ["nombre", "id_despacho"]
    resource_class = ProductoResource

class InsumoAdmin(admin.ModelAdmin):
#     # # list_display= ["productos"]
    search_fields = ["nombre"]

# Register your models here.
admin.site.register(Perfil_emprendedora)
admin.site.register(Emprendimiento)
admin.site.register(Asesoria_contable)
admin.site.register(Marketing)
admin.site.register(Producto, ProductoAdmin)
admin.site.register(Despacho)
admin.site.register(Insumo, InsumoAdmin)
admin.site.register(Cantidad)
admin.site.register(Frecuencia)
admin.site.register(Industria)
admin.site.register(Provincia)
admin.site.register(Comuna)
admin.site.register(Region)
admin.site.register(Tipo_usuario)
admin.site.register(Usuario)









