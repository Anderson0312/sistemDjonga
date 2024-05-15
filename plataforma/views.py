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
    
    quantAssociations = dataCollectPrevent()[0]
    
    totVenda = dataCollectPrevent()[1]
    
    quantPartners = dataCollectPrevent()[2]
    
    medLifePartners = quantAssociations / quantPartners
    
    context = {
        'mUser': mUser,
        'numero_de_linhas': quantAssociations,
        'totVendaPrevent': totVenda,
        'quantPartners':quantPartners,
        'medLifePartners':medLifePartners,
    }

    
    template = loader.get_template('index.html')
    
    return HttpResponse(template.render(context, request))



def dataCollectPrevent():
        
        planilhaPrevent = pd.read_excel('baseDados/relatorio_prevent_senior.xlsx')

        numero_de_linhas = len(planilhaPrevent)
        totalVenda_prevent = 0
        cont = 1

        # Iterar sobre os IDs e armazená-los em uma variável
        for index, row in planilhaPrevent.iterrows():
                if numero_de_linhas == 1:
                        print('Planilha de pedido vazia')
                        break
                else:
                        totalVenda_prevent += row['valor']    
        
        return numero_de_linhas, totalVenda_prevent, cont
