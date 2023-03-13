from django.db import models


# Create your models here.
class Curso(models.Model): #herencia para que tome como un modelo para bd
    nombre = models.CharField(max_length=48) #nombre es un string con una long maxima
    camada = models.IntegerField()
