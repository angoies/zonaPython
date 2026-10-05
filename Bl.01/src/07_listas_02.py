# BSUCAR elemento en la lista 

# Con in => True/False

lista_IP = ["192.168.1.1", "10.10.10.10", "172.16.100.100", "195.172.1.1"]
print("lista_IP", lista_IP)

ip = input("IP a buscar: ")
if ip in lista_IP:
    print(f"Yes, {ip} is in {lista_IP}") 
else:
    print(f"No, {ip} is not in {lista_IP}") 

# Buscar con index si necesitamos la posición 
# Nota: index genera excepción si no está

print("lista_IP", lista_IP)
ip = input("IP a buscar: ")

# pos = lista_IP.index(ip)  # Genera excepción si no está en la lista

# Para corregir excepción si no se encuentra
# a) usar in o count antes de index 
if ip in lista_IP:
    pos = lista_IP.index(ip) 
    print(f"{ip} está en la posición {pos}") 
else:
    print(f"{ip} NO está en {lista_IP}") 

# b) se añade bloque try/except  para evitarlo
try:
    pos = lista_IP.index(ip) 
    print(f"{ip} está en la posición {pos}") 
except ValueError:
    print(f"{ip} NO está en {lista_IP}") 

    


