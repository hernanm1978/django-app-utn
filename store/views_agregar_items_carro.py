import json
from django.http import HttpResponse
from .models import Store


def agregar_items_carro(request, *args, **kwargs):
    if request.method == "GET":
        idproducto = request.GET.get("cada_producto_id")
        valor = request.GET.get("valor")
        carro = request.session.get("carro")
        cantidad = int(valor)
        # ###########################################
        # RECUPERO PRODUCTO PARA LIMITAR STOCK
        # ###########################################
        idproducto_rec = idproducto[8:]
        idproducto_rec = int(idproducto_rec)
        el_prod = Store.objects.get(id=idproducto_rec)
        print(el_prod.stock)
        print("stock")
        stock_actual = int(el_prod.stock)
        if int(valor) >= stock_actual:
            cantidad = int(valor)
        else:
            cantidad = int(valor) + 1
        # ###########################################
        # ACTUALIZO VARIABLE DE SESSION
        # ###########################################
        carro[idproducto] = cantidad
        request.session["carro"] = carro
        # ###########################################
        # FIN
        # ###########################################
        print("bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb")
        results = []
        data = {}
        data["idproducto"] = str(idproducto)
        data["cantidad"] = str(cantidad)
        results.append(data)
        data_json = json.dumps(results)
        mimetype = "application/json"
        return HttpResponse(data_json, mimetype)