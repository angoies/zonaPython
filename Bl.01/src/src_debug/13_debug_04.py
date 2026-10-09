def aplicar_iva(precio):
    return precio * 1.21


def calcular_total(precios):
    total = 0

    for precio in precios:
        total += aplicar_iva(precio)

    return total


def generar_factura():
    precios = [10, 20, 30]
    return calcular_total(precios)

resultado = generar_factura()

print("Resultad0:", resultado)