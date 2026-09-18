# ordenar listas: sort ,reverse
edades = [19, 17, 23, 56, 48, 100, 31]
print("edades:", edades)

edades.sort()
print("edades tras edades.sort():", edades)
edades.reverse()
print("edades tras edades.reverse():", edades)


# Modificar la lista

## añadir al final
print("edades:", edades)
edades.append(20)
print("edades tras edades.append(20):", edades)

## añadir en cualquier posición: 
# The insert() method inserts an element to the list at the specified index.
edades.insert(1, 44)
print("edades tras edades.insert(1,44):", edades)

# Borrar un elemento
# The list pop() method removes the item at the specified index. The method also returns the removed item.
eliminado = edades.pop() # Si no hay index extrae el último
print("edades tras eliminado = edades.pop()", edades)
print("eliminado:", eliminado )

eliminado = edades.pop(0)
print("edades tras eliminado = edades.pop(0)", edades)
print("eliminado:", eliminado )

# Vaciar la lista
# The clear() method empties the list.
edades.clear()
print("edades tras clear", edades)


## CONVERTIR string en lista: split

users = "ana:luis:alfredo"
lista = users.split(":")
print("users:", users)
print("type(users)", type(users))
print("lista: ", lista)
print("type(lista)", type(lista))


# Ejemplo lectura notas con input y conversión a lista para calcular media

lectura = input("Notas separadas por el caracter ':'" )
print(lectura, type(lectura)) # es un string
notas = lectura.split(":") # es una lista
print(notas, type(notas))

suma = 0 # Almacena la suma de las notas
media = 0
for x in notas:
    suma = suma + int(x)
media = suma/len(notas)
print("Suma: ", suma)
print(f"Media: {media:.2f}")


# Avanzado: la conversión a enteros de una lista de string se puede 
#  hacer con map o con compresión

# comprensión de listas
edades = ["14", "21", "17", "33", "45"]
print("edades:", edades, "tipo:", type(edades))
print("type(edades[0]):", type(edades[0]))

edades =  [int(x) for x in edades]
print("edades:", edades, "tipo:", type(edades))
print("type(edades[0]):", type(edades[0]))

# método map. ojo que no es una lista, hay que convertirla
edades = ["14", "21", "17", "33", "45"]
print("edades:", edades, "tipo:", type(edades))
print("type(edades[0])", type(edades[0]))

edades = map(int, edades) 
print("edades:", edades, "tipo:", type(edades))
edades = list(map(int, edades))

print("edades:", edades, "tipo:", type(edades))
print("type(edades[0])", type(edades[0]))



