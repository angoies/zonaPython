# Definir lista y uso básico

# Lista de enteros
puertos = [22, 80, 443, 8080]

# mostar la lista y su tipo
print(puertos)
print(type(puertos))

# mostrar un elemento de la lista
print(puertos[0])
print(puertos[1])

# mostrar el tamaño (longitud => len())
print("Nº de elementos de la lista:", len(puertos))


# Ejemplos uso de lista: mostrar un rango
frutas = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print("frutas", frutas)
print("frutas[1:4]", frutas[1:4])

# Ejemplos uso de lista: generar nueva lista a partir de un rango
nueva_lista = frutas[1:4]
print("nueva_lista", nueva_lista)

# imprimir el último de una lista: usando len o con índice negativo...
print("frutas[len(frutas)-1]", frutas[len(frutas)-1])
print("Elemento finl: ", frutas[-1])

# modificar un elemento de la lista
print("Elemento 0: ", frutas[0])
print('ejecutamos frutas[0]="watermelon"')
frutas[0]="watermelon"
print("Elemento 0: ", frutas[0]) 


# Verificar lista vacía
lista = [1,2] 
print("lista: ",lista)
print("len(lista):", len(lista))

# B) usando longitud
if len(lista) != 0:
    print("La lista contiene elementos")
else:
    print("Lista vacía")  

# A) preferible usando la lista como condición lógica
lista =  []
print("lista: ",lista)
print("len(lista):", len(lista))
if lista: # if len(lista) != 0:
    print("La lista contiene elementos")
else:
    print("Lista vacía") 


# Ejemplos formas de recorrer lista
lista_IP = ["192.168.1.1", "10.10.10.10", "172.16.100.100", "195.172.1.1"]

# los elementos con for
for x in lista_IP:
    print("IP: ", x)

# los elementos y sus índices con for
for i in range(len(lista_IP)):
    print(f"IP[{i}]: {lista_IP[i]}")

# Avanzado: comprensión de listas: [expresión for elemento in iterable]
[print(" -", x) for x in lista_IP ]

