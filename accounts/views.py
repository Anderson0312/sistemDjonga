from multiprocessing import context

from django.http import HttpResponse, HttpResponseRedirect

from django.shortcuts import render
from django.template import loader

from django.contrib.auth import authenticate
from django.contrib.auth.models import User



def register(request):
    if request.method == "GET":
            return render(request, 'registration/cadastro.html')
            
    else:
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')
        
        user = User.objects.filter(username=username).first()
        
        if user:
            return HttpResponse('Já existe um usuario com este username')
        
        user = User.objects.create_user(username=username, email=email, password=password)
        user.save()        
        return HttpResponse("usuario cadastrado com sucesso")
    

def login(request):
    if request.method == "GET":
        print('1')
        return render(request, '/registration/login.html')
        
    else:
        username = request.POST.get('username')
        password = request.POST.get('password')
        
        user = authenticate(username=username, password=password)
        print('2')
        if user:
            login(request, user)
            return HttpResponse('User autenticada com sucesso')
        else:
            return HttpResponse('user não encontrado')
        
          
