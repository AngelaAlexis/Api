from django import forms
from .models import Proveedor, Objetivo, EmpresaObjetivos, Comprador


class ProveedorForm(forms.ModelForm):
    class Meta:
        model = Proveedor
        fields = ['nombre', 'producto', 'precio']


class ObjetivoForm(forms.ModelForm):
    class Meta:
        model = Objetivo
        fields = ['nombre', 'direccion_ip', 'tiempo_realizar']


class EmpresaObjetivosForm(forms.ModelForm):
    class Meta:
        model = EmpresaObjetivos
        fields = ['nombre_empresa', 'num_trabajadores', 'tiempo_realizar']


class CompradorForm(forms.ModelForm):
    class Meta:
        model = Comprador
        fields = ['nombre', 'num_compras', 'total_pagado']
