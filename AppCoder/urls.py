from django.urls import path
from AppCoder import views

urlpatterns = [
    path("inicio/", views.inicio, name="Inicio"),
    path("estudiantes/", views.estudiantes, name="Estudiantes"),
    path("profesores/", views.profesores, name="Profesores"),
    path("cursos/", views.cursos, name="Cursos"),
    path("entregables/", views.entregables, name="Entregables"),
]
