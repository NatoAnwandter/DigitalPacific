from django import forms
from .models import Perfil_emprendedora

class Perfil_emprendedoraForm(forms.ModelForm):

    class Meta:
        model = Perfil_emprendedora
        fields = ["nombre", "fecha_nacimiento", "email", "telefono", "whatsapp", "telegram", "direccion", "id_user"]
        # fields = '__all__'
        