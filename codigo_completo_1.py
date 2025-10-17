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
    
    if t_directo < 1000:    # Umbral de confianza: 1000 microsegundos
        k = 1000    # Número de repeticiones
        
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
            # Necesitamos inicializar el vector, pero sin ejecutar el algoritmo
            v = inicializar(n)
        t2 = microsegundos()
        t2_inicializacion = t2 - t1
        
        tiempo_neto = (t1_total - t2_inicializacion) / k
        
        if tiempo_neto <= 0:        # Comprobación para resultados negativos
            return max(t_directo, 1) 
        else:
            return tiempo_neto
    else:
        return t_directo


# INICIALIZACIÓN DE VECTORES
def aleatorio(n):
    v = list(range(n))
    for i in range(n):
        v[i] = random.randint(-n, n)
    return v

def ascendente(n):
    return list(range(1, n + 1)) 

def descendente(n):
    return list(range(n, 0, -1))


# EJERCICIO 1
# Algoritmo ordenación por inserción (Complejidad esperada: O(n) Mejor Caso, O(n^2) Peor/Promedio)
def ord_insercion(v):
    n = len(v)
    vector = v.copy()   # Copia para no modificar el original
    for i in range(1, n):
        x = vector[i]
        j = i - 1       
        while j >= 0 and vector[j] > x:
            vector[j + 1] = vector[j]
            j = j - 1       
        vector[j + 1] = x  
    return vector

# Algoritmo ordenación Shell (Complejidad esperada: Subcuadrática, ej. O(n^1.3) a O(n^1.5))
def ord_shell(v, inc):
    vector = v.copy()  # Copia para no modificar el original
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


# EJERCICIO 2
# Secuencias de incrementos para Shell
def secuencia_hibbard(n):
    sec = []
    k = 1
    while True:
        incremento = 2**k - 1
        if incremento > n // 2:
            break
        sec.append(incremento)
        k += 1
    if not sec or sec[0] != 1:
        if 1 not in sec:
             sec.append(1)
        sec = sorted(list(set(sec)))
    return sec[::-1]

def secuencia_knuth(n):
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
    sec = []
    k = 1
    while True:
        incremento = 4**k + 3 * (2**(k-1)) + 1
        if incremento > n // 2:
            break
        sec.append(incremento)
        k += 1
    if not sec or sec[0] != 1:    # Asegura que 1 esté presente como último paso
        if 1 not in sec:
             sec.append(1)
        sec = sorted(list(set(sec)))
    return sec[::-1] 

def secuencia_ciura(n):
    base = [1, 4, 10, 23, 57, 132, 301, 701, 1750]
    sec = []   
    for inc in base:
        if inc <= n // 2:
            sec.append(inc)
        else:
            break
    if sec and sec[-1] < n // 2:
        ultimo = sec[-1]
        while ultimo <= n // 2:
            proximo_inc = round(ultimo * 2.25) 
            if proximo_inc > n // 2:
                 break
            if proximo_inc > ultimo:     # Evitar bucles infinitos si redondeo no cambia valor
                sec.append(proximo_inc)
                ultimo = proximo_inc
            else:
                break
    if 1 not in sec:    # Asegura que 1 esté presente y elimina duplicados si los hubiera
        sec.append(1)  
    return sorted(list(set(sec)))[::-1]

# Validación del funcionamiento
def esta_ordenado(v):
    for i in range(len(v) - 1):
        if v[i] > v[i + 1]:
            return False
    return True

def test_algoritmos(n=11):
    print("=" * 70)
    print("EJERCICIO 2: VALIDACIÓN DE ALGORITMOS DE ORDENACIÓN")
    print("=" * 70)
    
    # Pruebas de inicialización
    v_aleatorio = aleatorio(n)
    v_ascendente = ascendente(n)
    v_descendente = descendente(n)

    # --- Ordenación por Inserción ---
    print(f"\n--- Ordenación por Inserción (n={n}) ---")
    # Vector Ascendente (Mejor caso para inserción)
    v_ord_ins_asc = ord_insercion(v_ascendente.copy())
    print(f"\nVector Ascendente (Mejor Caso):")
    print(f"  Original: {v_ascendente}")
    print(f"  Ordenado: {v_ord_ins_asc}")
    print(f"  ¿Ordenado? {esta_ordenado(v_ord_ins_asc)}")
    # Vector Descendente (Peor caso para inserción)
    v_ord_ins_desc = ord_insercion(v_descendente.copy())
    print(f"\nVector Descendente (Peor Caso):")
    print(f"  Original: {v_descendente}")
    print(f"  Ordenado: {v_ord_ins_desc}")
    print(f"  ¿Ordenado? {esta_ordenado(v_ord_ins_desc)}")
    # Vector Aleatorio (Caso promedio)
    v_ord_ins_aleat = ord_insercion(v_aleatorio.copy())
    print(f"\nVector Aleatorio (Caso Promedio):")
    print(f"  Original: {v_aleatorio}")
    print(f"  Ordenado: {v_ord_ins_aleat}")
    print(f"  ¿Ordenado? {esta_ordenado(v_ord_ins_aleat)}")

    # --- Ordenación Shell ---
    secuencias = {
        "Hibbard": secuencia_hibbard,
        "Knuth": secuencia_knuth,
        "Sedgewick": secuencia_sedgewick,
        "Ciura": secuencia_ciura
    }
    
    print(f"\n--- Ordenación Shell (n={n}) ---")
    tipos_vectores = [
    ("Ascendente", v_ascendente.copy()),
    ("Descendente", v_descendente.copy()), 
    ("Aleatorio", v_aleatorio.copy())
    ]
    for tipo_nombre, vector_original in tipos_vectores:
        print(f"\n Vector {tipo_nombre}:")
        print(f"  Original: {vector_original}")
        for nombre, func_sec in secuencias.items():
            inc = func_sec(n)
            v_ord_shell = ord_shell(vector_original.copy(), inc)
            print(f"  - Secuencia {nombre}: {inc}")
            print(f"    Vector Ordenado: {v_ord_shell}")
            print(f"    ¿Ordenado? {esta_ordenado(v_ord_shell)}")
        print("-" * 50)

test_algoritmos() # Ejecutar validación
print("\n")


# EJERCICIOS 3,4 Y 5 (ANÁLISIS DE COMPLEJIDAD Y GENERACIÓN DE TABLAS)
VECTORES_N = [500, 1000, 2000, 4000, 8000, 16000, 32000] 

def print_tabla(titulo, n_values, tiempos, k_exponents):    # Función auxiliar para imprimir las tablas en el formato requerido    
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

# --- Ordenación por Inserción ---
print("=" * 70)
print("ANÁLISIS DE ORDENACIÓN POR INSERCIÓN (3 TABLAS)")
print("=" * 70)
# Mejor Caso (Vector ordenado ascendentemente) -> Complejidad O(n)
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

# --- Ordenación Shell ---

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
print("ANÁLISIS DE ORDENACIÓN SHELL (4 TABLAS - Vector Aleatorio)")
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
