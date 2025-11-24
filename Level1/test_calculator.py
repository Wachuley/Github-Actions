import pytest
from calculator import divide

def test_divide_basic():
    #Prueba de lógica
    assert divide(10, 2) == 5

def test_divide_zero():
    try:
        resultado = divide(10, 0)
        assert resultado is None
    except ZeroDivisionError:
        pytest.fail()