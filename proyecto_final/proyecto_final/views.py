from django.http import HttpResponse 
from django.template import loader
from django.shortcuts import render
from appaeropuerto.forms import avionFormulario

def saludo(request):
    nombre = "Fran"
    dict_context = {"saludo": "Hola", "nombre_persona": nombre}
    plantilla = loader.get_template("page.html")
    documento = plantilla.render(dict_context)
    return HttpResponse(documento)


def formulario_avion(request):
    if request.method == "POST":
        avion = avionFormulario(request.POST)
        print(avion)
        if avion.is_valid:
            data = avion.cleaned_data
            avion_nuevo = avion(data['marca'], data['capacidad'], data['anio_creacion'])
            avion_nuevo.save()
            return render("appaeropuerto/page.html")
        else:
            avion_form = avionFormulario()
            return render(request, 'appaeropuerto/formulario_avion.html', {"formulario": avion_form})