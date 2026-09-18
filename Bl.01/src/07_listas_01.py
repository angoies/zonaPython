# Definir lista y uso básico

lista = ["Jerez", "Sevilla", "Huelva"]

# mostar toda la lista y su tipo
print(lista)
print(type(lista))

# mostrar un elemento
print(lista[0])
print(lista[1])

# mostrar el tamaño (longitud => len())
print("Nº de elementos de la lista:", len(lista))


# Ejemplos uso de lista

thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print("thislist", thislist)
# mostrar un rango
print("thislist[1:4]", thislist[1:4])

# generar nueva lista a partir de un rango
nueva_lista = thislist[1:4]
print("nueva_lista", nueva_lista)

# imprimir el último
print("thislist[len(thislist)-1]", thislist[len(thislist)-1])
print("Elemento finl: ", thislist[-1])

# modificar un elemento
print("Elemento 0: ", thislist[0])
print('ejecutamos thislist[0]="watermelon"')
thislist[0]="watermelon"
print("Elemento 0: ", thislist[0]) 



# lista vacía y longitud
lista = [1,2] 
print("lista: ",lista)
print("len(lista):", len(lista))

if len(lista) != 0:
    print("La lista contiene elementos")
else:
    print("Lista vacía")  
 
lista =  []
print("lista: ",lista)
print("len(lista):", len(lista))
if lista: # if len(lista) != 0:
    print("La lista contiene elementos")
else:
    print("Lista vacía") 


# Ejemplos formas de recorrer lista

lista = ["Jerez", "Sevilla", "Huelva"]

# los elementos con for
for x in lista:
    print("Hola ", x)

# los elementos y sus índices con for
for i in range(len(lista)):
    print(i, lista[i])

# Avanzado: comprensión de listas: [expresión for elemento in iterable]
[print(x) for x in lista]

