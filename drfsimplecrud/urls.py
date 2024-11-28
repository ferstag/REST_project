from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from proyects import views
from proyects.api import ProjectViewSet

# Configurar el router de la API
router = DefaultRouter()
router.register('projects', ProjectViewSet, basename='projects')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name='index'),  # Página de inicio
    path('create/', views.create, name='create'),  # Vista para crear proyecto
    path('edit/<int:id>/', views.edit, name='edit'),  # Editar proyecto
    path('api/', include(router.urls)),  # Rutas de la API
]


