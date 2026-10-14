FICHERO = "config.ini"

print(f"Abriendo {FICHERO} con 'with'...")

try:
    with open(FICHERO, "r") as f:
        # f es la variable que maneja el fichero
        contenido = f.read()

    # En este punto, el fichero YA ESTÁ CERRADO.
    print("Lectura completada (fichero cerrado automáticamente).")

    print("\n--- INICIO DEL FICHERO ---")
    print(contenido)
    print("--- FIN DEL FICHERO ---")

except FileNotFoundError:
    # Esto se ejecuta si open() falla porque el fichero no existe
    print(f"¡Error! El fichero '{FICHERO}' no existe.")