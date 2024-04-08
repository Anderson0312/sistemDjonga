from django.urls import reverse
from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect

from.models import User
from.models import Products

from django.template import loader

def index(request):
    mUsers = User.objects.all().values()
    
    context = {
        'mUsers': mUsers
    }
    
    mProducts = Products.objects.all().values()
    
    context = {
        'mProducts': mProducts
    }
    
    template = loader.get_template('index.html')
    
    return HttpResponse(template.render(context, request))


def create(resquest):
    template = loader.get_template('signup.html')
    
    return HttpResponse(template.render({},resquest))

def createUser(resquest):
    name = resquest.POST['name'],
    email = resquest.POST['email'],
    endereco = resquest.POST['endereco'],
    password = resquest.POST['password']
    
    newUser = User(name=name, email=email, password=password, endereco=endereco)
    newUser.save()
    return HttpResponseRedirect(reverse('index'))

def login(resquest):
    template = loader.get_template('login.html')
    
    return HttpResponse(template.render({},resquest))

