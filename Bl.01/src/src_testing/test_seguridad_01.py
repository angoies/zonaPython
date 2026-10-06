import pytest
#   se importa la función a probar
from seguridad import comprueba_clave 

# ==============================================================================
# Método 1: cada test una función
# ==============================================================================

# Casos VÁLIDOS (deben retornar True)
def test_clave_valida():
    """Clave de más de 10 caracteres que no está en el login ni en la lista negra."""
    assert comprueba_clave("usuario123", "ClaveMuySegura2026!") is True
def test_clave_longitud_exacta_10():
    """Caso límite: Clave con exactamente 10 caracteres."""
    assert comprueba_clave("admin", "1234567890") is True

# 2. Casos INVÁLIDOS (deben retornar False)
def test_clave_corta_menos_de_10_caracteres():
    """Clave con menos de 10 caracteres debe fallar."""
    assert comprueba_clave("usuario", "12345679") is False
def test_clave_contenido_en_login():
    """Si la clave está contenida en el login, debe fallar."""
    login = "alumno"
    password = "alu"  # Longitud > 10 y está dentro del login
    assert comprueba_clave(login, password) is False

