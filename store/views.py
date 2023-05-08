from django.shortcuts import render, redirect
from django.http import Http404
from django.http import HttpResponse
from .models import Store
from django.views.generic import View
from django.db.models import Q
from store.forms import BuscarProductoForm
import json
from django.contrib.auth.decorators import login_required


# Create your views here.


def index2(request):

    return HttpResponse("Store en construccion!!")

def index(request):
    params = {}
    params["site_name"] = "HM-NET Services"
    params["page_title"] = "Store"
    params['lista'] = "Una prueba par mandar algo desde views.py, va una lista: " + str(list(range(10)))
    params['productos_store'] = Store.objects.filter(Q(estado_actual="Publicado"))
    params['cantidad_total'] = Store.objects.count()
    #params["total_carro"] = ""
    temp = request.session.get("seleccion_productos")
    if "total_carro" in request.session:
        params["total_carro"] = request.session["total_carro"]
        return render(request, 'store/index.html', params)

    else:
        params["total_carro"] = 0
        print("temp",temp)
        return render(request, 'store/index.html', params)



def ver_imagen(request, producto_id):
    params={}
    try:
        producto = Store.objects.get(pk=producto_id)
    except producto.DoesNotExist:
        raise Http404
    params["producto"] = producto
    
    return render(request, "store/ver-producto.html", params)


class VerProducto(View):
    
    template = "store/ver-producto.html"
    
    
    def get(self, request, producto_id):
        
        params = {}
        producto = Store.objects.get(pk=producto_id)
        params['cantidad_total'] = Store.objects.count()
        params["producto"] = producto
        params["total_carro"] = ""
        temp = request.session.get("seleccion_productos")
        if temp:
            params["total_carro"] = request.session["total_carro"]
            
        return render(request, self.template, params)
    
    def post(self, request, producto_id):
        
        params = {}
        producto = request.POST.get("producto-seleccionado")
        seleccion_productos = request.session.get("seleccion_productos")
        #print(seleccion_productos)
        
        if seleccion_productos:
            cantidad = seleccion_productos.get(producto)
            
            if cantidad :
                seleccion_productos[producto] = cantidad + 1
            
            else:
                seleccion_productos[producto] = 1
        
        else:
            seleccion_productos = {}
            seleccion_productos[producto] = 1
            
        request.session["seleccion_productos"] = seleccion_productos
        total_carro = sum(seleccion_productos.values())
        request.session["total_carro"] = total_carro
        print(seleccion_productos)
        
        return redirect("/store/")


class VerProductoLs(View): 
    
    template = "store/ver-producto-ls.html"

    def get(self, request, producto_id):
        params={}
        try:
            producto = Store.objects.get(pk=producto_id)
        except Store.DoesNotExist:
            raise Http404
        params["producto"] = producto
        # ##########################################################
        # PARA INICIALIZAR LA VARIABLE DE SESSION CARRO
        # ###########################################################
        try:
            request.session["carro"]
            # request.session["total_carro"]
        except:
            request.session["carro"] = {}
            # request.session["total_carro"] = {}
        print("CARRO:", request.session["carro"])
        total_carro = sum(request.session["carro"].values())
        params["total_carro"] = total_carro
        print(params["producto"])    
        print("TOTALLLL CARRO", total_carro)
        return render(request, self.template, params)


# -----------------------------------------------------------------------------------------------
    #La clase barra_busqueda_ajax(request): tiene como url busqueda_ajax 
    #(no confundir con busqueda_ajax.html !!) al llamar a esta url definida en urls.py del store
    #llama al form BuscarProductoForm().
    #La clase BuscarProducto hace la consulta a la db apartir de los datos que 
    # vienen de la busqueda del form de busqueda_ajax.html, el js toma los datos 
    # con autocomplete, para el auto complete llama a la claseBuscarProducto quien 
    # hace la consulta a la db y devuelve los resultados en un json.dump que es lo 
    # que se muestra como resultados de busqueda, al hacer click en alguna de las 
    # opciones de busqueda que trae y al hacer click en el boton "ver datos" 
    # con id id="boton_prod" , llama y ejecuta la funcion onclick del static/js/ajax.js;
    # y el ajax llama a la clase BuscarProducto2 a travez de su url
    # (buscarproducto2, ver urls.py de store) quien le pasa la query a hacer por 
    # el prod seleccionado, la clase la hace, el ajax toma los resultados y se los pasa al 
    # html en el div contenedor_filtrado. Estoy casi segureo es asi pero chequear
    #
# -----------------------------------------------------------------------------------------------


def barra_busqueda_ajax(request):
    
    params = {}
    busqueda = BuscarProductoForm()
    params['busqueda'] = busqueda
    return render(request, 'store/busqueda_ajax.html', params)


class BuscarProducto(View):

    def get(self, request):
        if request.is_ajax:
            palabra_input = request.GET.get('term','')
            print("palabra innnnnnput",palabra_input)
            producto_ = Store.objects.filter(producto__icontains = palabra_input)
            resultado = []
            for i in producto_:
                data = {}
                data["label"] = i.producto
                resultado.append(data)
            data_json = json.dumps(resultado)
        else:
            data_json = "Error!"
        mimetype = "application/json"
        print("DDDATA JSONN",data_json)
        return HttpResponse(data_json, mimetype)
    
class BuscarProducto2(View):

    def get(self, request):
        print("hola")
        if request.is_ajax:
            q = request.GET['valor']

            print("111>>>>>>>>>>>> ", q)
            producto_ = Store.objects.filter(producto__icontains=q)
            print("222>>>>>>>>>>>> ",producto_)
            results = []
            for i in producto_:
                print(i.producto)
                print(i.estado_actual)
                print(i.imagen)


                data = {}
                data['producto'] = i.producto
                data['estado'] = i.estado_actual
                data['ruta_imagen'] = str(i.imagen)
                results.append(data)
          

            print("333>>>>>>>>>>>> ",results)
 
            data_json = json.dumps(results)
            mimetype = "application/json"
            return HttpResponse(data_json, mimetype)

    