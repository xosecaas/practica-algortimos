# Hugo Bouza Fernández
# Rafael Casás Lamas
# Xosé Castro González

import random
import time

# Medición de tiempo
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

# Wrapper para medir Quicksort con un umbral fijo
def medir_t_quicksort(n, inicializar_func, umbral):
    def quicksort_wrapper(v):
        ord_rapida(v, umbral) 
    return medir_tiempo_algoritmo(quicksort_wrapper, inicializar_func, n)

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

# Algoritmo ordenación por inserción
def ord_insercion(v):
    n = len(v)
    for i in range(1, n):
        x = v[i]
        j = i - 1
        while j >= 0 and v[j] > x:
            v[j + 1] = v[j]
            j = j - 1
        v[j + 1] = x


# EJERCICIO 1
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
        while j > i:
            i += 1
            while v[i] < pivote:
                i += 1
            while v[j] > pivote: 
                j -= 1   
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


# EJERCICIOS 2 y 3
def test_ord_rapida(tipo_vector, tamaño, umbral):
    # Crear el vector según el tipo
    if tipo_vector == "ascendente":
        v = ascendente(tamaño)
    elif tipo_vector == "descendente":
        v = descendente(tamaño)
    elif tipo_vector == "aleatorio":
        v = aleatorio(tamaño)
    else:
        print("Tipo de vector no válido")
        return False
    v_copia = v.copy() # Hacer copia para verificación
    print(f"Configuración: {tipo_vector}, tamaño={tamaño}, umbral={umbral}")
    print(f"Vector original: {v}")
    ord_rapida(v, umbral) # Ejecutar ordenación
    correcto = v == sorted(v_copia) # Verificar resultado
    print(f"Vector ordenado: {v}")
    print(f"¿Ordenado? {correcto}")
    print()

test_ord_rapida("aleatorio",10,1)
test_ord_rapida("ascendente",15,10)
test_ord_rapida("descendente",20,100)


# EJERCICIOS 4 Y 5
def print_tabla(titulo, n_values, tiempos, k_exponents, asterisco_list):      
    # Ajuste de ancho de columna para hacerla más estrecha
    col_n = 8
    col_t = 16
    col_r = 35
    # Definir nombres para las cotas
    cotas = ["(Cota subestimada)", "(Cota justa)", "(Cota sobre-estimada)"]
    header_str = f"{"n":>{col_n}} {"t(n)":>{col_t}}"
    # Construir cabecera de las cotas: t/n^k (Nombre de cota)
    for i, k in enumerate(k_exponents):
        cota_label = f"t/n^{k:.2f} {cotas[i] if i < len(cotas) else ''}"
        header_str += f" {cota_label:>{col_r}}"
    total_width = col_n + col_t + (col_r * len(k_exponents)) + 10
    line_separator = "-" * total_width
    print(line_separator)
    print(f"{titulo.upper()}")
    print(line_separator)
    print(header_str)
    print(line_separator)
    # Imprimir filas de datos
    for i, n in enumerate(n_values):
        t = tiempos[i]
        asterisco = asterisco_list[i]
        n_str = f"*{n}" if asterisco else str(n)
        line = f"{n_str:>{col_n}} {t:>{col_t}.8f}"
        for k in k_exponents:
            ratio = t / (n**k) if n > 0 else 0
            line += f" {ratio:>{col_r}.8f}"
        print(line)
    print(line_separator)
    print()

# Tamaños de vector para el análisis
VECTORES_N = [500, 1000, 2000, 4000, 8000, 16000, 32000] 

# Parámetros para escenarios
UMBRALES = [1, 10, 100]
ESCENARIOS = [
    ("Aleatorio", aleatorio),
    ("Ascendente", ascendente), 
    ("Descendente", descendente)]
COTAS_POR_ESCENARIO = {
    ("Aleatorio", 1): [1.05, 1.10, 1.15],
    ("Aleatorio", 10): [1.07, 1.12, 1.17], 
    ("Aleatorio", 100): [1.03, 1.08, 1.13],
    ("Ascendente", 1): [1.03, 1.08, 1.13],
    ("Ascendente", 10): [1.07, 1.12, 1.17],
    ("Ascendente", 100): [1.09, 1.14, 1.21],
    ("Descendente", 1): [1.03, 1.08, 1.13],
    ("Descendente", 10): [1.07, 1.12, 1.17],
    ("Descendente", 100): [1.09, 1.14, 1.21]}

# Imprimir escenarios
for umbral in UMBRALES:
    print("-" * 120)
    print(f"** ANÁLISIS DE ORDENACIÓN RÁPIDA - UMBRAL = {umbral} **")
    print("-" * 120)
    for nombre_escenario, func_inicializar in ESCENARIOS:
        tiempos = []
        asterisco_list = []
        # Obtener las cotas específicas para este escenario y umbral
        exponentes = COTAS_POR_ESCENARIO.get((nombre_escenario, umbral))
        # Medir para todos los valores de N
        for n in VECTORES_N:
            # Repetir 3 veces la medición para un resultado más robusto
            t_total = 0
            asterisco_count = 0
            for _ in range(3):
                t, asterisco = medir_t_quicksort(n, func_inicializar, umbral)
                t_total += t
                if asterisco:
                    asterisco_count += 1
            t_avg = t_total / 3
            tiempos.append(t_avg)
            # Considerar asterisco si al menos 2 de 3 mediciones lo requieren
            asterisco_list.append(asterisco_count >= 2) 

        # Generar Tabla
        print_tabla(
            f"**Ordenación Rápida - {nombre_escenario} (Umbral = {umbral})**",
            VECTORES_N,
            tiempos,
            exponentes,  # ← Usar las cotas específicas
            asterisco_list)
