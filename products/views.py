from django.contrib import messages
from django.shortcuts import redirect, render
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.template import loader

from products.forms import BuscaProdutoForm
from products.models import Products

# Create your views here.
def cadastroProducts(request):
    if request.method == "GET":
            return render(request, 'cadastroProducts.html')         
    else:
        name = request.POST.get('nameProd')
        valor = request.POST.get('valor')
        description = request.POST.get('description')
        category = request.POST.get('category')
                      
        user = Products.objects.filter(username=name).first()
        
        if user:
            messages.error(request, 'Já existe um Produto com este nome cadastrado')
        else:
            products = Products.objects.create(name=name, valor=valor, description=description, category=category)
            messages.success(request, 'Cadastrado com sucesso')
            return redirect(reverse('cadastroProducts'))
        
        
@login_required(login_url='')
def viewProducts(request):
    mProducts = Products.objects.all().values()
    
    context = {
        'mProducts': mProducts,
    }
    

    template = loader.get_template('viewProducts.html')
    
    return HttpResponse(template.render(context, request))

@login_required(login_url='')
def buscar_produto(request):
    if request.method == 'GET':
        form = BuscaProdutoForm(request.GET)
        if form.is_valid():
            query = form.cleaned_data['query']
            produtos = Products.objects.filter(nome__icontains=query)
            return render(request, 'resultado_busca.html', {'produtos': produtos, 'query': query})
    else:
        form = BuscaProdutoForm()
    
    return render(request, 'buscar_produto.html', {'form': form})
    