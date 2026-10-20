# DEVUELVE COMO RESULTADO la suma de valores de una lista
# def sumaLista(lista):
#     suma = 0
#     for x in lista:
#         suma += x   # suma = suma + x
#     return suma

# ventas = [1,2,3,4,5]
# ventasTotales = sumaLista(ventas)

# print("ventas:", ventas)
# print("ventasTotales:", ventasTotales)

# # DEVUELVE COMO RESULTADO la media USANDO LA FUNCIÓN sumaLista 
# def media(lista):
#     media = sumaLista(lista)/len(lista)
#     return media

# edades = [23, 46, 56, 72, 12, 34]
# print("sumaLista(edades):", sumaLista(edades))
# print("media(edades):", media(edades))


# Parametro posicionales
def carga_recibo(saldo, recibo):
    if recibo < 0:
        print("recibo debe ser > 0")
    elif saldo < recibo:
        print("saldo inferior a recibo")
    else:
        saldo = saldo - recibo
    
    return saldo

saldo_actual = 100
recibo_luz = 45
recibo_agua = 40
print("Saldo: ", saldo_actual)

# El orden importa, sin nombres la correspondencia es posicional
saldo_actual = carga_recibo(saldo_actual, recibo_luz)  # Correcto
print("Saldo tras recibo: ", saldo_actual)
print("llamada incorrecta que ademá modifica el saldo !!!!")
saldo_actual = carga_recibo(recibo_agua, saldo_actual)  # incorrecto !!!!
print("Saldo tras recibo: ", saldo_actual)

# # otra opción: con nombres
# saldo_actual = carga_recibo(recibo=recibo_luz, saldo=saldo_actual) # con nombres
# print("Saldo final: ", saldo_actual)