# Estos tests los corremos con pytest desde /proy_service/proy_service/pytest
import pytest

def test_prueba():
    assert 1 == 1


@pytest.mark.skip(reason="Probando skipear un test")
def test_prueba2():
    assert 1 == 1


# Agregamos una marca propia, la cual debe estar en pytest.ini
@pytest.mark.marca1
def test_prueba3():
    assert 1 == 1


@pytest.fixture  # se pude usar yield ver videos clase
def fixture_1():
    print("desde mi fixture")
    return 1

@pytest.mark.marca1
def test_prueba4(fixture_1):
    variable = fixture_1
    print("desde mi test_prueba4")
    assert variable == 1
