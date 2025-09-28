from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request, 'recipes/home.html', context={
        'name': 'Douglas',
    })

def contato(request):
    return render(request, 'temp/temp.html')

def sobre(request):
    return HttpResponse('Página Sobre')
    