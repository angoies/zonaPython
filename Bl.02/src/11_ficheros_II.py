import os

IP = "8.8.8.8"  # DNS de Google
print(f"Haciendo ping a {IP}...")

# os.name nos dice el S.O. ('nt' es Windows, 'posix' es Linux/Mac)
if os.name == 'nt':
    # -n 4 -> 4 pings (en Windows)
    comando = f"ping -n 4 {IP}"
else:
    # -c 4 -> 4 pings (en Linux/Mac)
    comando = f"ping -c 4 {IP}"

os.system(comando) # Deprecated, usar subprocess

print("Ping finalizado.")
