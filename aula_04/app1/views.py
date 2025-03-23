from django.shortcuts import render
from django.http import HttpResponse
from .models import agenda
from .Forms import InsereRegistros

def home(request):
    return HttpResponse('<h1>Seja bem vindo minha chará</h1>')

def teste(request):
    return HttpResponse('<h1>Voce esta no teste</h1>')

def agendaTell(request):
    agendaLista = agenda.objects.all()
    tabela = '<table border=1>'
    for amigo in agendaLista:
       nome = amigo.nome
       telefone = amigo.telefone
       saida = f'<tr><td>'+nome+'</td><td>'+str(telefone)+'</td></tr>'
       print(f'{nome}:{telefone}')
       tabela +=saida
    tabela += '</table>'
    return HttpResponse(tabela)

def inserir(request):
    form = InsereRegistros()
    return render(request, "form_inserir.html",{'form':form})

def salvar(request):
    form = InsereRegistros(request.POST)
    form.save()
    return HttpResponse('<h1>Registro salvo com sucesso</h1>')