from typing import Any
from django.shortcuts import render
from django.views.generic import View
from store.models import Store
from usuarios.models import Datosusuario
from django.core.exceptions import ObjectDoesNotExist
from django.contrib.sites.models import Site
from django.db.models import Q
from django.contrib import messages
from django.shortcuts import redirect



# Create your views here.


class Carrito(View):

    
    template = "carrito/carrito.html"
    
    def get(self, request):
        
        params = {} 
        
        if "carro" in request.session.keys():
            
              
            ids = list(request.session.get("carro").keys())
            #ids_2 = request.session.get("carro")

            cantidades = list(request.session.get("carro").values())
            
            ids2 = []
                
            for id in ids:
                print("id 8 -->",id[:8])
                print("id 8 -->",id[8:])
                print("id",id)
                if id[:8] == "hmstore_":
                    val = id[8:]
                    val = int(val)

                    ids2.append(val)     
            
                
            # ##########################################################
            # PARA USUARIO
            # ###########################################################
            # user = User.objects.create_user('john', 'lennon@thebeatles.com', 'johnpassword')
            # ##########################################################
            # PARA USUARIO
            # ###########################################################
            art_venta = Store.objects.filter(pk__in=ids2)
            print(art_venta)
            params["los_productos"] = art_venta
            params["las_cantidades"] = [i for i in cantidades]
            print("params", params)
            print("cantidades", cantidades)
            print(ids2)
            # ##########################################################
            # PARA USUARIO
            # ###########################################################
            if request.user.is_authenticated:
                params["usuario"] = request.user
                try:
                    datos_para_imagen = Datosusuario.objects.get(usuario=request.user.pk)
                    params["datos_para_imagen"] = datos_para_imagen
                except ObjectDoesNotExist:
                    print("ObjectDoesNotExist")
                    pass
            # ##########################################################
            # PARA RUTAS EN LINKS
            # ###########################################################
            current_site = Site.objects.get_current()
            params["dominio_actual"] = current_site.domain
            # messages.success(request, 'Producto agregado al carrito')
            
        else:
            print("ACAAAAAAAAAAAAAAAAAAAAAAAA")
            messages.error(request, ' - El carrito esta vacío, por favor volvé a la tienda y selecciona algún producto.')
            return redirect("/store")
        
        return render(request, self.template, params)
     
    
    