from django.db import models
from django.http import HttpResponse

# Create your models here.

class Padre(models.Model):

    nombre=models.CharField(max_length=40)
    edad=models.IntegerField()
    nac=models.DateField()


class Familia(models.Model):

    nombre=models.CharField(max_length=40)
    edad=models.IntegerField()
    nac=models.DateField()

