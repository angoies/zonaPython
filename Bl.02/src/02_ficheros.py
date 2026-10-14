# 1. Abrir: Esta vez en modo lectura ('r').
# Si 'config.ini' no existiera fallaría.
print("Abriendo 'config.ini' en modo 'r'...")
fichero = open("config.ini", "r")

# 2. Operar: se usa .read() para leer TODO el contenido de golpe.
# Lo guardamos en una variable de tipo string.
print("Leyendo contenido...")
contenido_completo = fichero.read()

# 3. Cerrar
fichero.close()
print("Fichero cerrado.")

# 4. Muestra la lectura
print("\n--- INICIO DEL FICHERO ---")
print(contenido_completo)
print("--- FIN DEL FICHERO ---")