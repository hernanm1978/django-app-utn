import json
from django.http import HttpResponse
from .models import Store

def agregar_item(request, *args, **kwargs):
    params = {}
    if request.method == "GET":
        idproducto = request.GET.get("cada_producto_id")
        valor = request.GET.get("valor")
        carro = request.session.get("carro")
        idproducto_rec = idproducto[8:]
        idproducto_rec = int(idproducto_rec)
        el_prod = Store.objects.get(id=idproducto_rec)
        print(el_prod.cantidad_disponible)
        print("stock")
        print(carro)
        stock_actual = int(el_prod.cantidad_disponible)
        cantidad = 0
        if int(valor) >= stock_actual:
            cantidad = int(valor)

        elif len(carro) > 0:
            if f"hmstore_{idproducto_rec}" in carro.keys():
                cantidad = int(carro[f"hmstore_{idproducto_rec}"]) + int(valor)
                print("aca")
                print(carro)
            else:
                cantidad = int(valor)
                print("aqui")
        else:
            cantidad = int(valor)
            print("por el else abajo")
            # cantidad = int(valor) + 1
            # print("aca estamos")
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