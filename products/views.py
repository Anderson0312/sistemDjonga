from msilib.schema import ListView
from django.contrib import messages
from django.shortcuts import redirect, render
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.template import loader

from products.forms import BuscaProdutoForm
from products.models import Products

from django.urls import reverse_lazy
from django.views.generic import DeleteView

from django.core.paginator import Paginator
from django.core.paginator import EmptyPage
from django.core.paginator import PageNotAnInteger

# Create your views here.
def cadastroProducts(request):   
    if request.method == "GET":
            return render(request, 'cadastroProducts.html')         
    else:
        name = request.POST.get('nameProd')
        valor = request.POST.get('valor')
        description = request.POST.get('description')
        category = request.POST.get('category')
                      
        product = Products.objects.filter(name=name).first()
        
        if product:
            messages.error(request, 'Já existe um Produto com este nome cadastrado')
            return redirect(reverse('viewProducts'))
        else:
            products = Products.objects.create(name=name, valor=valor, description=description, category=category)
            messages.success(request, 'Cadastrado com sucesso')
            return redirect(reverse('viewProducts'))
                
@login_required(login_url='')
def viewProducts(request):
    mProducts = Products.objects.all().values()
    
    context = {
        'mProducts': mProducts,
    }
    
    template = loader.get_template('cadastroProducts.html')
    
    return HttpResponse(template.render(context, request))


@login_required(login_url='')
def buscar_produto(request):
    if request.method == 'GET':
        form = BuscaProdutoForm(request.GET)
        if form.is_valid():
            query = form.cleaned_data['query']
            produtos = Products.objects.filter(name__icontains=query)
            print(produtos)
            return render(request, 'resultado_busca.html', {'produtos': produtos, 'query': query})
    else:
        form = BuscaProdutoForm()
    
    return render(request, 'buscar_produto.html', {'form': form})

class ProdutoDeleteView(DeleteView):
    model = Products
    success_url = reverse_lazy('viewProducts')  # substitua pelo nome da sua URL
    template_name = 'produto_confirm_delete.html'  # opcional: personalize o template
    
    