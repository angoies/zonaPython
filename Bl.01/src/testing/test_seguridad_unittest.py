import unittest

# El nombre del fichero seguridad.py es el nombre del módulo
# Se importa la función a probar
from seguridad import comprueba_clave


class TestCompruebaClave(unittest.TestCase):

    # ==============================================================================
    # 1. Casos VÁLIDOS (deben retornar True)
    # ==============================================================================

    def test_clave_valida(self):
        """Clave de más de 10 caracteres que no contiene el login ni está en la lista negra."""
        self.assertTrue(comprueba_clave("usuario123", "ClaveMuySegura2026!"))

    def test_clave_longitud_exacta_10(self):
        """Caso límite: clave con exactamente 10 caracteres."""
        self.assertTrue(comprueba_clave("admin", "1234567890"))

    # ==============================================================================
    # 2. Casos INVÁLIDOS (deben retornar False)
    # ==============================================================================

    def test_clave_corta_menos_de_10_caracteres(self):
        """Clave con menos de 10 caracteres debe fallar."""
        self.assertFalse(comprueba_clave("usuario", "12345679"))

    def test_clave_prohibida(self):
        """Una clave incluida en la lista de claves prohibidas debe fallar."""
        self.assertFalse(comprueba_clave("usuario", "administrador2026"))

    def test_clave_contiene_login(self):
        """Si el login aparece dentro de la clave, debe fallar."""
        self.assertFalse(comprueba_clave("alumno", "alumno1234567890"))

    def test_clave_igual_al_login(self):
        """Si la clave es exactamente igual al login y tiene longitud suficiente, debe fallar."""
        login_largo = "usuario_muy_largo_123"
        self.assertFalse(comprueba_clave(login_largo, login_largo))

    # ==============================================================================
    # 3. Otra forma: dataset usando subTest
    # ==============================================================================

    def test_comprueba_clave_con_dataset(self):
        """Prueba varios casos mediante un dataset y subTest de unittest."""
        dataset_pruebas = [
            # --- CASOS VÁLIDOS (Deben devolver True) ---
            ("juan_perez", "ContrasenaValida123", True),
            ("admin_sys", "SistemasOperativos2026", True),

            # --- CASOS INVÁLIDOS POR LONGITUD < 10 (Deben devolver False) ---
            ("admin", "", False),
            ("admin", "1234", False),
            ("admin", "password", False),
            ("admin", "123456789", False),

            # --- CASOS INVÁLIDOS POR SER CLAVES PROHIBIDAS ---
            ("admin", "123456789012", False),
            ("admin", "password12345", False),
            ("admin", "administrador2026", False),

            # --- CASOS INVÁLIDOS POR CONTENER EL LOGIN EN EL PASSWORD ---
            ("alumno", "alumno1234567890", False),
            ("usuario", "ClaveusuarioSegura2026", False),
        ]

        for login, password, esperado in dataset_pruebas:
            with self.subTest(login=login, password=password):
                resultado_real = comprueba_clave(login, password)
                self.assertEqual(
                    resultado_real,
                    esperado,
                    f"Fallo en el caso -> Login: '{login}', Password: '{password}'"
                )


if __name__ == "__main__":
    unittest.main()
