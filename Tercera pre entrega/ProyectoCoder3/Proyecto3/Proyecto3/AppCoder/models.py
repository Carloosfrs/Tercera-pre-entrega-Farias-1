from django.db import models

# Create your models here.

class Curso(models.Model):
    
    nombre = models.CharField(max_length=40)
    camada = models.IntegerField()
    
class Estudiantes(models.Model):
    nombre = models.CharField(max_length=30)
    apellido = models.CharField(max_length=30)
    email = models.EmailField()

class Profesores(models.Model):
    nombre = models.CharField(max_length=30)
    apellido = models.CharField(max_length=30)
    email = models.EmailField()
    asignatura = models.CharField(max_length=30)
    
class Entregas(models.Model):
    nombre = models.CharField(max_length=30)
    Asignatura = models.CharField(max_length=30)
    entregado = models.BooleanField()
    
