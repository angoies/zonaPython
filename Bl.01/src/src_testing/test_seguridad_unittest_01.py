import unittest
# Se importa la función a probar
from seguridad import comprueba_clave

class TestCompruebaClave(unittest.TestCase):

    # 1. Casos VÁLIDOS (deben retornar True)
    def test_clave_valida(self):
        """Clave de más de 10 caracteres que no contiene el login ni está en la lista negra."""
        self.assertTrue(comprueba_clave("usuario123", "ClaveMuySegura2026!"))

    def test_clave_longitud_exacta_10(self):
        """Caso límite: clave con exactamente 10 caracteres."""
        self.assertTrue(comprueba_clave("admin", "1234567890"))

    # 2. Casos INVÁLIDOS (deben retornar False)

    def test_clave_corta_menos_de_10_caracteres(self):
        """Clave con menos de 10 caracteres debe fallar."""
        self.assertFalse(comprueba_clave("usuario", "12345679"))

    def test_clave_prohibida(self):
        """Una clave incluida en la lista de claves prohibidas debe fallar."""
        self.assertFalse(comprueba_clave("usuario", "administrador2026"))

if __name__ == "__main__":
    unittest.main()
