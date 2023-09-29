# Create your models here.
from django.db import models

class Ordenes(models.Model):
    nombre_cliente = models.CharField(max_length=100)
    total = models.DecimalField(max_digits=10, decimal_places=2)

