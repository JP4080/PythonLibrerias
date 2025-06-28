from django.db import models
import numpy as np

class Estadistica(models.Model):
    valor1 = models.IntegerField()
    valor2 = models.IntegerField()

    def calcular_suma_numpy(self):
        arreglo = np.array([self.valor1, self.valor2])
        return np.sum(arreglo)
