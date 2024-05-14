# forms.py
from django import forms
from .models import custommer

class BuscaClientForm(forms.Form):
    query = forms.CharField(label='Buscar cliente', max_length=100 , widget=forms.TextInput(attrs={'class': 'text-primary'}))