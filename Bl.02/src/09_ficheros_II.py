import os

RUTA = "."
print(f"Buscando ficheros .txt en '{RUTA}'...")
num_txt = 0

for nombre_fichero in os.listdir(RUTA):

    # os.listdir() devuelve el nombre de cada elemento del directorio.
    # Con os.path.join() construimos su ruta completa para poder
    # realizar operaciones sobre él.
    ruta_completa = os.path.join(RUTA, nombre_fichero)

    # Condición 1: ¿Es un fichero?
    # Condición 2: ¿Termina en ".txt"?
    if os.path.isfile(ruta_completa) and nombre_fichero.endswith(".txt"):
        print(f" -> Encontrado: {nombre_fichero}")
        num_txt += 1

print(f"\nTotal de ficheros .txt encontrados: {num_txt}")