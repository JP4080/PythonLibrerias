from django.db import models
import matplotlib.pyplot as plt

class Grafico(models.Model):
    titulo = models.CharField(max_length=100)

    def generar_grafico(self):
        plt.figure()
        plt.plot([1, 2, 3], [4, 5, 6])
        plt.title(self.titulo)
        ruta = f'static/grafico_{self.id}.png'
        plt.savefig(ruta)
        plt.close()
        return ruta
