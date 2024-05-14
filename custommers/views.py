from multiprocessing import context
from unittest import loader
from django.http import HttpResponse
from django.shortcuts import get_object_or_404, redirect, render
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from django.template import loader
from django.core.paginator import Paginator, EmptyPage

from django.contrib import messages

from custommers import models
from custommers.forms import BuscaClientForm
from custommers.models import custommer

# Create your views here.
@login_required(login_url='')
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
        address = request.POST.get('Address')
        city = request.POST.get('city')
        cep = request.POST.get('cep')
        
        client = custommer.objects.filter(email=email).first()
        
        if client:
            messages.error(request, 'Já existe um usuario com este cliente')
        else:
            messages.success(request, 'Cliente cadastrado com sucesso')
            client = custommer.objects.create(first_name=first_name, last_name=last_name, email=email, phone=phone, profissao=profissao, sexo=sexo, address=address, city=city, cep=cep)
            return redirect(reverse('client'))
        
              
@login_required(login_url='')
def viewCustommer(request):
    paginate_by = 5
    query = request.GET.get('query')

    if query:
        mCustommer = custommer.objects.filter(name__icontains=query)
    else:
        mCustommer = custommer.objects.all()
        
    form = BuscaClientForm(initial={'query': query})
    
    mCustommer = custommer.objects.all().values()
    
    # Crie um objeto Paginator
    paginator = Paginator(mCustommer, paginate_by)
    
    # Obtenha o número da página atual
    numero_pagina = 2
    
    print(numero_pagina)
    
    try:
        # Obtenha os objetos para a página solicitada
        dados_paginados = paginator.page(numero_pagina)
    except EmptyPage:
        # Se a página solicitada estiver vazia, exiba a última página disponível
        dados_paginados = paginator.page(paginator.num_pages)


    context = {
        'mCustommer': mCustommer,
        # 'form': form,
        'query': query,
        'dados_paginados': dados_paginados,
    }
    
    template = loader.get_template('clienteview.html')
    print(custommer.id)
    
    return HttpResponse(template.render(context, request))



@login_required(login_url='')
def buscar_Cliente(request):
    if request.method == 'GET':
        form = BuscaClientForm(request.GET)
        if form.is_valid():
            query = form.cleaned_data['query']
            custommers = custommer.objects.filter(first_name__icontains=query)
            return render(request, 'resultado_busca_cli.html', {'custommers': custommers, 'query': query})
    else:
        form = BuscaClientForm()
    
    return render(request, 'buscar_cliente.html', {'form': form})


@login_required(login_url='')
def detalhe_cliente(request, cliente_id):
    # Buscar o cliente se estiver editando um existente

    mCustomer = None
    if cliente_id:
        mCustomer = get_object_or_404(custommer, id=cliente_id)
        print(mCustomer.id)
    
    # Restante da lógica da view aqui, como renderizar um template com o cliente

    return render(request, 'detalhe_cliente.html', {'cliente': mCustomer})
