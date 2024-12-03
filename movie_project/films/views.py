from django.shortcuts import render,redirect
from .models import Film
from .forms import FilmForm

# Create your views here.

def index_films(request):
    films = Film.objects.all()
    return render(request, 'films/index.html',{'films':films})

def add_film(request):
    error = None
    if request.method == 'POST':
        form = FilmForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect ('show_films')
        else:
            error = "Данные введены неверно"

    form = FilmForm()
    return render(request, 'films/new_film.html',{'form':form,'error':error})