from django.test import TestCase
from .models import Producto
import pandas as pd

class ProductoTestCase(TestCase):
    def test_resumen_pandas(self):
        producto = Producto.objects.create(nombre='Test', precio=1000)
        resumen = producto.resumen_pandas()
        self.assertIn('count', resumen)

