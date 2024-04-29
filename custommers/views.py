from multiprocessing import context
from unittest import loader
from django.http import HttpResponse
from django.shortcuts import redirect, render
from django.urls import reverse

# Create your views here.
def create_custommmer(request):
    if request.method == "GET":
            return render(request, 'clientes.html')         
    else:
        print('Creating')
        return redirect(reverse('client'))
    # template = loader.get_template('clientes.html')
    
    # return HttpResponse(template.render(context, request))