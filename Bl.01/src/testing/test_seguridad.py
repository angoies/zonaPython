import pytest

# El nombre del fichero seguridad.py es el nombre del módulo
#   se importa la función a probar
from seguridad import comprueba_clave 

# ==============================================================================
# 1. Casos VÁLIDOS (deben retornar True)
# ==============================================================================

def test_clave_valida():
    """Clave de más de 10 caracteres que no está en el login ni en la lista negra."""
    assert comprueba_clave("usuario123", "ClaveMuySegura2026!") is True

# def test_clave_longitud_exacta_10():
#     """Caso límite: Clave con exactamente 10 caracteres."""
#     assert comprueba_clave("admin", "1234567890") is True

# ==============================================================================
# 2. Casos INVÁLIDOS (deben retornar False)
# ==============================================================================
def test_clave_corta_menos_de_10_caracteres():
    """Clave con menos de 10 caracteres debe fallar."""
    assert comprueba_clave("usuario", "12345679") is False

# def test_clave_contenido_en_login():
#     """Si la clave está contenida en el login, debe fallar."""
#     login = "alumno"
#     password = "alu"  # Longitud > 10 y está dentro del login
#     assert comprueba_clave(login, password) is False

# def test_clave_igual_al_login():
#     """Si la clave es exactamente igual al login (y mide >= 10 caracteres)."""
#     login_largo = "usuario_muy_largo_123"
#     assert comprueba_clave(login_largo, login_largo) is False


### Otra forma: dataset

# # 2. Función de prueba para Pytest usando un Bucle y un Dataset
# def test_comprueba_clave_con_bucle():
#     # Dataset de datos de prueba: cada elemento es una tupla (login, password, resultado_esperado)
#     dataset_pruebas = [
#         # --- CASOS VÁLIDOS (Deben devolver True) ---
#         ("juan_perez", "ContrasenaValida123", True),
#         ("admin_sys", "SistemasOperativos2026", True),
        
#         # --- CASOS INVÁLIDOS POR LONGITUD < 10 (Deben devolver False) ---
#         ("admin", "", False),
#         ("admin", "1234", False),
#         ("admin", "password", False),
#         ("admin", "123456789", False),  # 9 caracteres
        
#         # --- CASOS INVÁLIDOS POR CONTENER EL PASSWORD EN EL LOGIN (Deben devolver False) ---
#         ("usuario_con_clave_larga", "clave_larga", False),
#         ("mi_super_password_secreta", "password_secreta", False)
#     ]

#     # Bucle que recorre el dataset evaluando cada caso
#     for login, password, esperado in dataset_pruebas:
#         resultado_real = comprueba_clave(login, password)
        
#         # El assert verifica que el resultado devuelto sea igual al esperado.
#         # Si no coincide, el mensaje de error personalizado indicará dónde falló.
#         assert resultado_real == esperado, f"Fallo en el caso -> Login: '{login}', Password: '{password}'"


### U otra forma, usando decoradores y funcionalidades de pytest
# ==============================================================================
# 3. Pruebas parametrizadas (múltiples casos organizados)
# ==============================================================================


# @pytest.mark.parametrize(
#     "login, password, resultado_esperado",
#     [
#         # Válidas
#         ("juan_perez", "ContrasenaValida123", True),
#         ("admin_sys", "SistemasOperativos2026", True),
#         # Inválidas por longitud (< 10)
#         ("admin", "", False),
#         ("admin", "1234", False),
#         ("admin", "password", False),
#         ("admin", "123456789", False),
#         # Inválidas por inclusión en el login
#         ("usuario_con_clave_larga", "clave_larga", False),
#     ],
# )
# def test_comprueba_clave_parametrizado(login, password, resultado_esperado):
#     assert comprueba_clave(login, password) == resultado_esperado