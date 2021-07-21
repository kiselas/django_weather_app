from django.forms import ModelForm, TextInput
from .models import City

class CityForm(ModelForm):
    class Meta:
        model = City
        fields = ['name', 'code']
        widgets = {'name': TextInput(attrs={'class' : 'input', 'placeholder':'City name'}),
                   'code': TextInput(attrs={'class' : 'input', 'placeholder':'City code'})}