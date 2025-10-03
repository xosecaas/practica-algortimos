# Hugo Bouza Fernández
# Rafael Casás Lamas
# Xosé Castro González

import random
import time

# EJERCICIO 1
# Algoritmo ordenación por inserción (complejidad O(n^2))
def ord_insercion(v):
    n = len(v)
    vector = v.copy()   # copia para no modificar el original
    for i in range(1, n):
        x = vector[i]
        j = i - 1       
        while j >= 0 and vector[j] > x:
            vector[j + 1] = vector[j]
            j = j - 1       
        vector[j + 1] = x   
    return vector

# Algoritmo ordenación Shell (complejidad O(n^2))
def ord_shell(v, inc):
    vector = v.copy()  # copia para no modificar el original
    n = len(vector)
    m = len(inc)  
    for k in range(m - 1, -1, -1):
        h = inc[k]
        for i in range(h, n):
            x = vector[i]
            j = i
            while j >= h and vector[j - h] > x:
                vector[j] = vector[j - h]
                j = j - h
            vector[j] = x
    return vector


# Ejemplo de uso y prueba de los algoritmos
if __name__ == "__main__":
    # Vector de prueba
    vector_prueba = [64, 34, 25, 12, 22, 11, 90, 5]
    print("Vector original:", vector_prueba)
    
    # Prueba de ordenación por inserción
    resultado_insercion = ordenacion_insercion(vector_prueba)
    print("Ordenación por inserción:", resultado_insercion)
    
    # Prueba de ordenación Shell
    # Vector de incrementos típico (el primero debe ser 1)
    incrementos = [1, 3, 7]  # Secuencia común
    
    resultado_shell = ordenacion_shell(vector_prueba, incrementos)
    print("Ordenación Shell:", resultado_shell)
    
    # Verificación de que el original no se modifica
    print("Vector original (sin modificar):", vector_prueba)
