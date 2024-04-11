from django.http import HttpResponse, HttpResponseRedirect

from django.shortcuts import render

from django.contrib.auth import authenticate
from django.contrib.auth.models import User



def cadastro(request):
    if request.method == "GET":
            return render(request, 'cadastro.html')
            
    else:
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')
        
        user = User.objects.filter(username=username).first()
        
        if user:
            return HttpResponse('Já existe um usuario com este username')
        
        user = User.objects.create_user(username=username, email=email, password=password)
        print(user)      
        return HttpResponse("usuario cadastrado com sucesso " + username)
    

def login(request):
    if request.method == "GET":
        return render(request, 'login.html')
        
    else:
        username = request.POST.get('username')
        password = request.POST.get('password')
        
        user = authenticate(username=username, password=password)
        if user:
            login(request, user)
            return HttpResponse('User autenticada com sucesso')
        else:
            return HttpResponse('user ou senha invalida')
        
def plataforma(request):
    if request.user.is_authenticated:
        return render(request, 'index.html')
    return HttpResponse('Voce precisaa estar logado')
 
        
          
