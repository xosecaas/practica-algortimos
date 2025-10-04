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

#EJERCICIO 2
# Secuencias de incrementos para Shell
def secuencia_hibbard(n):
    sec = []
    k = 1
    while True:
        incremento = 2**k - 1
        if incremento > n:
            break
        sec.append(incremento)
        k += 1
    return sec[::-1]  # De mayor a menor

def secuencia_knuth(n):
    sec = []
    k = 1
    while True:
        incremento = (3**k - 1) // 2
        if incremento > n:
            break
        sec.append(incremento)
        k += 1
    return sec[::-1]  # De mayor a menor

def secuencia_sedgewick(n):
    sec = [1]
    k = 1
    while True:
        # Fórmula: 4^k + 3 * 2^(k-1) + 1
        incremento = 4**k + 3 * (2**(k-1)) + 1
        if incremento > n:
            break
        sec.append(incremento)
        k += 1
    return sec[::-1]  # De mayor a menor

def secuencia_ciura(n):
    base = [1, 4, 10, 23, 57, 132, 301, 701, 1750]
    sec = []   
    for inc in base:
        if inc <= n:
            sec.append(inc)
        else:
            break
    if sec and sec[-1] < n:
        ultimo = sec[-1]
        while ultimo <= n:
            ultimo = round(ultimo * 2.25)
            if ultimo <= n:
                sec.append(ultimo)  
    return sec[::-1] 
