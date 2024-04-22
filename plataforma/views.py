from django.http import HttpResponse, HttpResponseRedirect

from django.shortcuts import render

from django.contrib.auth import authenticate
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login as login_django
from django.template import loader


@login_required(login_url='')
def index(request):
    mUser = User.objects.all().values()
    mUserer = User.objects.all().values()
    
    context = {
        'mUser': mUser,
    }
    
    if request.user.is_authenticated:
        user_name = request.user
        print(user_name.email)

    
    template = loader.get_template('index.html')
    
    return HttpResponse(template.render(context, request))

