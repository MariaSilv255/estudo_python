
from django.contrib import admin
from django.urls import path
from app1 import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.home,name="home"),
    path('teste',views.teste,name="teste"),
    path('agendaTell',views.agendaTell,name="agendaTell"),
    path('inserir',views.inserir,name="inserir"),
    path('salvar',views.salvar,name="salvar")
]
