
from django.contrib import admin
from django.urls import path
from App01 import views

urlpatterns = [
    path('', views.home, name='home')
]
