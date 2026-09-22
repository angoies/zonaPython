
# Ejemplo uso format en print
ombre = "Alfredo Zumberg"
edad = 23
altura = 1.915
print(nombre, "su edad es", edad, "y altura", altura)
# con format
print(f"{nombre} su edad es {edad} y altura {altura:.1f}") 


# Algunos métodos de string

saludo = "Hola Mundo"
print("saludo:", saludo)

print("saludo,lower():", saludo.lower())
print("saludo:", saludo)
# No modifica cadena original. 
# Si queremos modificar hace falta asignación

saludo = saludo.lower()
print("saludo:", saludo)

# Replace, lo mismo..
print("saludo.replace():", saludo.replace("mundo", "universo"))
print("saludo:", saludo)

# str como array o lista, longitud o tamaño del str
saludo ="¡Hola mundo!"
print("Primer carácter:", saludo[0])
print("Segundo carácter:",saludo[1])
print("Longitud saludo:", len(saludo))

# Buscar en un str: in y not in

texto = "The best thiNgs  life are free!"
busca = "FREE"

if busca.lower() in texto.lower():
    print("¡¡Sí está!!")
else:
    print("No está")

# o en negativo
if busca not in texto:
    print("No está")
else:
    print("¡¡Sí está!!") 
# Proponer: no case sensitive

 
# Concatenar str

nombre = "Raquel"
apellidos = "García Ross"
print(nombre + " " + apellidos) 

nombreCompleto = apellidos + ", " + nombre
print(nombreCompleto)

# Recorrer str
for x in nombre:
    print(x)
    
# con índices
for i in range(len(nombre)):
    print(f"{i}: {nombre[i]}")


# Extraer parte del string: slice

# La sintaxis del slicing en Python es string[inicio:fin:paso]:
#   - inicio: Por defecto empieza desde el extremo del string.
#   - fin: Por defecto recorre hasta el otro extremo.
#   - paso: por defecto 1.

saludo = "Hola Mundo"
print(saludo[:4])  # "Hola"
print(saludo[5:])  # "Mundo"
print(saludo[::2]) # de dos en dos => "Hl ud"

# Para invertir una cadena se usa salto negativo
print(saludo[::-1]) # en order inverso => "odnuM aloH"
 
