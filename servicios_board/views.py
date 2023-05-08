from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect, HttpResponseForbidden
from django.shortcuts import render
from .models import Servicio
import time
from store.views import index as fff

# Create your views here.

def index2(request):
    return HttpResponse("Prueba del sitio")


def test(request):

    params = {}
    params['nombre_sitio'] = 'Sistema de administracion de servicios'

    params['lista'] = str(list(range(10)))

    return render(request, 'servicios_board/test.html', params)

# def administracion_servicios(request):

#     # params = {}
#     # params["nombre_sitio"] = "Vista o index de Pagina principal del sitio"
#     # params['lista'] = "Una prueba par mandar algo desde views.py, va una lista: " + str(list(range(10)))
#     # return render(request, 'servicios_board/index.html', params)
#     params = {}
#     params["site_name"] = "HM-NET Services"
#     params["page_title"] = "Administrador de Servicios"
#     params['servicios'] = Servicio.objects.all()
#     params['cantidad_total'] = Servicio.objects.count()
#     if request.user.is_authenticated:
#         return render(request, 'servicios_board/administracion_servicios.html', params)

#     else:
#         try:
#             return HttpResponseRedirect("/accounts/login/")
            
#         except:
#             return HttpResponse("salio mal")
#         # finally:
#         #     return HttpResponseRedirect("/accounts/login/")


def administracion_servicios(request):

    # params = {}
    # params["nombre_sitio"] = "Vista o index de Pagina principal del sitio"
    # params['lista'] = "Una prueba par mandar algo desde views.py, va una lista: " + str(list(range(10)))
    # return render(request, 'servicios_board/index.html', params)
    params = {}
    params["site_name"] = "HM-NET Services"
    params["page_title"] = "Administrador de Servicios"
    params['servicios'] = Servicio.objects.all()
    params['cantidad_total'] = Servicio.objects.count()
    if request.user.is_authenticated and request.user.is_staff:
        return render(request, 'servicios_board/administracion_servicios_staff.html', params)
    
    elif request.user.is_authenticated:
        return render(request, 'servicios_board/administracion_servicios.html', params)
    
    else:
        try:
            return HttpResponseRedirect("/accounts/login/")
            
        except:
            return HttpResponse("salio mal")
        # finally:
        #     return HttpResponseRedirect("/accounts/login/")

        

def index(request):

    # params = {}
    # params["nombre_sitio"] = "Vista o index de Pagina principal del sitio"
    # params['lista'] = "Una prueba par mandar algo desde views.py, va una lista: " + str(list(range(10)))
    # return render(request, 'servicios_board/index.html', params)
    params = {}
    params["site_name"] = "HM-NET Services"
    params["page_title"] = "Home"
    params['servicios'] = Servicio.objects.all()
    params['cantidad_total'] = Servicio.objects.count()


    return render(request, 'servicios_board/index.html', params)

def recuperacion_datos(request):

    params = {}
    params["site_name"] = "HM-NET Services"
    params["page_title"] = "Recuperacion De Datos"
    return render(request, 'servicios_board/recupero_datos.html', params)

def electronics(request):

    params = {}
    params["site_name"] = "HM-NET Services"
    params["page_title"] = "Electronics"
    return render(request, 'servicios_board/electronics.html', params)

def dev(request):

    params = {}
    params["site_name"] = "HM-NET Services"
    params["page_title"] = "DEV"
    return render(request, 'servicios_board/dev.html', params)

def nosotros(request):

    params = {}
    params["site_name"] = "HM-NET Services"
    params["page_title"] = "Sobre Nosotros"
    return render(request, 'servicios_board/nosotros.html', params)

def alta_servicio(request):
    servicio = request.POST["servicio_txt"]
    dispositivo = request.POST["dispositivo_txt"]
    descripcion = request.POST["descr_txt"]
    descripcion_servicio = request.POST["descr_servicio_txt"]
    cliente = request.POST["cliente_txt"]
    telefono = request.POST["telefono_txt"]
    email = request.POST["email_txt"]
    estado = request.POST["estado_txt"]
    fecha_ingreso = request.POST["fecha_ingreso_txt"]
    valor_presupuesto = request.POST["valor_presupuesto_txt"]
    fecha_presupuesto = request.POST["fecha_presupuesto_txt"]
    entrega_estimada = request.POST["fecha_entrega_txt"]
    imagen = request.POST["imagen_txt"]

    if fecha_presupuesto == "":
        fecha_presupuesto = "0001-01-01"
    if entrega_estimada == "":
        entrega_estimada = "0001-01-01"
        
    alta_nuevo_servicio = Servicio.objects.create(
        servicio=servicio, dispositivo=dispositivo, descripcion=descripcion, 
        descripcion_servicio=descripcion_servicio, cliente=cliente, 
        telefono=telefono, email=email, estado_actual=estado, 
        fecha_ingreso=fecha_ingreso, valor_presupuestado1=valor_presupuesto,
        fecha_presupuesto=fecha_presupuesto, entrega_estimada=entrega_estimada,
        imagen=imagen
        )
    return redirect("/administracion_servicios/")