from rest_framework import generics
from .models import Producto
from .serializers import ProductoSerializer
import pandas as pd

class ProductoListCreateView(generics.ListCreateAPIView):
    queryset = Producto.objects.all()
    serializer_class = ProductoSerializer