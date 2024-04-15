from django.http import HttpResponse, HttpResponseRedirect

from django.shortcuts import render

from django.contrib.auth import authenticate
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login as login_django

from django.urls import reverse
from django.shortcuts import redirect



def cadastro(request):
    if request.method == "GET":
            return render(request, 'cadastro.html')
            
    else:
        username = request.POST.get('username')
        email = request.POST.get('email')
        name = request.POST.get('name')
        profissao = request.POST.get('profissao')
        sexo = request.POST.get('sexo')
        pais = request.POST.get('pais')
        city = request.POST.get('city')
        password = request.POST.get('password')
        
        user = User.objects.filter(username=username).first()
        
        if user:
            return HttpResponse('Já existe um usuario com este username')
        else:
            user = User.objects.create_user(username=username, email=email, name=name, profissao=profissao, sexo=sexo, pais=pais, city=city, password=password)
            return redirect(reverse('login'))
    

def login(request):
    if request.method == "GET":
        return render(request, 'login.html')
        
    else:
        username = request.POST.get('username')
        password = request.POST.get('password')
        
        user = authenticate(username=username, password=password)
        if user:
            login_django(request, user)
            return render(request, 'index.html')
        else:
            return HttpResponse('user ou senha invalida')
        

@login_required(login_url='/accounts/profile/')
def profile(request):
    return render(request, 'profile.html')


@login_required(login_url='/accounts/logout/')
def logout(request):
    return render(request, 'login.html')

 
        
          
