import numpy as np

# solve(a, b) : Devuelve la solución del sistema de ecuaciones lineales
# con los coeficientes de la matriz a y los términos independientes 
# de la matriz b.
# Sistema de dos ecuaciones y dos incógnitas
# x + 2y = 1
# 3x + 5y = 2 

a = np.array([[1, 2], [3, 5]])
b = np.array([1, 2])

print(np.linalg.solve(a, b))
# Resultado [-1. 1.]