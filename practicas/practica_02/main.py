import funciones as f 
from productos import LISTA_dummy, PRODUCTOS_EJEMPLO


lista = f.obtener_productos() # usando la API
# lista =  LISTA_dummy        # si no usa la API

print(lista)
# f.mostrar_productos(lista)
