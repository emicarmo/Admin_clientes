from django.db import models
from django.contrib.auth.models import User

# Create your models here.

TIPO_IVA_CHOICE = (
    ("CF", "Cons. final"),
    ("RI", "Responsable inscripto"),
    ("MT", "Monotributo")
)

class Localidad(models.Model):
    nombre = models.CharField("Nombre localidad",  max_length=50)
    cp = models.CharField("Cod postal", max_length=10)
    provincia = models.CharField(max_length=50)

    class Meta:
        verbose_name_plural = "Localidades"
        ordering = ["nombre"]

    def __str__(self) -> str:
        return f'{self.nombre} Pcia: {self.provincia}'

class Persona(models.Model):
    nombre = models.CharField("Nombre/s", max_length=150)
    apellido = models.CharField(max_length=100)
    edad = models.IntegerField(null=True, blank=True)
    email = models.EmailField(null=True, blank=True)
    activo = models.BooleanField(default=True)
    fecha_nac = models.DateField("Fecha de nacimiento", null=True, blank=True)
    tipo_iva = models.CharField("Tipo de Iva", max_length=2, choices=TIPO_IVA_CHOICE, default="CF")
    localidad = models.ForeignKey(Localidad, on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self) -> str:
        return f'{self.nombre} {self.apellido}'