from django.http import HttpResponse
import datetime
from django.template import  Template,Context

def saludo(request):

    doc_externo=open("C:/Users/Diego/Desktop/app de programcacion/curso_completo_jango/Project1/Project1/plantillas/template.html")
    plt=Template(doc_externo.read())
    doc_externo.close()

    ctx= Context()

    documento=plt.render(ctx)

    return HttpResponse(documento)

def reloj(request):
    fecha_actual=datetime.datetime.now()
    documento="""<html>
    <body>
    <h1>
    Fecha y hora actual %s
    </h1>
    </body>
    <html>"""% fecha_actual

    return HttpResponse(documento)

def calculate_age(request,agno,edad):

    agno_actual=2023
    nacimiento=agno_actual-edad
    edad_Futura=agno-nacimiento

    documento="""
    <html>
    <boby>
    <h2> 
    naciste en el agno %s y en el  %s tendras %s
    """ %(nacimiento,agno,edad_Futura)

    return HttpResponse(documento)
