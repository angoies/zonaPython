
# bucle for básico

# con índices y uso range
for i in range(5):
    print(f"{i} ")

for i in range(5):
    print(f"{i} ", end=" ")

for i in range(10, 20):
    print(f"{i} ", end=" ")

# Suma números
suma = 0  # acamulador
limite = 5
for i in range(limite+1):
    suma = suma + i
print("\nSuma:", suma)

# while

numero = int(input("Introduce un número (0 para terminar): "))

while numero != 0:
    print("Has introducido:", numero)
    numero = int(input("Introduce otro número (0 para terminar): "))

print("Fin del programa")


