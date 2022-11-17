from django import forms
from .models import Perfil_emprendedora, Emprendimiento, Producto, Insumo, Cantidad


class Perfil_emprendedoraForm(forms.ModelForm):
    
    class Meta:
        model = Perfil_emprendedora
        fields = ["id_user","fecha_nacimiento",
        "telefono", "whatsapp", "telegram", "direccion"]
        
        error_css_class = 'error-field'
        require_css_class = 'required-field'
        
        widgets = {        
        # "fecha_nacimiento": forms.SelectDateWidget(years=range(1955, 2007), ),
        "fecha_nacimiento": forms.DateInput(attrs={'type': 'date'}),
        "direccion" : forms.Textarea(attrs={"rows":3})                
        }

    def __init__(self,*args, **kwards):
        super().__init__(*args, **kwards)
        self.fields['id_user'].label = 'Usuario'
        
        # fields = '__all__'
        
class EmprendimientoForm(forms.ModelForm):
    
    class Meta:
        model = Emprendimiento
        fields = ["id_perfil_emprendedora", "id_comuna", "id_industria", "id_emprendimiento", "nombre", "email", "website", "id_marketing", "id_asesoria_contable"]
        
        error_css_class = 'error-field'
        require_css_class = 'required-field'

    def __init__(self,*args, **kwards):
        super().__init__(*args, **kwards)
        # self.fields['email'].widget.attrs.update({'class': 'form-control-2'})
        self.fields['nombre'].label = 'nombre del emprendimiento'
        self.fields['id_perfil_emprendedora'].label = 'emprendedora'
        self.fields['id_comuna'].label = 'comuna'
        self.fields['id_industria'].label = 'industria'
        self.fields['id_marketing'].label = 'incluye marketing'
        self.fields['id_asesoria_contable'].label = 'incluye asesoria contable'
        
        # fields = '__all__'

class ProductoForm(forms.ModelForm):

    class Meta:
        model = Producto
        fields = ["id_emprendimiento", "id_producto", "nombre", "id_despacho"]
        # fields = '__all__'

    def __init__(self,*args, **kwards):
        super().__init__(*args, **kwards)
        # self.fields['email'].widget.attrs.update({'class': 'form-control-2'})
        self.fields['id_emprendimiento'].label = 'emprendimiento'
        self.fields['nombre'].label = 'producto'
        self.fields['id_despacho'].label = 'incluye despacho'

class InsumoForm(forms.ModelForm):

    class Meta:      
        model = Insumo
        fields = ["id_producto", "id_insumo", "nombre", "id_cantidad", "id_frecuencia"]

    def __init__(self,*args, **kwards):
        super().__init__(*args, **kwards)
        self.fields['id_producto'].label = 'producto'
        self.fields['nombre'].label = 'insumo'
        self.fields['id_cantidad'].label = 'cantidad'
        self.fields['id_frecuencia'].label = 'frecuencia'

class CantidadForm(forms.ModelForm):

    class Meta:    
        model = Cantidad
        fields = ["id_cantidad", "tipo", "cantidad"]    

    
