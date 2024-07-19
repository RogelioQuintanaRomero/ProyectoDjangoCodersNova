from django.shortcuts import render, redirect

from .serializer import PeliculaSerializer
from .models import Pelicula
from .forms import PeliculaForm
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response


# Create your views here.
def inicio(request):
    return render(request, 'paginas/inicio.html')


def ayuda(request):
    return render(request, 'paginas/ayuda.html')

def peliculas(request):
    peliculas = Pelicula.objects.all()
    return render(request, 'peliculas/index.html', {'peliculas': peliculas})
 

def agregar(request):
    formulario = PeliculaForm(request.POST or None, request.FILES or None)
    if formulario.is_valid():
        formulario.save()
        return redirect('peliculas')
    return render(request, 'peliculas/agregar.html', {'formulario': formulario})

def editar(request, id):
    pelicula = Pelicula.objects.get(id=id)
    formulario = PeliculaForm(request.POST or None, request.FILES or None, instance=pelicula)
    if formulario.is_valid() and request.POST:
        formulario.save()
        return redirect('peliculas')    
    return render(request, 'peliculas/editar.html', {'formulario': formulario})
 
def eliminar(request, id):
    pelicula = Pelicula.objects.get(id=id)
    pelicula.delete()
    return redirect('peliculas')

#get de API
class PeliculasList(APIView):
    def get(self, request):
        peliculas = Pelicula.objects.all()
        serializer = PeliculaSerializer(peliculas, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)