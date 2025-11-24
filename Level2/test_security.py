import pytest
from security import validar_password

def test_too_short():
    # Regla 1: Debe tener al menos 8 caracteres
    assert validar_password("short") is False

def test_no_numbers():
    # Regla 2: Debe tener al menos un número
    assert validar_password("NoNumbersHere") is False

def test_no_uppercase():
    # Regla 3: Debe tener al menos una mayúscula
    assert validar_password("alllowercase1") is False

def test_common_password():
    # Regla 4: No puede ser una contraseña común
    assert validar_password("password123") is False

def test_valid_password():
    # Ejemplo válido
    assert validar_password("StrongPass123!") is True
