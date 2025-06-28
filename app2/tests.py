from django.test import TestCase
from .models import Grafico
import matplotlib.pyplot as plt
import os

class GraficoTestCase(TestCase):
    def test_generar_grafico(self):
        grafico = Grafico.objects.create(titulo='Prueba')
        ruta = grafico.generar_grafico()
        self.assertTrue(os.path.exists(ruta))
