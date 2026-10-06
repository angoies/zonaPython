## Depuración: errores 

# Error sintaxis
# edad = 20

# if edad >= 18
#     print("Mayor de edad")

# Error en ejecución
# numero = 10
# divisor = 0

# resultado = numero / divisor


# Errores por tipo: input 
# edad = input("Edad: ")

# print(edad)
# print(type(edad))


# Error en la lógica
precios = [10, 20, 30]
total = 0

for precio in precios:
    total = precio

print(total)


# Se añade print
for precio in precios:
    total = precio
    print(f"numero={precio}, total={total}")

print(total)


# Se añade break
for precio in precios:
    total = precio
    breakpoint()
    # print(f"numero={numero}, total={total}")

print(total)