from rest_framework import generics
from .models import Grafico
from .serializers import GraficoSerializer
import matplotlib.pyplot as plt

class GraficoListCreateView(generics.ListCreateAPIView):
    queryset = Grafico.objects.all()
    serializer_class = GraficoSerializer