import os

# # Método sin argumentos: 
# # Se invoca dejando los paréntesis vacíos
# directorio_actual = os.getcwd()
# print(f"El script se está ejecutando desde: {directorio_actual}")

# # Método con argumento obligatorio:
# # Definimos el argumento: el nombre de la carpeta que queremos crear
# carpeta_backup = "bk"

# # Invocación pasando el parámetro (obligatorio)
# os.mkdir(carpeta_backup)
# print(f"Directorio creado correctamente en: {carpeta_backup}")

# # Método con argumento opcional
# files_dir_actual = os.listdir()
# files_dir_backup = os.listdir(carpeta_backup)
# print(files_dir_actual)
# print(files_dir_backup)


## Método con 2 argumentos posicionales
# 1. Definimos los datos que necesita la función
log_actual = "servidor.log"
log_rotado = "servidor.log.old"

# 1.1 Crear archivo para que rename no falle,,,
with open(log_actual, mode="a", encoding="utf-8") as archivo:
    pass

# 2. Invocamos la función pasando ambos parámetros separados por una coma
os.rename(log_actual, log_rotado)

print("El archivo se ha renombrado correctamente.")


## Método con argumentos con nombre
# os.rename(dst="/tmp/archivo_nuevo.txt", src="/tmp/archivo.txt")