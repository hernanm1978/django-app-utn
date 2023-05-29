import json
from django.http import HttpResponse


def quitar(request, *args, **kwargs):
    if request.method == "GET":
        print("1111111aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa")
        idproducto = request.GET.get("cada_producto_id")
        valor = request.GET.get("valor")
        carro = request.session.get("carro")
        cantidad = int(valor) - 1
        # ###########################################
        # ACTUALIZO VARIABLE DE SESSION
        # ###########################################
        carro[idproducto] = cantidad
        request.session["carro"] = carro
        print("CARROOOO", request.session["carro"])
        total_carro = sum(carro.values())
        
        request.session["total_carro"] = total_carro
        # ###########################################
        # FIN
        # ###########################################

        print("aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa")
        print(idproducto)
        print(valor)
        print(cantidad)
        print(carro)
        results = []
        data = {}
        data["idproducto"] = str(idproducto)
        data["cantida"] = str(cantidad)
        results.append(data)
        data_json = json.dumps(results)
        mimetype = "application/json"
        return HttpResponse(data_json, mimetype)