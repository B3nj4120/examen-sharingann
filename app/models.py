from django.db import models


# Create your models here.
class numero_serie(models.Model):
    edicion = models.ImageField()
    nombre = models.CharField(max_length=100)
    numero = models.IntegerField()

    def __str__(self):
        return self.nombre

class tienda(models.Model):
    nombre = models.CharField(max_length=50)
    fecha_fabricacion = models.DateField()
    descripcion = models.CharField(max_length=500)
    precio = models.IntegerField()
    unidades = models.IntegerField()
    nuevo = models.BooleanField()
    numero_serie = models.ForeignKey(numero_serie, on_delete=models.PROTECT)
    
    def __str__(self):
        return self.nombre


class usuario(models.Model):
    id_usuario = models.IntegerField()
    nombreusuario = models.CharField(max_length=100)
    email = models.EmailField()
    constraseña = models.CharField(max_length=10)

    def __str__(self):
        return self.nombreusuario



    
opciones_consultas = [
    [ 0, 'consulta'],
    [ 1, 'reclamo'],
    [ 2, 'sugerencia'],
    [ 3, 'felicitaciones'],

     ]

class contacto (models.Model):
    nombre = models.CharField(max_length=50)
    correo = models.EmailField()
    tipo_consulta = models.IntegerField(choices=opciones_consultas)
    mensajes = models.TextField()
    avisos = models.BooleanField()

    def _str_(self):
        return self.nombre
    
    