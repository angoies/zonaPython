import os
import subprocess

IP = "8.8.8.8"  # DNS de Google

print(f"Haciendo ping a {IP}...")

# os.name nos dice el S.O. ('nt' es Windows, 'posix' es Linux/Mac)
if os.name == "nt":
    # -n 4 -> 4 pings en Windows
    comando = ["ping", "-n", "4", IP]
else:
    # -c 4 -> 4 pings en Linux/Mac
    comando = ["ping", "-c", "4", IP]

resultado = subprocess.run(comando)

if resultado.returncode == 0:
    print("Ping finalizado correctamente.")
else:
    print("El ping ha finalizado con errores.")