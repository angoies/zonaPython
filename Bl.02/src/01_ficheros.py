# 1. Abrir: fichero 'config.ini' en modo escritura ('w').
# Si ya existía, se borra su contenido. Si no, se crea.
print("Abriendo 'config.ini' en modo 'w'...")
fichero = open("config.ini", "w")

# 2. Operar: Escribe líneas en el fichero.
print("Escribiendo datos...")
fichero.write("hostname=servidor-web-01\n")
fichero.write("ip=192.168.1.100\n")
fichero.write("admin=root\n")
# '\n' es nueva línea.


# 3. Cerrar: guarda los cambios y libera el fichero.
fichero.close()
print("Fichero 'config.ini' creado y cerrado.")