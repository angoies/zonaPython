import requests

# URL de la API
URL_PRODUCTOS = "https://dummyjson.com/products"

def obtener_productos(limite=10, skip=10):
    """Consulta DummyJSON y devuelve la lista 'products'.

    Propaga RequestException si falla HTTP o la conexión y ValueError si
    la respuesta no contiene la estructura esperada.
    """
    if not isinstance(limite, int) or isinstance(limite, bool) or limite <= 0:
        raise ValueError("El límite debe ser un entero positivo")

    respuesta = requests.get(
        URL_PRODUCTOS,
        params={"limit": limite, "skip": skip},
        timeout=10,
    )
    respuesta.raise_for_status()  #  Si error (400 a 599), excepción HTTPError; si ok devuelve None.
    datos = respuesta.json()

    if not isinstance(datos, dict) or not isinstance(datos.get("products"), list):
        raise ValueError("Respuesta inesperada: falta la lista 'products'")

    return datos["products"]

def mostrar_productos(productos):
    """Imprime un listado compacto sin alterar los datos."""
    pass