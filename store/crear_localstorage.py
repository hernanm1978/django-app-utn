from django.shortcuts import render
from django.shortcuts import redirect
#from productos.models.categoria import Categoria
from django.contrib.auth.models import User
import json
from django.http import HttpResponse
import ast

# from .models.cliente import Cliente
from store.models import Store
from django.db.models import Q
from django.views.generic import View
from django.http import HttpResponseRedirect


def crear_localstorage(request, *args, **kwargs):
    if request.method == "GET":
        person = request.GET
        """ ######################################
        # CONVERTIR FORMATO DE JSON A DICCIONARIO
        # Y GUARDAR EN VARIABLE DE SESSION
        ##########################################"""
        producto_formato_diccionario = person.dict()
        producto_dict = ast.literal_eval(producto_formato_diccionario["producto"])
        print("essstoooo", producto_dict)
        
        # Hago esto por que, 1 se me mete en el ast la clave valor del recaptcha y me rompe el 
        # contador del carrito y 2 los values del dic del ast vienen en str y luego la app al querer calcular
        # el total del carrito con sum se rompe la app por que los argumentos de sum vienen en int y str
        
        mi_dic = {}
        for k, v in producto_dict.items():
            if str(k).startswith("hmstore"):
                mi_dic[f"{k}"] = int(v)
            else:
                continue
            
        request.session["carro"] = mi_dic#producto_dict
        request.session["total_carro"] = sum(request.session["carro"].values())
        request.session.modified = True
        
        results = []
        data = {}
        data_json = json.dumps(results)
        mimetype = "application/json"
        return HttpResponse(data_json, mimetype)