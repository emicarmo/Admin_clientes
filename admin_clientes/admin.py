from django.contrib import admin
from .models import Persona, Localidad

# Register your models here.

modelos = [Localidad, Persona]
admin.site.register(modelos)