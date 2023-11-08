from django.shortcuts import render,redirect
# from django.http import HttpResponse
# from django.template import loader
from inicio.models import Concierto
from inicio.models import Venues
from inicio.forms import CrearBandaFormulario
from inicio.forms import CrearVenueFormulario

def inicio(request):
    
    return render (request,'inicio/inicio.html',{})

def conciertos (request):

    banda_a_buscar = request.GET.get('banda')
    if banda_a_buscar:
        listado_de_conciertos = Concierto.objects.filter(banda__icontains=banda_a_buscar)
    else:
        listado_de_conciertos = Concierto.objects.all()

    return render (request,'inicio/conciertos.html',{'listado_de_conciertos':listado_de_conciertos})

def crear_conciertos (request):

    if request.method == 'POST':
        formulario = CrearBandaFormulario (request.POST)
        if formulario.is_valid():
            info_limpia =formulario.cleaned_data

            banda = info_limpia.get('banda')
            genero = info_limpia.get('genero')
            precioEntrada = info_limpia.get('precioEntrada')

            concierto = Concierto(banda=banda.lower(), genero=genero, precioEntrada=precioEntrada)
            concierto.save()

            return redirect('conciertos')
        else:
            return render(request,'inicio/crear_concierto.html',{'formulario': formulario}) 

    formulario = CrearBandaFormulario ()
    return render(request,'inicio/crear_concierto.html',{'formulario': formulario}) 

def crear_venue (request):
    if request.method == 'POST':
        formulario = CrearVenueFormulario (request.POST)
        if formulario.is_valid():
            info_limpia =formulario.cleaned_data

            Nombre = info_limpia.get('Nombre')
            Direccion = info_limpia.get('Direccion')
            capacidad = info_limpia.get('capacidad')

            venue = Venues(Nombre=Nombre.lower(), Direccion=Direccion, capacidad=capacidad)
            venue.save()

            return redirect('venue')
        else:
            return render(request,'inicio/venue.html',{'formulario': formulario}) 

    formulario = CrearVenueFormulario ()
    return render(request,'inicio/venue.html',{'formulario': formulario}) 