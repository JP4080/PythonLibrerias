from rest_framework import generics
from .models import Estadistica
from .serializers import EstadisticaSerializer
import numpy as np

class EstadisticaListCreateView(generics.ListCreateAPIView):
    queryset = Estadistica.objects.all()
    serializer_class = EstadisticaSerializer