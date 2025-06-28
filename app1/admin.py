from django.contrib import admin
from .models import Producto
import pandas as pd

class ProductoAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'precio')

admin.site.register(Producto, ProductoAdmin)