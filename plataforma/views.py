from django.http import HttpResponse, HttpResponseRedirect

from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login as login_django
from django.template import loader

from plataforma.models import Products

@login_required(login_url='')
def index(request):
    mProducts = Products.objects.all().values()
    mUser = User.objects.all().values()
    
    context = {
        'mProducts': mProducts,
        'mUser': mUser
    }
      

    template = loader.get_template('index.html')
    
    return HttpResponse(template.render(context, request))

@login_required(login_url='')
def profile(request):

    return 

