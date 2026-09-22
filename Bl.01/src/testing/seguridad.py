
def comprueba_clave(login, password):
  valida = True
  claves_prohibidas = {
        "123456789012",
        "password12345",
        "administrador2026"
  }

  if len(password) <10:
    valida = False
  elif password in claves_prohibidas:
    valida = False
  elif login in password:
    valida = False

  return valida

if __name__ == "__main__":
    print(comprueba_clave("alumno", "nose"))
    print(comprueba_clave("alumno", "administrador2026"))
    print(comprueba_clave("alumno", "alumno1234567890"))
    print(comprueba_clave("alumno", "1234qwerasdfzxcv"))

