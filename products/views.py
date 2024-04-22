from django.contrib import messages
from django.shortcuts import redirect, render
from django.urls import reverse

from products.models import Products

# Create your views here.
def cadastroProducts(request):
    if request.method == "GET":
            return render(request, 'cadastroProducts.html')         
    else:
        name = request.POST.get('username')
        valor = request.POST.get('email')
        description = request.POST.get('password')
        category = request.POST.get('password')
                      

        user = Products.objects.filter(username=name).first()
        
        if user:
            messages.error(request, 'Já existe um Produto com este nome cadastrado')
        else:
            products = Products.objects.create(name=name, valor=valor, description=description, category=category)
            return redirect(reverse('cadastroProducts'))
    