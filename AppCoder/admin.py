from django.contrib import admin
from .models import Curso, Estudiate, Profesor, Entregable

# Register your models here.
admin.site.register(Curso)
admin.site.register(Estudiate)
admin.site.register(Profesor)
admin.site.register(Entregable)
