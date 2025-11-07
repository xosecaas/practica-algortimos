# Hugo Bouza Fernández
# Rafael Casás Lamas
# Xosé Castro González

import random
import time

# MEDICIÓN DE TIEMPO
def microsegundos():
    return time.perf_counter_ns() // 1000

def medir_tiempo_algoritmo(algoritmo, inicializar, n):
    # Primera medición directa
    v = inicializar(n)
    t1 = microsegundos()
    algoritmo(v) 
    t2 = microsegundos()
    t_directo = t2 - t1
    
    asterisco = False
    
    if t_directo < 1000:    # Umbral de confianza: 1000 microsegundos
        asterisco = True
        k = 10000    # Número de iteraciones
        
        # Medir K ejecuciones del algoritmo completo
        t1 = microsegundos()
        for _ in range(k):
            v = inicializar(n)
            algoritmo(v)
        t2 = microsegundos()
        t1_total = t2 - t1
        
        # Medir K ejecuciones solo de la inicialización
        t1 = microsegundos()
        for _ in range(k):
            v = inicializar(n)
        t2 = microsegundos()
        t2_inicializacion = t2 - t1
        
        tiempo_neto = (t1_total - t2_inicializacion) / k
        
        if tiempo_neto <= 0:        # Comprobación para resultados negativos
            return max(t_directo, 1), asterisco 
        else:
            return tiempo_neto, asterisco
    else:
        return t_directo, asterisco


# ALGORITMO ORDENACIÓN POR INSTERCIÓN
def ord_insercion(v):
    n = len(v)
    for i in range(1, n):
        x = v[i]
        j = i - 1
        while j >= 0 and v[j] > x:
            v[j + 1] = v[j]
            j = j - 1
        v[j + 1] = x


# EJERCICIOS 1 Y 2
def mediana3(v, i, j):
    k = (i + j) // 2
    if v[k] > v[j]:
        v[k], v[j] = v[j], v[k]
    if v[k] > v[i]:
        v[k], v[i] = v[i], v[k]
    if v[i] > v[j]:
        v[i], v[j] = v[j], v[i]

def ord_rapida_aux(v, izq, der, umbral):
    if izq + umbral <= der:
        mediana3(v, izq, der)
        pivote = v[izq]
        i = izq
        j = der
        while True:
            i += 1
            while v[i] < pivote:
                i += 1
            j -= 1
            while v[j] > pivote: 
                j -= 1   
            if j <= i:
                break
            v[i], v[j] = v[j], v[i] # Intercambiar elementos
        v[i], v[j] = v[j], v[i] # Deshacer el último intercambio
        v[izq], v[j] = v[j], v[izq] # Colocar el pivote en su posición correcta
        ord_rapida_aux(v, izq, j-1, umbral)
        ord_rapida_aux(v, j+1, der, umbral)

def ord_rapida(v, umbral):
    n = len(v)
    ord_rapida_aux(v, 0, n- 1, umbral)
    if (umbral > 1):
        ord_insercion(v)


# EJERCICIO 3
# Inicialización de vectores
def aleatorio(n):
    v = list(range(n))
    for i in range(n):
        v[i] = random.randint(-n, n)
    return v

def ascendente(n):
    return list(range(1, n+1)) 

def descendente(n):
    return list(range(n, 0, -1))
