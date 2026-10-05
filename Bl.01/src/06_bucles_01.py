# bucle for básico

# con índices y uso range
for i in range(5):
    print(i)

for i in range(10, 20):
    print(f"{i} ", end=" ")

# Suma números
suma = 0  # acumulador
ini = int(input("inicio: "))
fin = int(input("fin: "))

for i in range(ini, fin+1):
    print(i)
    suma += i  # equivale a suma = suma + i   

print("\nSuma:", suma)  # \n salto de línea

# Bucle while

numero = int(input("Introduce un número (0 para terminar): "))
while numero != 0:
    print("Has introducido:", numero)
    numero = int(input("Introduce otro número (0 para terminar): "))
print("Fin del programa")

while True:  # el uso del break debe ser "cuidadoso..."
    numero = int(input("Introduce un número (0 para terminar): "))
    if numero == 0:
        break
    print("Has introducido:", numero)
print("Fin del programa")

# Se muestra ahora el uso de cadenas con bucle for

nombre = "www.aulas.local"
# a) Recorrer cada caracter de un str
for x in nombre:
    print(x)
    
# b) Recorrer cada caracter de un str 
# usando el índice o posición si es necesario en el bucle
for i in range(len(nombre)):
    print(f"Pos{i}: {nombre[i]}")

