from django.http import HttpResponse, HttpResponseRedirect

from django.shortcuts import render

from django.contrib.auth import authenticate
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login as login_django
from django.template import loader

from plataforma.models import Products

@login_required(login_url='')
def index(request):
    mProducts = Products.objects.all().values()
    
    context = {
        'mProducts': mProducts
    }
    
    template = loader.get_template('index.html')
    
    return HttpResponse(template.render(context, request))

