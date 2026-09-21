import os

# Función sin parámetros
def imprime_separador_simple():
    print("-"*25)

imprime_separador_simple()
imprime_separador_simple()

# Función con un parámetro
def imprime_separador(longitud):
    print("-"*longitud)

# Invocaciones con diferentes expresiones
imprime_separador(5)
imprime_separador(10)
tam = 15
imprime_separador(tam)
imprime_separador(tam*2)

# Función con dos parámetros
def imprime_linea(letra, longitud):
    print(letra*longitud)

# Invocaciones posicionales con diferentes valores
imprime_linea("*", 5)
imprime_linea("#", tam)

# Invocación con nombres, puede cambiar el orden
imprime_linea(longitud=10, letra="&")

# test
# res = imprime_linea("+",10)
# print(res)

def imprime_cabecera(titulo):
    imprime_linea("+",10)
    print(titulo)
    imprime_linea("-",10)

imprime_cabecera("Latencias")

# def imprime_lista(lista):
#     for i in range(len(lista)):
#         print(i, "-", lista[i])

# latencias = [12.5, 0.25, 0.67, 1.35]
# imprime_cabecera("Latencias")
# imprime_lista(latencias)