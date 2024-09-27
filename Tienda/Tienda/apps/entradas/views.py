from django.views.generic import ListView, DetailView
from django.shortcuts import get_object_or_404, render, redirect
from django.contrib.auth.mixins import LoginRequiredMixin
#from django.contrib.auth.decorators import login_required Hace exactamente lo mismo que el de arriba :v
from django.contrib.auth.models import User
from .models import Entrada, Alumno, Profesor, Asignatura
from django.shortcuts import render
from django.contrib.auth.views import LoginView
from .forms import EmailAuthenticationForm

# Vista basada en clases para listar las entradas
class EntradaListView(LoginRequiredMixin, ListView):
    model = Entrada
    template_name = 'index.html'  # Nombre del template que se utilizará para renderizar la lista
    context_object_name = 'entradas'  # Nombre del contexto que contiene la lista de entradas

    # Opcional: Método para personalizar el queryset
    def get_queryset(self):
        return Entrada.objects.order_by('-fecha_creacion')  # Ordenar las entradas por fecha de creación descendente

# Vista basada en clases para listar los alumnos
class AlumnoListView(ListView):
    model = Alumno
    template_name = 'alumnos.html'  # Nombre del template que se utilizará para renderizar la lista
    context_object_name = 'alumnos'  # Nombre del contexto que contiene la lista de alumnos

    # Método para obtener el contexto adicional si es necesario
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # Puedes agregar más datos al contexto aquí si es necesario
        return context

# Vista basada en funciones para mostrar los detalles de un alumno específico
def detalle_alumno(request, id):
    alumno = get_object_or_404(Alumno, pk=id)  # Obtener el alumno o devolver un 404 si no existe
    return render(request, 'detalle_alumno.html', {'alumno': alumno})  # Renderizar el template con el alumno

# Vista basada en clases para listar los profesores
class ProfesorListView(ListView):
    model = Profesor
    template_name = 'profesores.html'  # Nombre del template que se utilizará para renderizar la lista
    context_object_name = 'profesores'  # Nombre del contexto que contiene la lista de profesores

    # Método para obtener el contexto adicional si es necesario
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # Puedes agregar más datos al contexto aquí si es necesario
        return context

# Vista basada en funciones para mostrar los detalles de un profesor específico
def detalle_profesor(request, id):
    profesor = get_object_or_404(Profesor, pk=id)  # Obtener el profesor o devolver un 404 si no existe
    return render(request, 'detalle_profesor.html', {'profesor': profesor})  # Renderizar el template con el profesor

# Vista para el curso "Calidad del Software"
def asignatura(request):
    return render(request, 'vista_alumno.html')


# Vista para el inicio de sesión de usuario
class CustomLoginView(LoginView):
    authentication_form = EmailAuthenticationForm
    template_name = 'registration/login.html'  # Asegúrate de que el nombre del template sea correcto
    
def index(sefl):
    return redirect('index')


def lista_asignaturas(request):
    asignaturas = Asignatura.objects.all()
    return render(request, 'vista alumno/asignaturas.html', {'asignaturas': asignaturas})


