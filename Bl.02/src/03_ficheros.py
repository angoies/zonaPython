# 1. Abrir: En modo 'append' ('a').
# El *cursor* se pone al final del fichero.
print("Abriendo 'config.ini' en modo 'a'...")
fichero = open("config.ini", "a")

# 2. Operar: Escribe la nueva línea.
fichero.write("puerto=80\n")

# 3. Cerrar:
fichero.close()
print("Fichero modificado y cerrado.")