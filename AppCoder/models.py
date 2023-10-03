from django.db import models


# Create your models here.
class Curso(models.Model):
    nombre = models.CharField(max_length=20)
    camada = models.IntegerField()


class Estudiate(models.Model):
    nombre = models.CharField(max_length=20)
    apellido = models.CharField(max_length=20)
    email = models.EmailField()


class Profesor(models.Model):
    nombre = models.CharField(max_length=20)
    apellido = models.CharField(max_length=20)
    email = models.EmailField(max_length=40)
    profesion = models.CharField(max_length=20)


class Entregable(models.Model):
    nombre = models.CharField(max_length=20)
    fecha_de_entrega = models.CharField(max_length=20)
    entregado = models.BooleanField()
