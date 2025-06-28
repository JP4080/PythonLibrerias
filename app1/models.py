from django.db import models
import pandas as pd

class Producto(models.Model):
    nombre = models.CharField(max_length=100)
    precio = models.DecimalField(max_digits=10, decimal_places=2)

    def resumen_pandas(self):
        df = pd.DataFrame({'Precio': [self.precio]})
        return df.describe().to_html()