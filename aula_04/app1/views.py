from django.shortcuts import render,redirect
from .models import agenda
from .Forms import InsereRegistros

def home(request):
    amigos = agenda.objects.all()
    context = {"amigos":amigos}
    return render (request,"home.html",context)

def inserir(request):
    
    form = InsereRegistros()
    context = {"formulario":form}
    
    return render(request,"form_inserir.html",context)

def salvar(request):
    form = InsereRegistros(request.POST)
    form.save()
    return redirect(home)