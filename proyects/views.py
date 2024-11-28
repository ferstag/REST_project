from django.shortcuts import render, redirect, get_object_or_404
from .models import Proyect

# Vista para la página principal
def index(request):
    projects = Proyect.objects.all()
    return render(request, 'index.html', {'projects': projects})

def create(request):
    if request.method == 'POST':
        title = request.POST.get('title')
        description = request.POST.get('description')
        technology = request.POST.get('technology')

        # Crear un nuevo proyecto
        Proyect.objects.create(
            title=title,
            description=description,
            technology=technology
        )

        return redirect('index')  # Redirige a la página principal después de crear el proyecto

    return render(request, 'create.html')  # Muestra el formulario de creación si es GET

# Vista para editar un proyecto
def edit(request, id):
    project = get_object_or_404(Proyect, id=id)
    if request.method == 'POST':
        project.title = request.POST.get('title')
        project.description = request.POST.get('description')
        project.technology = request.POST.get('technology')
        project.save()
        return redirect('index')
    return render(request, 'edit.html', {'project': project})