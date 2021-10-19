from django.db import models
from django.contrib.auth.models import User


class Categoria (models.Model):
    nombre = models.CharField(max_length=50)
    def __str__(self):
        return self.nombre

ciudad =(
    ('San Andres', 'San Andres'),
    ('Providencia', 'Providencia'),
    ('Santa Catalina', 'Santa Catalina')
)

class Sitio(models.Model):
    nombre = models.CharField(max_length=100)
    descripcion = models.TextField(null=True, blank=True)
    telefono = models.IntegerField(null=True, blank=True)
    direccion = models.CharField(max_length=100, null=True, blank=True)
    ciudad = models.CharField(max_length=100, choices=ciudad, default='San Andres')
    imagen = models.ImageField(upload_to='imagenes')
    categoria = models.ForeignKey(Categoria, on_delete=models.PROTECT)
    usuario = models.ForeignKey(User, on_delete=models.PROTECT)
    def __str__(self):
        return self.nombre + "" +self.descripcion + "" + self.ciudad

