from .models import Boletins
from django.views.generic import ListView,CreateView,UpdateView,DeleteView
from .forms import inserer_registro
from  django.urls import reverse_lazy

class BoletinsListView(ListView):
    template_name ="home.html"
    model = Boletins
    context_object_name = "notas_alunos"
    
class BoletinsCreateView(CreateView):
    template_name = "inserir_registro.html"
    model = Boletins
    form_class = inserer_registro
    success_url = reverse_lazy('listagem')

class BoletinsUpdateView(UpdateView):
    template_name ="editar_registro.html"
    model = Boletins
    fields= '__all__'
    success_url=reverse_lazy('listagem')
    
class BoletinsDeleteView(DeleteView):
    template_name='confirmacao.html'
    model = Boletins
    success_url = reverse_lazy("listagem")