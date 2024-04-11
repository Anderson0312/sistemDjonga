
from django.http import HttpResponse, HttpResponseRedirect

from.models import Products

from django.template import loader

def index(request):

    mProducts = Products.objects.all().values()
    
    context = {
        'mProducts': mProducts
    }
    
    template = loader.get_template('index.html')
    
    return HttpResponse(template.render(context, request))




