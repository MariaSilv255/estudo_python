
from django.contrib import admin
from django.urls import path
from app1 import views

urlpatterns = [
   
    path('',views.AgendaListView.as_view(), name='lista_amigos'),
    path('inserir',views.AgendaCreateView.as_view(),name='inserir'),
    path('editar/<int:pk>',views.AgendaUpdateView.as_view(),name='editar'),
    path('excluir/<int:pk>',views.AgendaDeleteView.as_view(),name='excluir')
]
