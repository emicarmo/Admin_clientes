from django.forms import ModelForm
from .models import Persona, Localidad

class ClienteForm(ModelForm):
    class Meta:
        model = Persona
        fields = '__all__'

class LocalidadForm(ModelForm):
    class Meta:
        model = Localidad
        fields = '__all__'
