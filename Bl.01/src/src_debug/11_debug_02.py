def calcular_descuento(precio, porcentaje):
    descuento = precio * porcentaje / 100
    precio_final = precio - descuento
    return precio_final


precio = 100
porcentaje = 20

breakpoint()

resultado = calcular_descuento(precio, porcentaje)

print(resultado)