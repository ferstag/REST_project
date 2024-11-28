from rest_framework import viewsets, permissions
from .models import Proyect
from .serializers import ProyectSerializer

class ProjectViewSet(viewsets.ModelViewSet):
    queryset = Proyect.objects.all()  # Consulta todos los proyectos
    permission_classes = [permissions.AllowAny]  # Permite acceso sin restricciones
    serializer_class = ProyectSerializer  # Usa el serializer ProyectSerializer


    