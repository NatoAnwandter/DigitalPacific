from django import forms
from .models import Perfil_emprendedora, Emprendimiento, Producto


class Perfil_emprendedoraForm(forms.ModelForm):
    
    class Meta:
        model = Perfil_emprendedora
        fields = ["id_user","nombre","fecha_nacimiento",
        "email", "telefono", "whatsapp", "telegram", "direccion"]
        
        error_css_class = 'error-field'
        require_css_class = 'required-field'
        
        widgets = {        
        "fecha_nacimiento": forms.SelectDateWidget(years=range(1955, 2007), ), 
        "direccion" : forms.Textarea(attrs={"rows":3})                
        }

    def __init__(self,*args, **kwards):
        super().__init__(*args, **kwards)
        self.fields['id_user'].label = 'tipo de usuario'
        
        # fields = '__all__'
        
class EmprendimientoForm(forms.ModelForm):
    
    # name = forms.CharField(widget=forms.TextInput(attrs={"class":"form-control", 
    # "placeholder":"Nombre emprendimiento"}))
    class Meta:
        model = Emprendimiento
        fields = ["id_perfil_emprendedora", "id_comuna", "id_industria", "id_emprendimiento", "nombre", "email", "website", "id_marketing", "id_asesoria_contable"]
        
        error_css_class = 'error-field'
        require_css_class = 'required-field'

        # widgets={
        # "nombre" : forms.TextInput(attrs={"class":"form-control", 
        #                                 "placeholder" : "Nombre de su emprendimiento"})
        # } 

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

    def __init__(self,*args, **kwards):
        super().__init__(*args, **kwards)
        # self.fields['email'].widget.attrs.update({'class': 'form-control-2'})
        self.fields['id_emprendimiento'].label = 'emprendimiento'
        self.fields['nombre'].label = 'producto'
        self.fields['id_despacho'].label = 'incluye despacho'