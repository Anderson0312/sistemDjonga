from multiprocessing import context
from unittest import loader
from django.http import HttpResponse
from django.shortcuts import redirect, render
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from django.template import loader

from django.contrib import messages

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
        address = request.POST.get('address')
        city = request.POST.get('city')
        cep = request.POST.get('cep')
        
        client = custommer.objects.filter(email=email).first()
        
        if client:
            messages.error(request, 'Já existe um usuario com este cliente')
        else:
            client = custommer.objects.create(first_name=first_name, last_name=last_name, email=email, phone=phone, profissao=profissao, sexo=sexo, address=address, city=city, cep=cep)
            return redirect(reverse('client'))
        
              
@login_required(login_url='')
def viewCustommer(request):
    query = request.GET.get('query')

    if query:
        mCustommer = custommer.objects.filter(name__icontains=query)
    else:
        mCustommer = custommer.objects.all()
        
    form = BuscaClientForm(initial={'query': query})
    
    mCustommer = custommer.objects.all().values()
    
    context = {
        'mCustommer': mCustommer,
        # 'form': form,
        'query': query,
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
            print(custommers)
            return render(request, 'resultado_busca.html', {'custommers': custommers, 'query': query})
    else:
        form = BuscaClientForm()
    
    return render(request, 'buscar_cliente.html', {'form': form})