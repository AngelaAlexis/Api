from django.contrib import admin
from .models import Proveedor, Objetivo, EmpresaObjetivos, Comprador

admin.site.register(Proveedor)
admin.site.register(Objetivo)
admin.site.register(EmpresaObjetivos)
admin.site.register(Comprador)
