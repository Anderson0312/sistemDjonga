from django.http import HttpResponse
from django.shortcuts import redirect, render
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.template import loader
from django.urls import reverse, reverse_lazy
from django.views.generic import DeleteView

from partners.models import partners

# Create your views here.
@login_required(login_url='')
def viewPartners(request):
    query = request.GET.get('query')

    if query:
        mPartner = partners.objects.filter(name__icontains=query)
    else:
        mPartner = partners.objects.all()
        
    mPartner = partners.objects.all().values()
    context = {
        'partners': mPartner,
    }
    
    template = loader.get_template('partnersview.html')
    
    return HttpResponse(template.render(context, request))


# Create your views here.
@login_required(login_url='')
def create_Partners(request):
    if request.method == "GET":
            return render(request, 'partners.html')         
    else:
        name_empresa = request.POST.get('name_empresa')
        pathbase = request.POST.get('pathbase')
        
        partner = partners.objects.filter(name_empresa=name_empresa).first()
        
        if partner:
            messages.error(request, 'Já existe uma empresa com esse nome cadastrado')
        else:
            messages.success(request, 'Cliente cadastrado com sucesso')
            partner = partners.objects.create(name_empresa=name_empresa, pathbase=pathbase)
            return redirect(reverse('viewPartners'))
        
        
class partner_delete(DeleteView):
    model = partners
    success_url = reverse_lazy('viewPartners')  # substitua pelo nome da sua URL

    
    
        