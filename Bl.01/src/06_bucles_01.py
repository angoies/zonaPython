# bucle for básico

# con índices y uso range
# for i in range(5):
#     print(i)

# for i in range(10, 20):
#     print(f"{i} ", end=" ")

# Suma números
# suma = 0  # acumulador
# ini = int (input("inicio: "))
# fin = int (input("fin: "))

# for i in range(ini, fin+1):
#     print(i)
#     suma = suma + i

# print("\nSuma:", suma)  # \n salto de línea

# Bucles while

numero = int(input("Introduce otro número (0 para terminar): "))
while numero!=0:
    print("Has introducido:", numero)
    numero = int(input("Introduce otro número (0 para terminar): "))
print("Fin del programa")

# while True:  # el uso del break debe ser "cuidadoso..."
#     numero = int(input("Introduce otro número (0 para terminar): "))
#     if numero==0:
#         break
#     print("Has introducido:", numero)
# print("Fin del programa")
