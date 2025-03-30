from .models import agenda
from .Forms import InsereRegistros
from django.views.generic import ListView,CreateView,UpdateView,DeleteView
from django.urls import reverse_lazy

class AgendaListView(ListView):
    template_name='home.html'
    model = agenda
    context_object_name ='amigos'

class AgendaCreateView(CreateView):
    template_name="form_inserir.html"
    model = agenda
    form_class = InsereRegistros
    success_url = reverse_lazy('lista_amigos') 
    
class AgendaUpdateView(UpdateView):
    template_name='form_editar.html'
    model = agenda
    fields = "__all__"
    success_url = reverse_lazy('lista_amigos')
    
class AgendaDeleteView(DeleteView):
    template_name='confirmar_exclusao.html'
    model = agenda
    success_url = reverse_lazy("lista_amigos")
    