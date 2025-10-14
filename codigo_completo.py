# Hugo Bouza Fernández
# Rafael Casás Lamas
# Xosé Castro González

import random
import time
import sys

# Aumentar el límite de recursión para las inicializaciones grandes si fuera necesario
# Aunque no se usa recursión, es una buena práctica en scripts de análisis.
# sys.setrecursionlimit(2000)

# ==============================================================================
# REUTILIZACIÓN DE CÓDIGO DE P1_ALGORITMOS.PY (Medición de Tiempo)
# ==============================================================================

def microsegundos():
    """Función para obtener la hora del sistema en microsegundos (10^-6 s)."""
    return time.perf_counter_ns() // 1000

def aleatorio(n):
    """Genera un vector de tamaño n con números enteros aleatorios en [-n, n]."""
    v = list(range(n))
    for i in range(n):
        # Se generan números aleatorios en un rango adecuado.
        v[i] = random.randint(-n, n)
    return v

def medir_tiempo_algoritmo(algoritmo, inicializar, n):
    """
    Mide el tiempo de ejecución del algoritmo para un tamaño n y lo ajusta 
    mediante repeticiones si el tiempo es muy bajo. (Reutilizado de p1_algoritmos.py)
    """
    # Primera medición directa
    v = inicializar(n)
    t1 = microsegundos()
    # Ejecutamos el algoritmo. El retorno no se usa, solo se mide el tiempo.
    algoritmo(v) 
    t2 = microsegundos()
    t_directo = t2 - t1
    
    if t_directo < 1000:    # Umbral de confianza: 1000 microsegundos
        k = 1000    # Número de repeticiones (ejecuciones). Ajustar si es necesario.
        
        # Medir K ejecuciones del algoritmo completo (inicialización + algoritmo)
        t1 = microsegundos()
        for _ in range(k):
            v = inicializar(n)
            algoritmo(v)
        t2 = microsegundos()
        t1_total = t2 - t1
        
        # Medir K ejecuciones solo de la inicialización
        t1 = microsegundos()
        for _ in range(k):
            # Necesitamos inicializar el vector, pero sin ejecutar el algoritmo
            v = inicializar(n)
        t2 = microsegundos()
        t2_inicializacion = t2 - t1
        
        tiempo_neto = (t1_total - t2_inicializacion) / k
        
        if tiempo_neto <= 0:        
            # Si el tiempo neto es negativo o cero, devolvemos la medición directa
            return max(t_directo, 1) 
        else:
            return tiempo_neto
    else:
        return t_directo

# ==============================================================================
# INICIALIZACIÓN DE VECTORES (Ejercicio 3 - Situaciones Iniciales)
# ==============================================================================

def ascendente(n):
    """Inicializa un vector ordenado ascendentemente."""
    # Enunciado Figura 1: list(range(1, n+1))
    return list(range(1, n + 1)) 

def descendente(n):
    """Inicializa un vector ordenado descendentemente (Peor Caso para Inserción)."""
    return list(range(n, 0, -1))

# La función aleatorio(n) se encuentra en la sección de REUTILIZACIÓN.

# ==============================================================================
# IMPLEMENTACIÓN DE ALGORITMOS (Ejercicio 1)
# ==============================================================================

# Algoritmo ordenación por inserción (Complejidad esperada: O(n) Mejor Caso, O(n^2) Peor/Promedio)
def ord_insercion(v):
    """Ordenación por Inserción (basado en el pseudocódigo del enunciado)"""
    n = len(v)
    vector = v.copy()   # Copia para no modificar el original
    for i in range(1, n):
        x = vector[i] # v[i] en el pseudocódigo
        j = i - 1       
        while j >= 0 and vector[j] > x:
            vector[j + 1] = vector[j] # v[j+1] := v[j]
            j = j - 1       
        vector[j + 1] = x   # v[j+1] := x
    return vector

# Algoritmo ordenación Shell (Complejidad esperada: Subcuadrática, ej. O(n^1.3) a O(n^1.5))
def ord_shell(v, inc):
    """Ordenación Shell (basado en el pseudocódigo del enunciado)"""
    vector = v.copy()  # Copia para no modificar el original
    n = len(vector)
    m = len(inc)  
    
    # El vector inc debe estar de mayor a menor incremento.
    # El pseudocódigo itera de m hasta 1.
    for k in range(m - 1, -1, -1): # Itera sobre el vector de incrementos 'inc'
        h = inc[k] # Incremento actual
        # Ordenación por inserción con salto h (h-ordenación)
        for i in range(h, n): # Desde h+1 hasta n en el pseudocódigo (en Python desde índice h hasta n-1)
            x = vector[i]
            j = i
            # Mientras j sea >= h (j > 0 en Inserción) y el elemento anterior esté desordenado
            while j >= h and vector[j - h] > x: 
                vector[j] = vector[j - h]
                j = j - h
            vector[j] = x
    return vector

# ==============================================================================
# GENERACIÓN DE SECUENCIAS DE INCREMENTOS (Ejercicio 2)
# ==============================================================================

def secuencia_hibbard(n):
    """Secuencia 2^k - 1 (1, 3, 7, 15...). Devuelve en orden descendente."""
    sec = []
    k = 1
    while True:
        incremento = 2**k - 1
        if incremento > n // 2: # El incremento máximo no debe superar n/2 para ser efectivo
            break
        sec.append(incremento)
        k += 1
    # Nos aseguramos que siempre termine en 1 si n es suficiente
    if not sec or sec[0] != 1:
        if 1 not in sec:
             sec.append(1)
        sec = sorted(list(set(sec)))
    
    return sec[::-1]  # De mayor a menor

def secuencia_knuth(n):
    """Secuencia (3^k - 1)/2 (1, 4, 13, 40...). Devuelve en orden descendente."""
    sec = []
    k = 1
    while True:
        incremento = (3**k - 1) // 2
        if incremento > n // 2:
            break
        sec.append(incremento)
        k += 1
    if not sec or sec[0] != 1:
        if 1 not in sec:
             sec.append(1)
        sec = sorted(list(set(sec)))
        
    return sec[::-1] 

def secuencia_sedgewick(n):
    """Secuencia 4^k + 3 * 2^(k-1) + 1 (1, 8, 23, 77...). Devuelve en orden descendente."""
    sec = []
    k = 1
    while True:
        # Fórmula: 4^k + 3 * 2^(k-1) + 1
        incremento = 4**k + 3 * (2**(k-1)) + 1
        if incremento > n // 2:
            break
        sec.append(incremento)
        k += 1

    # Asegura que 1 esté siempre presente como último paso
    if not sec or sec[0] != 1:
        if 1 not in sec:
             sec.append(1)
        sec = sorted(list(set(sec)))

    return sec[::-1] 

def secuencia_ciura(n):
    """Secuencia Ciura (1, 4, 10, 23...). Con ampliación para n grande."""
    # [cite_start]Base de Ciura: [1, 4, 10, 23, 57, 132, 301, 701, 1750] [cite: 12]
    base = [1, 4, 10, 23, 57, 132, 301, 701, 1750]
    sec = []   
    
    # 1. Añadir incrementos base que no superen n
    for inc in base:
        if inc <= n // 2:
            sec.append(inc)
        else:
            break
    
    # [cite_start]2. Ampliación por 2.25 y redondeo si el último es menor que n [cite: 14]
    if sec and sec[-1] < n // 2:
        ultimo = sec[-1]
        while ultimo <= n // 2:
            # Multiplicación por 2.25 y redondeo al entero más cercano
            proximo_inc = round(ultimo * 2.25) 
            if proximo_inc > n // 2:
                 break
            if proximo_inc > ultimo: # Evitar bucles infinitos si redondeo no cambia valor
                sec.append(proximo_inc)
                ultimo = proximo_inc
            else:
                break
    
    # Asegura que 1 esté presente y elimina duplicados si los hubiera
    if 1 not in sec:
        sec.append(1)
    
    return sorted(list(set(sec)))[::-1] # Orden descendente

# ==============================================================================
# VALIDACIÓN DEL FUNCIONAMIENTO (Ejercicio 2)
# ==============================================================================

def esta_ordenado(v):
    """Verifica si un vector está ordenado ascendentemente."""
    for i in range(len(v) - 1):
        if v[i] > v[i + 1]:
            return False
    return True

def test_algoritmos(n=11):
    """
    Valida el funcionamiento de la Ordenación por Inserción y Ordenación Shell 
    con las diferentes secuencias.
    """
    print("=" * 70)
    print("EJERCICIO 2: VALIDACIÓN DE ALGORITMOS DE ORDENACIÓN")
    print("=" * 70)
    
    # Pruebas de inicialización
    v_aleatorio = aleatorio(n)
    v_descendente = descendente(n)

    # --- Ordenación por Inserción ---
    v_ord_ins = ord_insercion(v_aleatorio)
    print(f"\n--- Ordenación por Inserción (Vector Aleatorio de n={n}) ---")
    print(f"Vector Original: {v_aleatorio}")
    print(f"Vector Ordenado: {v_ord_ins}")
    print(f"Ordenado? {esta_ordenado(v_ord_ins)}")
    
    # --- Ordenación Shell ---
    secuencias = {
        "Hibbard": secuencia_hibbard,
        "Knuth": secuencia_knuth,
        "Sedgewick": secuencia_sedgewick,
        "Ciura": secuencia_ciura
    }
    
    print(f"\n--- Ordenación Shell (Vector Descendente de n={n}) ---")
    print(f"Vector Original: {v_descendente}")
    
    for nombre, func_sec in secuencias.items():
        inc = func_sec(n)
        v_ord_shell = ord_shell(v_descendente, inc)
        print("-" * 50)
        print(f"Secuencia {nombre}: {inc} (Primer incremento debe ser 1: {inc[-1] == 1})")
        print(f"Vector Ordenado: {v_ord_shell}")
        print(f"Ordenado? {esta_ordenado(v_ord_shell)}")

test_algoritmos() # Ejecutar validación
print("\n")

# ==============================================================================
# ANÁLISIS DE COMPLEJIDAD Y GENERACIÓN DE TABLAS (Ejercicios 3, 4 y 5)
# ==============================================================================

# Tamaños de vectores a analizar (Se extiende el rango del ejemplo de p1_algoritmos.py)
VECTORES_N = [500, 1000, 2000, 4000, 8000, 16000, 32000] 

# Función auxiliar para imprimir las tablas en el formato requerido
def print_tabla(titulo, n_values, tiempos, k_exponents):
    """Imprime una tabla de resultados para el análisis de complejidad."""
    
    header_str = f"{"n":<10} {"t(n)":<20}"
    for k in k_exponents:
        header_str += f" {"t(n)/n^{:.2f}".format(k):<30}"

    print("-" * (10 + 20 + 30 * len(k_exponents)))
    print(f"{titulo.upper()}")
    print("-" * (10 + 20 + 30 * len(k_exponents)))
    print(header_str)
    print("-" * (10 + 20 + 30 * len(k_exponents)))

    for i, n in enumerate(n_values):
        t = tiempos[i]
        line = f"{n:<10} {t:<20.4f}"
        for k in k_exponents:
            ratio = t / (n**k)
            line += f" {ratio:<30.8f}"
        print(line)
    print("-" * (10 + 20 + 30 * len(k_exponents)))
    print()


# ------------------------------------------------------------------------------
# 1. Ordenación por Inserción (Ejercicio 3)
# ------------------------------------------------------------------------------

print("=" * 70)
print("EJERCICIO 3: ANÁLISIS DE ORDENACIÓN POR INSERCIÓN (3 TABLAS)")
print("=" * 70)

# Caso (a): Mejor Caso (Vector ya ordenado ascendentemente) -> Complejidad O(n)
tiempos_asc = []
for n in VECTORES_N:
    t = medir_tiempo_algoritmo(ord_insercion, ascendente, n)
    tiempos_asc.append(t)

print_tabla(
    "** Ordenación Inserción - Inicialización Ascendente (Mejor Caso: O(n)) **",
    VECTORES_N,
    tiempos_asc,
    [0.8, 1.0, 1.2]
)

# Caso (b): Peor Caso (Vector ordenado descendentemente) -> Complejidad O(n^2)
tiempos_desc = []
for n in VECTORES_N:
    t = medir_tiempo_algoritmo(ord_insercion, descendente, n)
    tiempos_desc.append(t)

print_tabla(
    "** Ordenación Inserción - Inicialización Descendente (Peor Caso: O(n^2)) **",
    VECTORES_N,
    tiempos_desc,
    [1.8, 2.0, 2.2]
)

# Caso (c): Caso Promedio (Vector aleatorio) -> Complejidad O(n^2)
tiempos_aleatorio = []
for n in VECTORES_N:
    t = medir_tiempo_algoritmo(ord_insercion, aleatorio, n)
    tiempos_aleatorio.append(t)

print_tabla(
    "** Ordenación Inserción - Inicialización Aleatorio (Caso Promedio: O(n^2)) **",
    VECTORES_N,
    tiempos_aleatorio,
    [1.8, 2.0, 2.2]
)


# ------------------------------------------------------------------------------
# 2. Ordenación Shell (Ejercicio 4)
# ------------------------------------------------------------------------------

# Helper para medir Shell Sort, pasando la función de secuencia
def medir_tiempo_shell(n, inicializar_func, secuencia_func):
    """
    Wrapper que crea una función temporal para ord_shell con la secuencia 
    específica, compatible con medir_tiempo_algoritmo.
    """
    def shell_sort_wrapper(v):
        # La secuencia se calcula dentro del wrapper para usar el tamaño actual del vector (len(v))
        inc = secuencia_func(len(v)) 
        return ord_shell(v, inc)
    
    return medir_tiempo_algoritmo(shell_sort_wrapper, inicializar_func, n)


print("=" * 70)
print("EJERCICIO 4: ANÁLISIS DE ORDENACIÓN SHELL (4 TABLAS - Vector Aleatorio)")
print("=" * 70)

SHELL_SECUENCIAS = [
    ("Hibbard", secuencia_hibbard, [1.4, 1.5, 1.6]),    # O(n^1.5)
    ("Knuth", secuencia_knuth, [1.2, 1.3, 1.4]),        # O(n log^2 n) ~ O(n^1.3)
    ("Sedgewick", secuencia_sedgewick, [1.2, 1.33, 1.4]), # O(n^1.33)
    ("Ciura", secuencia_ciura, [1.2, 1.25, 1.3])       # O(n^1.25)
]

for nombre, func_secuencia, exponents in SHELL_SECUENCIAS:
    tiempos = []
    print(f"\nCalculando tiempos para Ordenación Shell con secuencia {nombre}...")
    for n in VECTORES_N:
        # Se mide el tiempo en vectores aleatorios, como pide el enunciado
        t = medir_tiempo_shell(n, aleatorio, func_secuencia)
        tiempos.append(t)
    
    print_tabla(
        f"** Ordenación Shell - Secuencia {nombre} **",
        VECTORES_N,
        tiempos,
        exponents
    )
