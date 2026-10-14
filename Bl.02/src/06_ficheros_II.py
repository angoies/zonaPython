import os

FICHERO = "config.ini"

# 1. Comprobamos ANTES de abrir
if os.path.exists(FICHERO):
    # Si entra aquí, es seguro abrirlo en modo 'r'
    print(f"Éxito: El fichero '{FICHERO}' existe.")
    with open(FICHERO, "r") as f:
        print("Contenido:")
        print(f.read())
else:
    print(f"Error: El fichero '{FICHERO}' no se ha encontrado.")