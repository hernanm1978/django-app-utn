import json
from django.http import HttpResponse
from .models import Store

def agregar_item(request, *args, **kwargs):
    params = {}
    if request.method == "GET":
        idproducto = request.GET.get("cada_producto_id")
        valor = request.GET.get("valor")
        # if valor is None:
        #     print("ACAAAAAAAAAAAAAAAAAAAAAAAAAAAAA")
        #     valor = 1
        print("idddddddddddddddddddddddd",idproducto)
        carro = request.session.get("carro")
        idproducto_rec = idproducto[8:]
        idproducto_rec = int(idproducto_rec)
        el_prod = Store.objects.get(id=idproducto_rec)
        print(el_prod.cantidad_disponible)
        print("valor", valor)
        print(carro)
        stock_actual = int(el_prod.cantidad_disponible)
        cantidad = int(valor)
        if int(valor) >= stock_actual:
            cantidad = int(valor)
        else:
            cantidad = int(valor)
            print("aqui")
            
        print("cantidad -->", cantidad)
        print("valor ----->", valor)
        # ###########################################
        # ACTUALIZO VARIABLE DE SESSION
        # ###########################################

        carro[idproducto] = cantidad
        total_carro = sum(carro.values())
        request.session["carro"] = carro
        request.session["total_carro"] = total_carro
        # ###########################################
        # FIN
        # ###########################################

        results = []
        data = {}
        data["idproducto"] = str(idproducto)
        data["cantidad"] = str(cantidad)
        data["total_carro"] = str(sum(carro.values()))
        results.append(data)
        data_json = json.dumps(results)
        mimetype = "application/json"
        total_carro = sum(carro.values())
        print("Carro", carro)
        print("carro values",carro.values())
        print("ttoal carro", total_carro)
        params["total_carro"] = total_carro
        return HttpResponse(data_json, mimetype)
    