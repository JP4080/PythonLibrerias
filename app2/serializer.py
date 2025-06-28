from rest_framework import serializers
from .models import Grafico
import matplotlib.pyplot as plt

class GraficoSerializer(serializers.ModelSerializer):
    grafico_path = serializers.SerializerMethodField()

    class Meta:
        model = Grafico
        fields = ['id', 'titulo', 'grafico_path']

    def get_grafico_path(self, obj):
        return obj.generar_grafico()