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
    
    VendaConfirma =round(dataCollectPrevent()[2],3)
    
    quantPartners = dataCollectPrevent()[4]
    
    contratoConfi = dataCollectPrevent()[3]
    
    contratoPende = dataCollectPrevent()[5]
    
    totalVendaPrev_prevent = dataCollectPrevent()[1]
    
    medLifePartners = quantAssociations / quantPartners

    
    context = {
        'mUser': mUser,
        'numero_de_linhas': quantAssociations,
        'totVendaPrevent': VendaConfirma,
        'quantPartners':quantPartners,
        'medLifePartners':medLifePartners,
        "contratoConfi":contratoConfi,
        "contratoPende":contratoPende,
        "totalVendaPrev_prevent": totalVendaPrev_prevent,
    }

    
    template = loader.get_template('index.html')
    
    return HttpResponse(template.render(context, request))



def dataCollectPrevent():
        
        planilhaPrevent = pd.read_excel('baseDados/relatorio_prevent_senior.xlsx')

        numero_de_linhas = len(planilhaPrevent)
        totalVendaPrev_prevent = 0
        totalVendaConfir_prevent = 0
        contratoConfi = 0
        cont = 1
        contratoPende = 0

        # Iterar sobre os IDs e armazená-los em uma variável
        for index, row in planilhaPrevent.iterrows():
                if numero_de_linhas == 1:
                        print('Planilha de pedido vazia')
                        break
                else:
                        totalVendaPrev_prevent += row['valor']   
                        if row['status']  == 'Sim':
                                contratoConfi +=1 
                                totalVendaConfir_prevent += row['valor']
                        else:
                               contratoPende +=1  
        
        return numero_de_linhas, totalVendaPrev_prevent, totalVendaConfir_prevent, contratoConfi, cont, contratoPende
