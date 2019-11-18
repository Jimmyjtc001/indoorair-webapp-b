from django.http import HttpResponse, JsonResponse
from django.shortcuts import render

# Create your views here.
def index_page(request):

    context = {
        'login' : 11111,

    }

    return render(request, 'homepage/index.html', context)

def login(request):


    context = {
        'login' :77777,

    }

    return render(request, 'gateway/login.html', context)

def register(request):


    context = {
        'register' :55555,

    }

    return render(request, 'gateway/register.html', context)



def contact_page(request):


    context = {
        'contact' : 222222,

    }

    return render(request, 'homepage/contact.html', context)



def post_version_api(request):
    return JsonResponse({
    'version': 33333,
    })
