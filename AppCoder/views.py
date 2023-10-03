from django.shortcuts import render
from AppCoder.models import Curso
from AppCoder.forms import CursoFormulario, BuscaCursoForm


# Create your views here.
def inicio(request):
    return render(request, "AppCoder/index.html")


def curso(request):
    return render(request, "AppCoder/cursos.html")


def profesores(request):
    return render(request, "AppCoder/profesores.html")


def estudiantes(request):
    return render(request, "AppCoder/estudiantes.html")


def entregables(request):
    return render(request, "AppCoder/entregables.html")


def cursoFormulario(request):
    if request.method == "POST":
        curso = Curso(curso=request.POST["curso"], camada=request.POST["camada"])

        curso.save()

        return render(request, "AppCoder/index.html")

    return render(request, "AppCoder/cursoFormulario.html")


def apiCursoFormulario(request):
    if request.method == "POST":
        miFormulario = CursoFormulario(
            request.POST
        )  # Aqui me llega la informacion del html
        print(miFormulario)

        if miFormulario.is_valid():
            informacion = miFormulario.cleaned_data
            curso = Curso(curso=informacion["curso"], camada=informacion["camada"])
            curso.save()
            return render(request, "AppCoder/index.html")
    else:
        miFormulario = CursoFormulario()

    return render(
        request, "AppCoder/apicursoFormulario.html", {"miFormulario": miFormulario}
    )


def buscar(request):
    if request.method == "POST":
        miFormulario = BuscaCursoForm(
            request.POST
        )  # Aqui me llega la informacion del html
        print(miFormulario)

        if miFormulario.is_valid():
            informacion = miFormulario.cleaned_data
            cursos = Curso.objects.filter(nombre__icontains=informacion["curso"])

            return render(request, "AppCoder/lista.html", {"cursos": cursos})
    else:
        miFormulario = BuscaCursoForm()

    return render(
        request, "AppCoder/formulario_api.html", {"miFormulario": miFormulario}
    )


def mostrar():
    pass
