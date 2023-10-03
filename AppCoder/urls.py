from django.urls import path
from AppCoder import views

urlpatterns = [
    path("inicio/", views.inicio, name="Inicio"),
    path("estudiantes/", views.estudiantes, name="Estudiantes"),
    path("profesores/", views.profesores, name="Profesores"),
    path("cursos/", views.curso, name="Cursos"),
    path("entregables/", views.entregables, name="Entregables"),
    path("cursoform/", views.cursoFormulario, name="CursoForm"),
    path("apicursoform/", views.apiCursoFormulario, name="ApiCursoForm"),
    path("buscar/", views.buscar, name="Buscar"),
    path("mostrar/", views.mostrar, name="Mostrar"),
]
