from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    def __str__(self):
        return f'Perfil de {self.user.username}'

class Cliente(models.Model):
    rut = models.CharField(max_length= 10, unique=True)
    nombre = models.CharField(max_length=50)
    apellido = models.CharField(max_length=100)
    password = models.CharField(max_length=50)

opciones_consultas = [
    [0, "consulta"],
    [1, "reclamo"],
    [2, "sugerencia"],
    [3, "felicitaciones"]

]
class Contacto(models.Model):
    nombre = models.CharField(max_length= 50)
    correo = models.EmailField()
    tipo_consulta=models.IntegerField(choices= opciones_consultas)
    mensaje = models.TextField()
    avisos = models.BooleanField()

    def __str__(self) -> str:
        return self.nombre

class productos(models.Model):
    pelicula = models.CharField(max_length=50)
    url = models.CharField(max_length=300)
    image = models.ImageField(null=True, blank=True)

    @property
    def imageURL(self):
        try:
            url = 'static/images'+self.image.url
        except:
            url = ''
        return url
    
    def __str__(self):
        return f'Se agrega el producto {self.pelicula}'