FICHERO = "config.ini"
print(f"Leyendo {FICHERO} línea por línea...")

try:
    with open(FICHERO, "r") as f:
        # 'f' se comporta como una lista de líneas
        for linea in f:
            # La variable 'linea' contiene una línea entera,
            # incluyendo el '\n' del final.

            # .strip() es un método de string que limpia
            # espacios, tabuladores y '\n' de los extremos.
            linea_limpia = linea.strip()

            # Imprimimos si la línea no está en blanco
            if linea_limpia:
                print(f"Línea leída: --> {linea_limpia} <--")

except FileNotFoundError:
    print(f"¡Error! El fichero '{FICHERO}' no existe.")