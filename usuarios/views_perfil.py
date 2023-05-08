from django.shortcuts import render
from django.http import HttpRequest
from django.http import HttpResponse, HttpResponseRedirect
import time
# Create your views here.


def index(request):
    if request.user.is_authenticated:
        
        return HttpResponseRedirect("/")

    else:
        return HttpResponse("Usuario No Autenticado")


# def no_aut(request):
#     return HttpResponse("Usuario No Autenticado")

def test(request):
    if request.user.is_authenticated:

        return HttpResponse("Usuario Autenticado")
    else:
        return HttpResponse("Usuario No Autenticado")