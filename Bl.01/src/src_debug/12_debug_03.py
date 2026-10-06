def calcular_media(lista):
    suma = 0

    for x in lista:
        suma = x

    return suma / len(lista)


precios = [7, 8, 5, 9]

media = calcular_media(precios)

print("Media:", media)