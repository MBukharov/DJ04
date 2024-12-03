from django.urls import path, include
from . import views

urlpatterns = [
    path('',views.index_films,name = 'show_films'),
    path('new_film',views.add_film, name='add_film'),
]