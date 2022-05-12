from django.shortcuts import render, redirect
from django.contrib import messages
from django.http import Http404, HttpResponse, HttpResponseBadRequest, HttpResponseNotFound
import sqlite3
import requests
from .forms import ClienteForm, AnimalForm, ConsultaForm
from .models import Cliente, Animal, Consulta


# Create your views here.

def home(request):
    connection = sqlite3.connect('contabilidad.sqlite')
    cliente = connection.cursor()
    cliente.execute("select * from personas")
    content = {
        "clientes": cliente
    }
    connection.close()
    return render(request, 'myapp/index.html', content)

def dollar(request):
    data = requests.get("https://api.recursospython.com/dollar").json()

    content = {
        "data": data,
        "monedas": ['Dollar', 'Peso']
    }

    return render(request, 'myapp/dollar.html', content)

def comentarios(request, pelicula_nombre, comentario_numero):
    if (isinstance(comentario_numero, int)):
        content = {
            "pelicula_nombre": pelicula_nombre,
            "comentario_numero": comentario_numero
        }
        return render(request, 'myapp/comentarios.html', content)
    
    return Http404

def animales(request):
    animales = Animal.objects.all()

    content = {
       "animales": animales
    }
    return render(request, 'animales/animales.html', content)

def clientes(request):
    clientes = Cliente.objects.all()
    
    content = {
        "clientes": clientes
    }
    return render(request, 'clientes/clientes.html', content)

def animal(request, animal_id):
    animal = Animal.objects.get(id=animal_id)
    content = {
       "animal": animal
    }
    return render(request, 'animales/animal.html', content)

def cliente(request, nro_documento):
    try:
        cliente = Cliente.objects.get(documento=nro_documento)
        content = {
            "cliente": cliente
        }
        return render(request, 'clientes/cliente.html', content)
    except:
        return HttpResponseBadRequest("No existe")



def crear_cliente(request):
    form = ClienteForm()
    if request.method == 'POST':
        form = ClienteForm(request.POST)
        if (form.is_valid()):
            form.save()
            messages.success(request, 'Cliente creado correctamente')
            return redirect('/clientes')
 
    content = {
        "form": form,
        "mode": "ADD"
    }
    return render(request, 'forms/crear_cliente.html', content)

def crear_animal(request):
    form = AnimalForm()
    if request.method == 'POST':
        form = AnimalForm(request.POST)
        if (form.is_valid()):
            form.save()
            return redirect('/animales')

    content = {
        "form": form,
        "mode": "ADD"
    }
    return render(request, 'forms/crear_animal.html', content)

def editar_cliente(request, cliente_id):
    cliente = Cliente.objects.get(id=cliente_id)
    form = ClienteForm(instance=cliente)

    if (request.method == 'POST'):
        form = ClienteForm(request.POST, instance=cliente)
        if (form.is_valid()):
            form.save()
            messages.success(request, 'Cliente editado correctamente')
            return redirect('/clientes')

    content = {
        "form": form,
        "mode": "EDIT"
    }
    return render(request, 'forms/crear_cliente.html', content)

def editar_animal(request, animal_id):
    animal = Animal.objects.get(id=animal_id)
    form = AnimalForm(instance=animal)

    if (request.method == 'POST'):
        form = AnimalForm(request.POST, instance=animal)
        if (form.is_valid()):
            form.save()
            messages.success(request, 'Animal editado correctamente')
            return redirect('/animales')

    content = {
        "form": form,
        "mode": "EDIT"
    }
    return render(request, 'forms/crear_animal.html', content)

def eliminar_cliente(request, nro_documento):
    cliente = Cliente.objects.get(documento=nro_documento)
    if (request.method == 'POST'):
        cliente.delete()
        messages.success(request, 'El cliente {} ha sido eliminado correctamente'.format(cliente))
        return redirect('clientes')

    content = {
        "obj": cliente
    }

    return render(request, 'myapp/delete.html', content)

def eliminar_animal(request, animal_id):
    animal = Animal.objects.get(id=animal_id)
    if (request.method == 'POST'):
        animal.delete()
        messages.success(request, 'El animal {} ha sido eliminado correctamente'.format(animal))
        return redirect('animales')

    content = {
        "obj": animal
    }

    return render(request, 'myapp/delete.html', content)

def registro_de_consultas(request):
    consultas = Consulta.objects.all()
    content = {
        "consultas": consultas
    }
    return render(request, 'consultas/consultas.html', content)

def crear_consulta(request):
    form = ConsultaForm()
    if request.method == 'POST':
        form = ConsultaForm(request.POST)
        if (form.is_valid()):
            form.save()
            messages.success(request, 'Consulta registrada correctamente')
            return redirect('consultas')

    content = {
        "form": form
    }
    return render(request, 'forms/crear_consulta.html', content)

def eliminar_consulta(request, consulta_id):
    consulta = Consulta.objects.get(id=consulta_id)
    content = {
        "obj": consulta
    }

    if (request.method == 'POST'):
        consulta.delete()
        messages.success(request, '{} ha sido borrada correctamente'.format(consulta))
        return redirect('consultas')

    return render(request, 'myapp/delete.html', content)

def editar_consulta(request, consulta_id):
    consulta = Consulta.objects.get(id=consulta_id)
    form = ConsultaForm(instance=consulta)
    if (request.method == 'POST'):
        form = ConsultaForm(request.POST, instance=consulta)
        if (form.is_valid()):
            form.save()
            return redirect('consultas')

    content = {
        "form": form,
        "mode": "EDIT"
    }
    return render(request, 'forms/crear_consulta.html', content)
    









