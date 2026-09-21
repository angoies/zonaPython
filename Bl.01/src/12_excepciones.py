import os

def crear_directorio_backup(ruta):
    try:
        # Invocación de la función con la ruta requerida
        os.mkdir(ruta)
        print(f"El directorio '{ruta}' ha sido creado correctamente.")
        
    except FileExistsError:
        print(f"[Warning] El directorio '{ruta}' ya existe. No se realizó ninguna acción.")
        
    except PermissionError:
        print(f"[Error] Permisos insuficientes para crear '{ruta}'. ")
        
    except FileNotFoundError:
        print(f"[Error] La ruta base especificada en '{ruta}' no existe.")
        
    except Exception as e:  # Actua como default, y {e} muestra el error
        print(f"[Otros] Error inesperado al intentar crear la carpeta: {e}")
        # print(f"Tipo de excepción real: {type(e).__name__}")  # nombre exacto de la excepción

# --- Pruebas de ejecución ---


# # Invocación de la función en directorio sin permisos
# os.mkdir("/root/nueva_carpeta")

# 1. Creación normal
crear_directorio_backup("/tmp/mis_backups")

# 2. Ya creado en paso 1, capturará el FileExistsError
crear_directorio_backup("/tmp/mis_backups")

# 3. Intentar crear en  directorio restringido 
crear_directorio_backup("/root/nueva_carpeta")

# 4. Intentar crear en una ruta que no existe
crear_directorio_backup("/tmp/docs/nueva_carpeta")