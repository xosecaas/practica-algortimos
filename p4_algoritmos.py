# Hugo Bouza Fernández
# Rafael Casás Lamas
# Xosé Castro González

import time
import random
from collections.abc import Callable

# Medición de tiempo
def microsegundos():
    return time.perf_counter_ns() // 1000

# Funciones de dispersión
def dispersionA(clave : str, tamTabla : int)-> int:
    n = min(8, len(clave))
    valor = ord(clave[0])
    for i in range(1, n):
        valor += ord(clave[i])
    return valor % tamTabla

def dispersionB(clave : str, tamTabla : int)-> int:
    n = min(8, len(clave))
    valor = ord(clave[0])
    for i in range(1, n):
        valor = ((valor * 32) + ord(clave[i])) # desplazamiento de 5 bits
    return valor % tamTabla # a multiplicar por 32


# EJERCICIO 1
# Tablas de dispersión abierta 
# (factor de carga aproximado de  λ = 1,0(N = 19069))
class Nodo:
    def __init__(self, clave, sinonimos):
        self.clave = clave
        self.sinonimos = sinonimos
        self.siguiente = None 

class TablaAbierta:
    def __init__(self, tam, dispersion):
        # Inicialización del vector de punteros/cabeceras
        self.tabla = [None] * tam
        self.tam = tam
        self.dispersion = dispersion

    def buscar(self, clave):
        # Calcular el índice de dispersión
        indice = self.dispersion(clave, self.tam)
        actual = self.tabla[indice]
        comparaciones = 0
        # Recorrer la lista enlazada
        while actual is not None:
            if actual.clave == clave:
                # Retornar los sinónimos y el número de comparaciones
                return actual.sinonimos, comparaciones
            comparaciones += 1  # Incrementar comparaciones
            actual = actual.siguiente
            # Retornar None y el número de comparaciones en caso de fracaso
        return None, comparaciones

    def insertar(self, clave, sinonimos):
        pos, colisiones_al_buscar = self.buscar(clave)
        if pos is None:
            indice = self.dispersion(clave, self.tam)
            nuevo_nodo = Nodo(clave, sinonimos)
            nuevo_nodo.siguiente = self.tabla[indice]
            self.tabla[indice] = nuevo_nodo
            # Devolver las colisiones 
            return colisiones_al_buscar
        else:
            # Si ya existe, el procedimiento termina sin insertar
            return 0

    def mostrar(self):
        print("{")
        for i in range(self.tam):
            actual = self.tabla[i]
            if actual is None:
                print(f"{i}- [ ]")
            else:
                elementos = []
                while actual is not None:
                    elementos.append(f"({actual.clave})")
                    actual = actual.siguiente
                print(f"{i}- [ {' '.join(elementos)} ]")
        print("}")

# Tablas de dispersión cerrada 
# (factor de carga aproximado de  λ = 0,5 (N = 38197))
def exploracion_lineal(pos_ini: int, intento: int)-> int:
    return pos_ini + intento

def exploracion_cuadratica(pos_ini: int, intento: int)-> int:
    return pos_ini + intento * intento

def exploracion_doble(pos_ini: int, intento: int)-> int:
    R = 10007  # Número primo menor que el tamaño de la tabla
    h2 = R - (pos_ini % R)
    return pos_ini + intento * h2

class Entrada:
    def __init__(self):
        self.ocupada = False
        self.clave = None
        self.sinonimos = None

class TablaCerrada:
    def __init__(self, tam : int, dispersion : Callable[[str, int], int],
                    resol_colisiones : Callable[[int, int], int]):
        self.tabla = [Entrada() for _ in range(tam)]
        self.tam = tam
        self.dispersion = dispersion
        self.resol_colisiones = resol_colisiones

    def buscar(self, clave : str)-> tuple[str | None, int]:
        colisiones = 0
        pos_inicial = self.dispersion(clave, self.tam)
        intento = 0
        while intento < self.tam:
            # Calcular posición actual según la estrategia de resolución
            pos_actual = self.resol_colisiones(pos_inicial, intento) % self.tam
            entrada = self.tabla[pos_actual]
            # Si la celda está vacía, la clave no existe
            if not entrada.ocupada:
                return None, colisiones
            # Si encontramos la clave, devolvemos los sinónimos
            if entrada.clave == clave:
                return entrada.sinonimos, colisiones
            # Si hay colisión incrementar contador y seguir buscando
            colisiones += 1
            intento += 1
        # No encontramos la clave después de revisar toda la tabla
        return None, colisiones

    def insertar(self, clave : str, sinonimos : str)-> int:
        colisiones = 0
        pos_inicial = self.dispersion(clave, self.tam)
        intento = 0
        while intento < self.tam:
            # Calcular posición actual según la estrategia de resolución
            pos_actual = self.resol_colisiones(pos_inicial, intento) % self.tam
            entrada = self.tabla[pos_actual]
            # Si la celda está vacía, podemos insertar aquí
            if not entrada.ocupada:
                entrada.clave = clave
                entrada.sinonimos = sinonimos
                entrada.ocupada = True
                return colisiones
            # Si la celda ya contiene la misma clave, actualizamos sinónimos
            if entrada.clave == clave:
                entrada.sinonimos = sinonimos
                return colisiones
            # Colisión con otra clave diferente
            colisiones += 1
            intento += 1
        # Si llegamos aquí, la tabla está llena
        raise Exception("Tabla llena - no se puede insertar")

    def mostrar(self):
        print("{")
        for i in range(self.tam):
            entrada = self.tabla[i]
            if entrada.ocupada:
                print(f"{i}- [ ({entrada.clave}) ]")
            else:
                print(f"{i}- [ ]")
        print("}")


# EJERCICIO 2
def dispersionTestTeoria(clave: str, tam_tabla: int) -> int:
    if clave in ("ANA", "JOSE", "OLGA"):
        return 7
    return 6

def exploracion_dobleTeoria(pos_ini: int, intento: int) -> int:
    R = 5  # Como en el ejemplo de teoría
    h2 = R - (pos_ini % R)
    return pos_ini + intento * h2

def test_tabla_abierta(datos_teoria):
    print("\n*** TEST TABLA ABIERTA")
    tabla = TablaAbierta(11, dispersionTestTeoria)
    coli_ab = 0
    for clave, sinonimos in datos_teoria:
        coli = tabla.insertar(clave, sinonimos)
        coli_ab += coli
    tabla.mostrar()
    print(f"Número total de colisiones al insertar los elementos: {coli_ab}")
    buscar_y_mostrar(tabla, datos_teoria, "CARLOS")

def test_tabla_cerrada(datos_teoria, nombre, resol_colisiones):
    print(f"\n*** TEST TABLA CERRADA {nombre}")
    if nombre == "DOBLE":
        tabla = TablaCerrada(11, dispersionTestTeoria, exploracion_dobleTeoria)
    else:
        tabla = TablaCerrada(11, dispersionTestTeoria, resol_colisiones)
    coli_t = 0
    for clave, sinonimos in datos_teoria:
        coli = tabla.insertar(clave, sinonimos)
        coli_t += coli
    tabla.mostrar()
    print(f"Número total de colisiones al insertar los elementos: {coli_t}")
    buscar_y_mostrar(tabla, datos_teoria, "CARLOS")

def buscar_y_mostrar(tabla, datos_teoria, clave_no_existe):
    for clave, _ in datos_teoria:
        resultado, coli = tabla.buscar(clave)
        print(f"Al buscar: {clave}, encuentro: {clave}, colisiones: {coli}")
    resultado, coli = tabla.buscar(clave_no_existe)
    print(f"No encuentro: {clave_no_existe}, colisiones: {coli}")

def test_teoria():
    print("=" * 60)
    print("VALIDACIÓN CON EJEMPLO DE TEORÍA")
    print("=" * 60)
    # Datos de prueba del ejemplo de teoría
    datos_teoria = [
        ("ANA", "sinonimos_ANA"),
        ("LUIS", "sinonimos_LUIS"), 
        ("JOSE", "sinonimos_JOSE"),
        ("OLGA", "sinonimos_OLGA"),
        ("ROSA", "sinonimos_ROSA"),
        ("IVAN", "sinonimos_IVAN")]
    # Ejecutar todos los tests
    test_tabla_abierta(datos_teoria)
    test_tabla_cerrada(datos_teoria, "LINEAL", exploracion_lineal)
    test_tabla_cerrada(datos_teoria, "CUADRÁTICA", exploracion_cuadratica)
    test_tabla_cerrada(datos_teoria, "DOBLE", None)

test_teoria()


# EJERCICIOS 3 Y 4
# Leer datos del archivo
def leer_sinonimos(nombre="sinonimos.txt"):
    datos = []
    with open(nombre, "r", encoding="utf-8") as f:
        for linea in f:
            clave, sinonimos = linea.strip().split("\t", 1)
            datos.append((clave, sinonimos))
    return datos

datos = leer_sinonimos()

# Configuraciones de tablas
configuraciones = [
    # (Nombre, Tipo, Tamaño, Dispersión, Resolución, [Cota1, Cota2, Cota3])
    ("TablaAbierta dispersionA", "abierta", 
     19069, dispersionA, None, [0.9, 1.0, 1.1]),
    ("TablaAbierta dispersionB", "abierta", 
     19069, dispersionB, None, [0.9, 1.0, 1.1]),
    ("TablaCerrada dispersionA exploracion_lineal", "cerrada", 
     38197, dispersionA, exploracion_lineal, [0.9, 1.0, 1.1]),
    ("TablaCerrada dispersionB exploracion_lineal", "cerrada", 
     38197, dispersionB, exploracion_lineal, [0.9, 1.0, 1.1]),
    ("TablaCerrada dispersionA exploracion_cuadratica", "cerrada", 
     38197, dispersionA, exploracion_cuadratica, [0.9, 1.0, 1.1]),
    ("TablaCerrada dispersionB exploracion_cuadratica", "cerrada", 
     38197, dispersionB, exploracion_cuadratica, [0.9, 1.0, 1.1]),
    ("TablaCerrada dispersionA exploracion_doble", "cerrada", 
     38197, dispersionA, exploracion_doble, [0.9, 1.0, 1.1]),
    ("TablaCerrada dispersionB exploracion_doble", "cerrada", 
     38197, dispersionB, exploracion_doble, [0.9, 1.0, 1.1]),]

# EJERCICIO 3: Insertar todos los datos y contar colisiones totales
print("\n" + "=" * 60)
print("COLISIONES TOTALES AL INSERTAR")
print("=" * 60)

resultados_insertar = {}

for nombre, tipo, tam, disp, resol, cotas in configuraciones:
    print(f"\n*** {nombre}")
    if tipo == "abierta":
        tabla = TablaAbierta(tam, disp)
    else:
        tabla = TablaCerrada(tam, disp, resol)
    colisiones_totales = 0
    elementos_insertados = 0
    print(f"Insertando {len(datos)} elementos...", end=" ")
    for clave, sinonimos in datos:
        colisiones = tabla.insertar(clave, sinonimos)
        colisiones_totales += colisiones
        if colisiones >= 0:  # Si se insertó (no era duplicado)
            elementos_insertados += 1
    print(f"Elementos insertados: {elementos_insertados}")
    print(f"Número total de colisiones: {colisiones_totales}")
    # Resultados para ejercicio 4
    resultados_insertar[nombre] = {
        'tabla': tabla,
        'colisiones_totales': colisiones_totales,
        'elementos_insertados': elementos_insertados,
        'cotas': cotas}

# EJERCICIO 4: Complejidad computacional de la búsqueda
print("\n" + "=" * 60)
print("COMPLEJIDAD COMPUTACIONAL DE BÚSQUEDA")
print("=" * 60)
# Tamaños para el análisis
n_values = [125, 250, 500, 1000, 2000, 4000, 8000, 16000]

# Definir nombres para las cotas
cota_nombres = {
    0.9: " (Cota subestimada)",
    1.0: " (Cota ajustada)",
    1.1: " (Cota sobre-estimada)"}

for config in configuraciones:
    nombre, tipo, tam, disp, resol, cotas = config
    print(f"\n*** {nombre}")
    # Obtener la tabla ya poblada y las cotas
    tabla_info = resultados_insertar[nombre]
    tabla = tabla_info['tabla']
    cotas_tabla = tabla_info['cotas']
    print("Buscando n elementos...")
    # Construir cabecera dinámica basada en las cotas
    header = f"{'n':>8} {'t(n)':>14}"
    for cota in cotas_tabla:
        cota_nombre = cota_nombres.get(cota, f"")
        header += f" {'t(n)/n^' + str(cota) + cota_nombre:>35}"
    header += f" {'Colisiones':>14}"
    print(header)
    print("-" * (8 + 14 + 35 * len(cotas_tabla) + 14 + 10))
    tiempos = []
    colisiones_totales_busqueda = []
    asterisco_list = []
    
    # Medir tiempo de búsqueda
    def buscar_n_elementos(tabla_obj, claves):
        colisiones_totales = 0
        for clave, _ in claves:
            _, colisiones = tabla_obj.buscar(clave)
            colisiones_totales += colisiones
        return colisiones_totales
    
    for n in n_values:
        if n > len(datos):
            break
        
        # Repetir 3 veces la medición para un resultado más robusto
        t_total = 0
        colisiones_total = 0
        asterisco_count = 0
        for repeticion in range(3):
            # Seleccionar nuevas claves aleatorias en cada repetición
            claves_a_buscar = random.sample(datos, n)

            # Medición de tiempo
            t_directo = microsegundos()
            colisiones_n = buscar_n_elementos(tabla, claves_a_buscar)
            t_directo = microsegundos() - t_directo
            if t_directo < 1000:  # Umbral de confianza
                asterisco_count += 1
                k = 1000  # Número de iteraciones
                # Medir K ejecuciones completas
                t1 = microsegundos()
                for _ in range(k):
                    # Usar una nueva muestra en cada iteración
                    claves_iteracion = random.sample(datos, n)
                    buscar_n_elementos(tabla, claves_iteracion)
                t2 = microsegundos()
                t_total_rep = t2 - t1
                t_directo = t_total_rep / k
            t_total += t_directo
            colisiones_total += colisiones_n
        
        # Promediar resultados
        t_avg = t_total / 3
        colisiones_avg = colisiones_total / 3
        tiempos.append(t_avg)
        colisiones_totales_busqueda.append(colisiones_avg)
        # Considerar asterisco si al menos 2 de 3 mediciones lo requieren
        asterisco_list.append(asterisco_count >= 2)
        
        # Calcular ratios
        t = t_avg
        ratios = []
        for cota in cotas_tabla:
            ratio = t / (n ** cota) if n > 0 else 0
            ratios.append(ratio)
        
        # Imprimir fila
        n_str = f"*{n}" if asterisco_list[-1] else str(n)
        fila = f"{n_str:>8} {t:>14.4f}"
        for ratio in ratios:
            fila += f" {ratio:>35.8f}"
        # Mostrar colisiones promedio como entero
        fila += f" {int(round(colisiones_avg)):>14}"
        print(fila)
    
    print("-" * (8 + 14 + 35 * len(cotas_tabla) + 14 + 10))
    
