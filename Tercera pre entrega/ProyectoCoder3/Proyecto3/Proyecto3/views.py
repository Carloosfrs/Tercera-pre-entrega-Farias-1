from django.http import HttpResponse
from django.template import Template, Context
from django.template import loader

def inicio(request):
	return HttpResponse("Hola Django - Coder")

def alumnos(request):
    return HttpResponse("Página para alumnos")

def probandoTemplate(self):
    
    diccionario = {
        "pepito" : "Daniel",
        "Apellido" : "Becarini",
        "Notas" : [10, 9, 7, 5, 10, 2]
    }
    
    plantilla = loader.get_template("plantilla1.html")
    documento = plantilla.render(diccionario)
    return HttpResponse(documento)



