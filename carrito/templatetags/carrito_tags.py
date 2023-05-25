from django import template
from store.models import Store
from django.db.models import Q
from django.shortcuts import redirect


register = template.Library()


@register.filter(name="carrito_cantidad_producto")
def carrito_cantidad_producto(producto, carro):
    
    keys = carro.keys()
    for id in keys:
        
        prod = "hmstore_" + str(producto.id)
        if id == prod:
            return carro.get(id)
    
    return 0


# @register.filter(name="carrito_eliminar_producto")
# def carrito_eliminar_producto(producto, carro):
    
#     keys = carro.keys()
#     for id in keys:
        
#         prod = "hmstore_" + str(producto.id)
#         if id == prod:
#             del carro[prod]
#             return redirect("/")
    
#     return 0



@register.filter(name="preciototal_item")
def preciototal_item(producto, carro):
    
    total_item = int(carrito_cantidad_producto(producto, carro)) * producto.precio
    
    res = "{0:.1f}".format(total_item)
    
    return float(res)



@register.filter(name="subtotal_compra")
def subtotal_compra(productos, carro):
    
    suma = 0
        
    for i in productos:
        suma += preciototal_item(i, carro)
    
    res = "{0:.1f}".format(suma)
    
    return float(res)