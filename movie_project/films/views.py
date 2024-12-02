from django.shortcuts import render

# Create your views here.

def index_films(request):
    return render(request, 'films/index.html',)

def add_film(request):
    return render(request, 'films/new_film.html',)