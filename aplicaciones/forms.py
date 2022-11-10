from django import forms
from .models import Perfil_emprendedora, Emprendimiento, Producto


class Perfil_emprendedoraForm(forms.ModelForm):

    class Meta:
        model = Perfil_emprendedora
        fields = ["id_user","nombre", "fecha_nacimiento", "email", "telefono", "whatsapp", "telegram", "direccion"]
        
        widgets = {
            "fecha_nacimiento": forms.SelectDateWidget()
        }
        # fields = '__all__'
        
class EmprendimientoForm(forms.ModelForm):

    class Meta:
        model = Emprendimiento
        fields = ["id_perfil_emprendedora", "id_comuna", "id_industria", "id_emprendimiento", "nombre", "email", "website", "id_marketing", "id_asesoria_contable"]

        
        # fields = '__all__'

class ProductoForm(forms.ModelForm):

    class Meta:
        model = Producto
        fields = ["id_emprendimiento", "id_producto", "nombre", "id_despacho"]

