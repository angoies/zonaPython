import os

# Prueba a cambiar esto por "config.ini" o una carpeta que tengas
RUTA_A_PROBAR = input("Escribe un nombre de fichero o carpeta: ")

if not os.path.exists(RUTA_A_PROBAR):
    print(f"Error: '{RUTA_A_PROBAR}' NO existe.")
elif os.path.isfile(RUTA_A_PROBAR):
    print(f"Info: '{RUTA_A_PROBAR}' es un FICHERO.")
elif os.path.isdir(RUTA_A_PROBAR):
    print(f"Info: '{RUTA_A_PROBAR}' es un DIRECTORIO.")
else:
    print(f"Info: '{RUTA_A_PROBAR}' existe, pero no es ni fichero ni dir.")