
# Ejemplo uso format en print
nombre = "Alfredo Zumberg"
edad = 23
altura = 1.915
print(nombre, "su edad es", edad, "y altura", altura)
# Uso de format con cadenas
print(f"{nombre} su edad es {edad} y altura {altura:.1f}") 


# Algunos métodos de string

saludo = "Hola Mundo"
print("Valor de saludo:", saludo)

print("Resultado de saludo.lower():", saludo.lower())
print("Valor de saludo:", saludo)


# No modifica cadena original. 
# Si queremos modificar hace falta asignación
saludo = saludo.lower()
print("Valor de saludo:", saludo)

# Replace, lo mismo..
print('Resultado de saludo.replace("mundo", "universo"):' , saludo.replace("mundo", "universo"))
print("Valor de saludo:", saludo)

# el tipo str se puede tratar como array o lista:
saludo ="¡Hola mundo!"
print("Primer carácter:", saludo[0])
print("Segundo carácter:",saludo[1])
print("Longitud saludo:", len(saludo))

# Buscar en un str: in y not in
texto = "The best thiNgs  life are free!"
busca = "FREE"

if busca.lower() in texto.lower():
    print(f"{busca} sí está en {texto}")
else:
    print(f"{busca} NO está en {texto}")

# o en negativo y sin ser case sensitve
if busca not in texto:
    print(f"{busca} NO está en {texto}")
else:
    print(f"{busca} sí está en {texto}")

 
# Concatenar str
nombre = "Raquel"
apellidos = "García Ross"
print(nombre + " " + apellidos)  # el operador + con cadenas concatena

nombreCompleto = apellidos + ", " + nombre
print(nombreCompleto)

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





 
