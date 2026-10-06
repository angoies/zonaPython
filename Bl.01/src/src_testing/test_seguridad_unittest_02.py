import unittest
from seguridad import comprueba_clave

class TestCompruebaClave(unittest.TestCase):

    def test_varios_casos(self):
        dataset = [
            (
                "juan_perez",
                "ContrasenaValida123",
                True
            ),
            ("admin", "1234", True),
            ("usuario", "password12345", False),
        ]

        for login, password, esperado in dataset:
            with self.subTest(
                login=login,
                password=password
            ):
                resultado = comprueba_clave(
                    login,
                    password
                )
                self.assertEqual(resultado, esperado)


if __name__ == "__main__":
    unittest.main()