from django.db import models

# Create your models here.


class Avion(models.Model):
    id = models.AutoField(primary_key=True)
    marca = models.CharField(max_length=60)
    capacidad = models.IntegerField()
    anio_creacion = models.IntegerField()


class Empleado(models.Model):
    nombre = models.CharField(max_length=60)
    apellido = models.CharField(max_length=60)
    profesion = models.CharField(max_length=60)
    dni = models.IntegerField()


class Pasajero(models.Model):
    nombre = models.CharField(max_length=60)
    apellido = models.CharField(max_length=60)
    dni = models.IntegerField()
    email = models.EmailField()