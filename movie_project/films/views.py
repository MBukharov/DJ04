from django.shortcuts import render
from .models import Film

# Create your views here.

def index_films(request):
    films = Film.objects.all()
    return render(request, 'films/index.html',{'films':films})

def add_film(request):
    return render(request, 'films/new_film.html',)