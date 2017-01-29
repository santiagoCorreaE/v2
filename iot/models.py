from django.db import models
from django.utils import timezone

"""
nombre = models.CharField(max_length=50)


"""

class Variable(models.Model):
    nombre = models.CharField(max_length=50)
    unidad = models.CharField(max_length=10)

    def __str__(self):
        return self.nombre

class Tipo_nodo(models.Model):
    nombre = models.CharField(max_length=50)

class Tipo_ubicacion(models.Model):
    nombre = models.CharField(max_length=50)

class Tipo_sensor(models.Model):
    nombre = models.CharField(max_length=50)
    referencia = models.CharField(max_length=50)
    variable = models.ForeignKey(Variable)

class Ubicacion(models.Model):
    nombre = models.CharField(max_length=50)
    tipo_ubicacion = models.ForeignKey(Tipo_ubicacion)

class Nodo(models.Model):
    ubicacion = models.ForeignKey(Ubicacion)
    tipo_nodo = models.ForeignKey(Tipo_nodo)
    nombre = models.CharField(max_length=50)
    ciclo = models.PositiveSmallIntegerField()
    en_campo = models.BooleanField()

class Sensor(models.Model):
    nodo = models.ForeignKey(Nodo)
    tipo_sensor = models.ForeignKey(Tipo_sensor)
    posicion = models.PositiveSmallIntegerField()
    fecha_instalacion = models.DateTimeField()
    on = models.BooleanField()

class Lectura(models.Model):
    sensor = models.ForeignKey(Sensor)
    valor = models.DecimalField(max_digits=8, decimal_places=3)
    fecha = models.DateTimeField()













