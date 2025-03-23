from django.shortcuts import render

def home (request):
    resultado = 5+6
    context = {'resultado': resultado}
    return render(request,"home.html",context)