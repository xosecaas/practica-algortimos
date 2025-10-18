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


# INICIALIZACIÓN DE VECTORES
def aleatorio(n):
    v = list(range(n))
    for i in range(n):
        v[i] = random.randint(-n, n)
    return v

def ascendente(n):
    return list(range(1, n+1)) 

def descendente(n):
    return list(range(n, 0, -1))


# EJERCICIO 1
# Algoritmo ordenación por inserción
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

# Algoritmo ordenación Shell
def ord_shell(v, inc):
    vector = v.copy()  # Copia para no modificar el original
    n = len(vector)
    m = len(inc)  
    for k in range(m-1, -1, -1):
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
    return sec 

def secuencia_knuth(n):
    sec = []
    k = 1
    while True:
        incremento = (3**k - 1) // 2
        if incremento > n // 2:
            break
        sec.append(incremento)
        k += 1    
    return sec

def secuencia_sedgewick(n):
    sec = [1]
    k = 1
    while True:
        incremento = 4**k + 3 * (2**(k-1)) + 1
        if incremento > n // 2:
            break
        sec.append(incremento)
        k += 1
    return sec

def secuencia_ciura(n):
    base = [1, 4, 10, 23, 57, 132, 301, 701, 1750]
    sec = []   
    for inc in base:    # Incrementos base
        if inc <= n // 2:
            sec.append(inc)
    if sec:    # Extender secuencia para vectores grandes
        ultimo = sec[-1]
        while ultimo <= n // 2:
            proximo_inc = round(ultimo * 2.25)
            if proximo_inc > n // 2:
                break
            if proximo_inc > ultimo:
                sec.append(proximo_inc)
                ultimo = proximo_inc
            else:
                break
    return sec

# Validación del funcionamiento
def esta_ordenado(v):
    for i in range(len(v) - 1):
        if v[i] > v[i + 1]:
            return False
    return True

def test_algoritmos(n=20):
    print("=" * 70)
    print("VALIDACIÓN DE ALGORITMOS DE ORDENACIÓN")
    print("=" * 70)  
    v_aleatorio = aleatorio(n)
    v_ascendente = ascendente(n)
    v_descendente = descendente(n)
    # --- Ordenación por Inserción ---
    print(f"\n--- Ordenación por Inserción (n={n}) ---")
    v_ord_ins_asc = ord_insercion(v_ascendente.copy())  # Vector Ascendente
    print(f"\nVector Ascendente (Mejor Caso):")
    print(f"  Original: {v_ascendente}")
    print(f"  Ordenado: {v_ord_ins_asc}")
    print(f"  ¿Ordenado? {esta_ordenado(v_ord_ins_asc)}")
    v_ord_ins_desc = ord_insercion(v_descendente.copy())  # Vector Descendente
    print(f"\nVector Descendente (Peor Caso):")
    print(f"  Original: {v_descendente}")
    print(f"  Ordenado: {v_ord_ins_desc}")
    print(f"  ¿Ordenado? {esta_ordenado(v_ord_ins_desc)}")
    v_ord_ins_aleat = ord_insercion(v_aleatorio.copy())  # Vector Aleatorio
    print(f"\nVector Aleatorio (Caso Promedio):")
    print(f"  Original: {v_aleatorio}")
    print(f"  Ordenado: {v_ord_ins_aleat}")
    print(f"  ¿Ordenado? {esta_ordenado(v_ord_ins_aleat)}")
    # --- Ordenación Shell ---
    secuencias = {"Hibbard": secuencia_hibbard,"Knuth": secuencia_knuth,
                  "Sedgewick": secuencia_sedgewick,"Ciura": secuencia_ciura}   
    print(f"\n--- Ordenación Shell (n={n}) ---")
    tipos_vectores = [("Ascendente", v_ascendente.copy()),
                      ("Descendente", v_descendente.copy()), 
                      ("Aleatorio", v_aleatorio.copy())]
    for tipo_nombre, vector_original in tipos_vectores:
        print(f"\n Vector {tipo_nombre}:")
        print(f"  Original: {vector_original}")
        for nombre, func_sec in secuencias.items():
            inc = func_sec(n)
            v_ord_shell = ord_shell(vector_original.copy(), inc)
            print(f"  - Secuencia {nombre}: {inc}")
            print(f"    Vector Ordenado: {v_ord_shell}")
            print(f"    ¿Ordenado? {esta_ordenado(v_ord_shell)}")

test_algoritmos() # Ejecutar validación
print("\n")


# EJERCICIOS 3,4 Y 5 (ANÁLISIS DE COMPLEJIDAD Y GENERACIÓN DE TABLAS)
VECTORES_N = [500, 1000, 2000, 4000, 8000, 16000, 32000] 

# Función auxiliar para imprimir las tablas en el formato requerido  
def print_tabla(titulo, n_values, tiempos, k_exponents, asterisco_list):      
    header_str = f"{"n":>10} {"t(n)":>20}"
    cota = ["(Cota subestimada)", "(Cota ajustada)", "(Cota sobre-estimada)"]
    for i, k in enumerate(k_exponents):
        header_str += f" {"t(n)/n^" + f'{k:.2f} {cota[i]} ':>40}"
    print("-" * (10 + 20 + 42 * len(k_exponents)))
    print(f"{titulo.upper()}")
    print("-" * (10 + 20 + 42 * len(k_exponents)))
    print(header_str)
    print("-" * (10 + 20 + 42 * len(k_exponents)))
    for i, n in enumerate(n_values):
        t = tiempos[i]
        asterisco = asterisco_list[i]
        n_str = f"*{n}" if asterisco else str(n)
        line = f"{n_str:>10} {t:>20.8f}"
        for k in k_exponents:
            ratio = t / (n**k)
            line += f" {ratio:>38.8f}"
        print(line)
    print("-" * (10 + 20 + 42 * len(k_exponents)))
    print()

# Repetir 3 veces el proceso de cálculo y generación de tablas para tratar de
# reducir las mediciones anómalas
for _ in range(3):
    # --- Ordenación por Inserción ---
    print("=" * 70)
    print("ANÁLISIS DE ORDENACIÓN POR INSERCIÓN (3 TABLAS)")
    print("=" * 70)
    # Mejor Caso (Vector ordenado ascendentemente) -> Complejidad O(n)
    tiempos_asc = []
    asterisco_asc = []
    for n in VECTORES_N:
        t, asterisco = medir_tiempo_algoritmo(ord_insercion, ascendente, n)
        tiempos_asc.append(t)
        asterisco_asc.append(asterisco)
    print_tabla(
        "** Ordenación Inserción - Ascendente (Mejor Caso: O(n)) **",
        VECTORES_N,
        tiempos_asc,
        [0.8, 1.0, 1.2],
        asterisco_asc
    )
    # Peor Caso (Vector ordenado descendentemente) -> Complejidad O(n^2)
    tiempos_desc = []
    asterisco_desc = []
    for n in VECTORES_N:
        t, asterisco = medir_tiempo_algoritmo(ord_insercion, descendente, n)
        tiempos_desc.append(t)
        asterisco_desc.append(asterisco)
    print_tabla(
        "** Ordenación Inserción - Descendente (Peor Caso: O(n^2)) **",
        VECTORES_N,
        tiempos_desc,
        [1.8, 2.0, 2.2],
        asterisco_desc
    )
    # Caso Promedio (Vector aleatorio) -> Complejidad O(n^2)
    tiempos_aleatorio = []
    asterisco_aleatorio = []
    for n in VECTORES_N:
        t, asterisco = medir_tiempo_algoritmo(ord_insercion, aleatorio, n)
        tiempos_aleatorio.append(t)
        asterisco_aleatorio.append(asterisco)

    print_tabla(
        "** Ordenación Inserción - Aleatorio (Caso Promedio: O(n^2)) **",
        VECTORES_N,
        tiempos_aleatorio,
        [1.8, 2.0, 2.2],
        asterisco_aleatorio
    )

    # --- Ordenación Shell ---
    # Helper para medir Shell Sort, pasando la función de secuencia
    def medir_tiempo_shell(n, inicializar_func, secuencia_func):
        def shell_sort_wrapper(v):
            inc = secuencia_func(len(v)) 
            return ord_shell(v, inc)  
        return medir_tiempo_algoritmo(shell_sort_wrapper, inicializar_func, n)

    print("=" * 70)
    print("ANÁLISIS DE ORDENACIÓN SHELL (4 TABLAS - Vector Aleatorio)")
    print("=" * 70)

    SHELL_SECUENCIAS = [
        ("Hibbard", secuencia_hibbard, [1.15, 1.22, 1.30]),    # O(n^1.22)
        ("Knuth", secuencia_knuth, [1.15, 1.25, 1.35]),        # O(n^1.25)
        ("Sedgewick", secuencia_sedgewick, [1.05, 1.16, 1.25]), # O(n^1.16) 
        ("Ciura", secuencia_ciura, [1.10, 1.18, 1.25])       # O(n^1.18)
    ]

    for nombre, func_secuencia, exponents in SHELL_SECUENCIAS:
        tiempos = []
        asterisco_list = []
        for n in VECTORES_N:
            t, asterisco = medir_tiempo_shell(n, aleatorio, func_secuencia)
            tiempos.append(t)
            asterisco_list.append(asterisco)
    
        print_tabla(
            f"** Ordenación Shell - Secuencia {nombre} **",
            VECTORES_N,
            tiempos,
            exponents,
            asterisco_list
        )
