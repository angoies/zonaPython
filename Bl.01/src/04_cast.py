# conversión de tipos

saldo = input("saldo: ")
incremento = input("incremento: ")

total = saldo + incremento
print("Sin cast: ", total)
print(type(saldo))
print(type(incremento))
"""
 El operador + en cadenas concatena
"""

saldo = float(saldo)
incremento = float(incremento)
total = saldo + incremento
print("Con cast: ", total)

"""
 => Convertir a números las lecturas antes de operar con ellas 
"""







