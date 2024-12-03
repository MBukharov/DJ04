from .models import Film
from django.forms import ModelForm, Textarea, TextInput

class FilmForm(ModelForm):
    class Meta:
        model = Film
        fields = ['name', 'description', 'comment']
        widgets = {
            'name': TextInput(attrs={'class': 'form-control','placeholder':'Название'}),
            'description': Textarea(attrs={'class': 'form-control','placeholder':'Описание'}),
            'comment': TextInput(attrs={'class': 'form-control','placeholder':'Отзыв'}),
        }