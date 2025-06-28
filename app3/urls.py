from django.urls import path
from .views import EstadisticaListCreateView

urlpatterns = [
    path('estadisticas/', EstadisticaListCreateView.as_view(), name='estadistica-list-create'),
]
