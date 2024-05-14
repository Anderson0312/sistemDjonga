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
        
    dataCollectPrevent()
    
    template = loader.get_template('index.html')
    
    return HttpResponse(template.render(context, request))



def dataCollectPrevent():
        
        planilha = pd.read_excel('relatorio_prevent_senior.xlsx')

        numero_de_linhas = len(planilha)
        totalVenda_prevent = 0
        print(numero_de_linhas)
        # Iterar sobre os IDs e armazená-los em uma variável
        for index, row in planilha.iterrows():
                if numero_de_linhas == 1:
                        print('Planilha de pedido vazia')
                        break
                else:
                        totalVenda_prevent += row['valor']
        print(totalVenda_prevent)
        
        context = {
        'numero_de_linhas': numero_de_linhas,
        'totVendaPrevent': totalVenda_prevent,
        }
        
        template = loader.get_template('index.html')
        
        return HttpResponse(template.render(context))
