
from django.contrib import admin
from django.urls import path
from app1 import views

urlpatterns = [
    path('',views.home,name="home"),
    path('inserir',views.inserir,name="inserir"),
    path('salvar',views.salvar,name="salvar")
]
