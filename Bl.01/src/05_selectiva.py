## Selectiva simple (y  probar indentación)

edad = int(input("Edad: "))
print( type(edad) ) 

if  edad >= 18:  # selectiva simple
    print("Adulto")
    print("puede jugar") ## Error indentación
print("¡Hola Clase!")  # siempre,fuera if




# Ejemplo selectiva if-else y condición lógica con and

saldo = int(input("saldo: "))
edad = int(input("edad: "))

if (edad >= 18 and saldo > 0) or (saldo > 100000):
    print("Puede jugar")
else:
    print("no puede jugar")
print("Fin selectiva")  # siempre se muestra,fuera selectiva


# Ejemplo selectivas anidadas
a = int(input("valor de a:"))
b = 200

if b > a:
    print(f"{b} es mayor que {a}")
else: 
    if b < a:
        print(f"{a} es mayor que {b}")
    else:
        print(f"{a} es igual a {b}")

# lo mismo con elif (else if), más legible/compacto
if b > a:
    print(f"{b} es mayor que {a}")
elif b < a:
    print(f"{a} es mayor que {b}")
else:
    print(f"{a} es igual a {b}")


"""
Selector multiple
 Cuando se quieren por ejemplo evaluar las opciones de un menú
 evita concatenar demasiados elif que hacen menos legible el código, 
"""

opcion = int(input("Seleccione una opción: "))

match opcion:
    case 0:
        print("Ha seleccionado opción 0")
        print("procedemos opción 0")
    case 1:
        print("Ha seleccionado opción 1")
        print("procedemos opción 1")

    # otros case...

    case _:   #este es el caso por defecto
        print("Opción por defecto")
        print("No ha indicado ninguna opción contemplada")
