# Variables, asignación (=) y tipos (int, float, str...) 

# Asignación
saldo_total = 254.55  # float
email = 'ana@local.com'  # str

print("saldo_total") # imprime cadena
print(saldo_total)   # imprime valor de la variable
  print(email)   # error indentación: el prograam se detiene

# Imprime tipo de las variables usando type(variable)
print("tipo de email: ", type(email)  )
print("tipo de saldo_total: ", type(saldo_total)  )
# print puede recibir varias expresiones separadas por comas

# Variables pueden cambiar de tipo
#  NO es algo recomdable
email = 4  # pasa de string a integer
print( "Tipo email: ", type(email)  )
print("El email es ", email, " y el saldo es ", saldo_total, "\n") 

