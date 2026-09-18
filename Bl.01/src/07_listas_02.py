# BSUCAR elemento en la lista 

# Con in => True/False

thislist = ["apple", "banana", "cherry"]
print("thislist", thislist)
buscar = input("Fruta a buscar: ")

if buscar.lower() in thislist:
    print(f"Yes, {buscar} is in the fruits list") 
else:
    print(f"No, {buscar} no está")

# Buscar con index si necesitamos la posición 
# Nota: index genera excepción si no está
thislist = ["apple", "banana", "cherry"]
print("thislist", thislist)
buscar = input("Fruta a buscar: ")

# pos = thislist.iWdex(buscar)  # Genera excepción si no está en la lista

# Para corregir excepción si no se encuentra
# a) usar in o count antes de index 
if buscar.lower() in thislist:
    pos = thislist.index(buscar) 
    print(f"{buscar} está en la posición {pos}") 
else:
    print("That item does not exist") 

# b) se añade bloque try/except  para evitarlo
try:
    pos = thislist.index(buscar) 
    print(f"{buscar} está en la posición {pos}") 
except ValueError:
    print("That item does not exist") 

    


