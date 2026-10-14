import os

# El '.' significa 'esta misma carpeta donde se ejecuta el script'
RUTA = "."
# RUTA = input("Escribe un nombre de carpeta: ")

print(f"Contenido de la carpeta '{RUTA}':")

try:
    lista_de_ficheros = os.listdir(RUTA)
    print(type(lista_de_ficheros), lista_de_ficheros)
    # lista_de_ficheros.sort()s

    for nombre_fichero in lista_de_ficheros:
        print(f"- {nombre_fichero}")

except FileNotFoundError:
    print(f"Error: El directorio '{RUTA}' no existe.")
except NotADirectoryError:
    print(f"Error: '{RUTA}' es un fichero, no un directorio.")
