from django.http import HttpResponse, HttpResponseRedirect

from django.shortcuts import render

from django.contrib.auth import authenticate
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login as login_django
from django.template import loader
import pandas as pd


@login_required(login_url='')
def index(request):
    mUser = User.objects.all().values()
    
    context = {
        'mUser': mUser,
    }
    
    # if request.user.is_authenticated:
    #     user_name = request.user
    #     print(user_name.email)
        
    planilha = pd.read_excel('relatorio_prevent_senior.xlsx')
        
    print(planilha.head())  # Exibe as primeiras linhas   
    
    
    template = loader.get_template('index.html')
    
    return HttpResponse(template.render(context, request))



def dataCollectPrevent():
        
        planilha = pd.read_excel('relatorio_prevent_senior.xlsx')

        # Agora você pode manipular os dados no DataFrame 'df'
        print(planilha.head())  # Exibe as primeiras linhas
