from django.shortcuts import render

def home(request):
    signo = "libra"
    nome="Maria"
    idade ="24"
    context = {
        'nome':nome,
        'idade':idade,
        'signo':signo
               }
    return render(request,'home.html',context)
