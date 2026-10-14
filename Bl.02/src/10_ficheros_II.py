import os

CARPETA_LOGS = "logs"
RUTA_ACTUAL = "."

# 1. Crear la carpeta 'logs' si no existe
if not os.path.exists(CARPETA_LOGS):
    print(f"Creando carpeta '{CARPETA_LOGS}'...")
    os.mkdir(CARPETA_LOGS)
else:
    print(f"La carpeta '{CARPETA_LOGS}' ya existe.")

# 2. Buscar ficheros .log y moverlos
print("Buscando ficheros .log para mover...")
for nombre_fichero in os.listdir(RUTA_ACTUAL):

    # Comprobamos que sea un fichero y termine en .log
    ruta_antigua = nombre_fichero
    if os.path.isfile(ruta_antigua) and nombre_fichero.endswith(".log"):

        ruta_nueva = os.path.join(CARPETA_LOGS, nombre_fichero)
        try:
            os.rename(ruta_antigua, ruta_nueva)
            print(f" -> Moviendo '{ruta_antigua}' a '{ruta_nueva}'")

        except Exception as e:
            print(f"Error moviendo '{nombre_fichero}': {e}")

print("Organización completada.")