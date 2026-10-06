import pytest
#   se importa la función a probar
from seguridad import comprueba_clave 

# ==============================================================================
# Método 2: conjunto de datos y bucle
# ==============================================================================

# Dataset de datos de prueba: 
#  cada elemento es una tupla (login, password, resultado_esperado)
dataset_pruebas = [
    # --- CASOS VÁLIDOS (Deben devolver True) ---
    ("juan_perez", "ContrasenaValida123", True),
    ("admin_sys", "SistemasOperativos2026", True),
    
    # --- CASOS INVÁLIDOS POR LONGITUD < 10 (Deben devolver False) ---
    ("admin", "", False),
    ("admin", "password", False),
]
# Función de prueba con Bucle y  usando dataset
def test_comprueba_clave_con_bucle():
    # Bucle que recorre el dataset evaluando cada caso
    for login, password, esperado in dataset_pruebas:
        resultado_real = comprueba_clave(login, password)
        # El assert verifica que el resultado devuelto sea igual al esperado.
        # Si no coincide, el mensaje de error personalizado indicará dónde falló.
        assert resultado_real == esperado, f"Fallo en el caso -> Login: '{login}', Password: '{password}'"
