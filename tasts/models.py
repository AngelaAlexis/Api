from django.db import models
from django.contrib.auth.models import User


class Proveedor(models.Model):
    nombre = models.CharField(max_length=100)
    producto = models.CharField(max_length=100)
    precio = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f"{self.nombre} - {self.producto} - ${self.precio}"


class Objetivo(models.Model):
    nombre = models.CharField(max_length=100)
    direccion_ip = models.GenericIPAddressField()
    # Puedes ajustar este campo según la unidad de tiempo necesaria
    tiempo_realizar = models.IntegerField()

    def __str__(self):
        return f"{self.nombre} - {self.direccion_ip} - Tiempo: {self.tiempo_realizar} unidades de tiempo"


class EmpresaObjetivos(models.Model):
    nombre_empresa = models.CharField(max_length=100)
    num_trabajadores = models.IntegerField()
    tiempo_realizar = models.IntegerField()

    def __str__(self):
        return f"{self.nombre_empresa} - {self.num_trabajadores} trabajadores - Tiempo: {self.tiempo_realizar} unidades de tiempo"


class Comprador(models.Model):
    nombre = models.CharField(max_length=100)
    num_compras = models.IntegerField()
    total_pagado = models.DecimalField(max_digits=10, decimal_places=2)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.nombre} - Compras: {self.num_compras} - Total Pagado: ${self.total_pagado}"
