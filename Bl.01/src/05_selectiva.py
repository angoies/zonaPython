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

if (edad >= 18 and saldo > 0) or (saldo >100000):
    print("Puede jugar")
else:
    print("no puede jugar")
print("Fin selectiva")  # siempre,fuera if


# Ejemplo selectiva anidadas
a = int(input("valor de a:"))
b = 200

if b > a:
    print("b es mayor que a")
else: 
    if b<a:
        print("a es mayor que b")
    else:
        print("son iguales") 

# lo mismo con elif (else if), más legible/compacto
if b > a:
    print("b is greater than a")
elif b<a:
    print("a es mayorr que b")
else:
    print("son iguales") 


"""
Selector multiple
Cuando se quieren por ejemplo evaluar las opciones de un menú, para evitar concatenar demasiados elif que terminan haciendo ilegible nuestro código, se puede emplear la sentencia múltiple, que actúa sobre una variable normalmente numérica
""""

opcion = int(input("Seleccione una opción"))

match opcion:
    case 0:
        print("Ha seleccionado opción 0")
        print("procedemos")
    case 1:
        print("Ha seleccionado opción 1")
        print("procedemos")

    ...

    case _:   #este es el caso por defecto
        print("por defecto")
        print("cuando no se le ha indicado ninguna de las opciones contempladas")
