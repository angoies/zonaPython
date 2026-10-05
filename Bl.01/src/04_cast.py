# conversión de tipos

# Ejemplo sin cast que no "funciona"
saldo = input("saldo: ")
incremento = input("incremento: ")

total = saldo + incremento
print("Valor de total sin cast: ", total)
print(type(saldo))
print(type(incremento))
"""
 El operador + en cadenas concatena
"""

# Se intenta ahora haciendo cast de las cadenas
saldo = float(saldo)
incremento = float(incremento)
total = saldo + incremento
print("Valor de total: ", total)

"""
 => Convertir a números las lecturas antes de operar con ellas 
"""







