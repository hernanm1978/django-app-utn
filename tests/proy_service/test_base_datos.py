from usuarios.models import Datosusuario
from servicios_board.models import Servicio
import pytest
from django.contrib.auth.models import User
import datetime


@pytest.mark.django_db
def test_crear_nuevo_usuario():
    mi_usuario = Datosusuario(nombre = "cliente_nombre")
    mi_usuario.save()
    print(mi_usuario.nombre)
    assert mi_usuario.nombre == "cliente_nombre"

@pytest.mark.django_db
def test_crear_nuevo_cliente():
    mi_servicio = Servicio(cliente = "un nuevo cliente", fecha_ingreso = datetime.datetime.now())
    mi_servicio.save()
    print(mi_servicio.cliente)
    assert mi_servicio.cliente == "un nuevo cliente"

@pytest.mark.django_db
def test_crear_nuevo_servicio():
    mi_servicio = Servicio(servicio = "Recupero De Datos", fecha_ingreso = datetime.datetime.now())
    mi_servicio.save()
    print(mi_servicio.servicio)
    assert mi_servicio.servicio == "Recupero De Datos"

# pasamos a la funcion desde los fixtures que estan en conftest.py
@pytest.mark.django_db
def test_crear_nuevo_servicio_fixture(crear_nuevo_servicio_fixture):
    # mi_servicio = Servicio(servicio = "Recupero De Datos", fecha_ingreso = datetime.datetime.now())
    # mi_servicio.save()
    print(crear_nuevo_servicio_fixture.servicio)
    assert crear_nuevo_servicio_fixture.servicio == "Reparaciones Varias"