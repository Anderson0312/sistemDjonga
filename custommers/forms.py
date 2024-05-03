# forms.py
from django import forms
from .models import custommer

class BuscaClientForm(forms.Form):
    query = forms.CharField(label='Buscar clinte', max_length=100)