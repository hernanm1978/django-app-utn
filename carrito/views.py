from django.shortcuts import render
from django.views.generic import View
from store.models import Store
from usuarios.models import Datosusuario
from django.core.exceptions import ObjectDoesNotExist
from django.contrib.sites.models import Site
from django.db.models import Q



# Create your views here.


class Carrito(View):
    template = "carrito/carrito.html"

    def get(self, request):
        params = {}   
        ids = list(request.session.get("carro").keys())
        ids2 = []

        for id in ids:
            print(id[:8])
            if id[:8] == "hmstore":
                val = id[9:]
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
        return render(request, self.template, params)