# forms.py
from django import forms
from .models import Products

class BuscaProdutoForm(forms.Form):
    query = forms.CharField(label='Buscar Produto', max_length=100)