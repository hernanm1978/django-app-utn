from django.shortcuts import render, redirect
from django.contrib.auth import logout

def pagina_logout(request):
    params = {}
    logout(request)
    return render(request, "usuarios/logout.html")

