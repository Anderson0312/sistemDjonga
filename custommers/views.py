from multiprocessing import context
from unittest import loader
from django.http import HttpResponse
from django.shortcuts import redirect, render
from django.urls import reverse

from django.contrib import messages

from custommers.models import custommer

# Create your views here.
def create_custommmer(request):
    if request.method == "GET":
            return render(request, 'clientes.html')         
    else:
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        profissao = request.POST.get('profissao')
        sexo = request.POST.get('sexo')
        address = request.POST.get('address')
        city = request.POST.get('city')
        cep = request.POST.get('cep')
        
        client = custommer.objects.filter(email=email).first()
        
        if client:
            messages.error(request, 'Já existe um usuario com este cliente')
        else:
            client = custommer.objects.create(first_name=first_name, last_name=last_name, email=email, phone=phone, profissao=profissao, sexo=sexo, address=address, city=city, cep=cep)
            return redirect(reverse('client'))