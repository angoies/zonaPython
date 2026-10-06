import pytest
from seguridad import comprueba_clave 

# ==============================================================================
# Método 3: pruebas parametrizadas de pytest usando decoradores 
# ==============================================================================

# Pruebas parametrizadas usando decorador 
#  que actua sobre función de test que le sigue
@pytest.mark.parametrize(
    "login, password, resultado_esperado",
    [
        # Válidas
        ("juan_perez", "ContrasenaValida123", True),
        ("admin_sys", "SistemasOperativos2026", True),
        # Inválidas 
        ("admin", "1234", False),
        ("admin", "password", False),
        # ("usuario_con_clave_larga", "clave_larga", False),
    ],
)
# Función (no lleva bucle)
def test_comprueba_clave_parametrizado(login, password, resultado_esperado):
    assert ( 
        comprueba_clave(login, password) == resultado_esperado
    ), f"Fallo en el caso -> Login: '{login}', Password: '{password}'"