from usuarios.models import Datosusuario
from servicios_board.models import Servicio
import pytest
from django.contrib.auth.models import User
import datetime

# se lo pasamos a las funciones que estan en la carpeta tests
@pytest.fixture()
def crear_nuevo_servicio_fixture(db):
    mi_servicio = Servicio(servicio = "Reparaciones Varias", fecha_ingreso = datetime.datetime.now())
    mi_servicio.save()

    return mi_servicio