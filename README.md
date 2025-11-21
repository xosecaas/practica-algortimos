# practica-algortimos

https://prod.liveshare.vsengsaas.visualstudio.com/join?6FBCDFBA66A607EDA9BB6855CAF55C97C149

============================================================
VALIDACIÓN CON EJEMPLO DE TEORÍA
============================================================

*** TEST TABLA ABIERTA
{
0- [ ]
1- [ ]
2- [ ]
3- [ ]
4- [ ]
5- [ ]
6- [ (IVAN) (ROSA) (LUIS) ]
7- [ (OLGA) (JOSE) (ANA) ]
8- [ ]
9- [ ]
10- [ ]
}
Numero total de colisiones al insertar los elementos: 6
Al buscar: ANA, encuentro: ANA, colisiones: 2
Al buscar: LUIS, encuentro: LUIS, colisiones: 2
Al buscar: JOSE, encuentro: JOSE, colisiones: 1
Al buscar: OLGA, encuentro: OLGA, colisiones: 0
Al buscar: ROSA, encuentro: ROSA, colisiones: 1
Al buscar: IVAN, encuentro: IVAN, colisiones: 0
No encuentro: CARLOS, colisiones: 3

** TEST TABLA CERRADA LINEA
{
0- [ (IVAN) ]
1- [ ]
2- [ ]
3- [ ]
4- [ ]
5- [ ]
6- [ (LUIS) ]
7- [ (ANA) ]
8- [ (JOSE) ]
9- [ (OLGA) ]
10- [ (ROSA) ]
}
Numero total de colisiones al insertar los elementos: 12
Al buscar: ANA, encuentro: ANA, colisiones: 0
Al buscar: LUIS, encuentro: LUIS, colisiones: 0
Al buscar: JOSE, encuentro: JOSE, colisiones: 1
Al buscar: OLGA, encuentro: OLGA, colisiones: 2
Al buscar: ROSA, encuentro: ROSA, colisiones: 4
Al buscar: IVAN, encuentro: IVAN, colisiones: 5
No encuentro: CARLOS, colisiones: 6

*** TEST TABLA CERRADA CUADRATICA
{
0- [ (OLGA) ]
1- [ ]
2- [ ]
3- [ ]
4- [ (IVAN) ]
5- [ ]
6- [ (LUIS) ]
7- [ (ANA) ]
8- [ (JOSE) ]
9- [ ]
10- [ (ROSA) ]
}
Numero total de colisiones al insertar los elementos: 8
Al buscar: ANA, encuentro: ANA, colisiones: 0
Al buscar: LUIS, encuentro: LUIS, colisiones: 0
Al buscar: JOSE, encuentro: JOSE, colisiones: 1
Al buscar: OLGA, encuentro: OLGA, colisiones: 2
Al buscar: ROSA, encuentro: ROSA, colisiones: 2
Al buscar: IVAN, encuentro: IVAN, colisiones: 3
No encuentro: CARLOS, colisiones: 5

*** TEST TABLA CERRADA DOBLE
{
0- [ (IVAN) ]
1- [ ]
2- [ (OLGA) ]
3- [ (ROSA) ]
4- [ ]
5- [ ]
6- [ (LUIS) ]
7- [ (ANA) ]
8- [ ]
9- [ ]
10- [ (JOSE) ]
}
Numero total de colisiones al insertar los elementos: 9
Al buscar: ANA, encuentro: ANA, colisiones: 0
Al buscar: LUIS, encuentro: LUIS, colisiones: 0
Al buscar: JOSE, encuentro: JOSE, colisiones: 1
Al buscar: OLGA, encuentro: OLGA, colisiones: 2
Al buscar: ROSA, encuentro: ROSA, colisiones: 2
Al buscar: IVAN, encuentro: IVAN, colisiones: 4
No encuentro: CARLOS, colisiones: 5

C:\Users\Usuario\OneDrive\Escritorio\Uni\2º\Algoritmos\practicas\p4>C:\Users\Usuario\AppData\Local\Programs\Python\Python313\python.exe c:/Users/Usuario/OneDrive/Escritorio/Uni/2º/Algoritmos/practicas/p4/p4_algoritmos.py
============================================================
VALIDACIÓN CON EJEMPLO DE TEORÍA
============================================================

*** TEST TABLA ABIERTA
{
0- [ ]
1- [ ]
2- [ ]
3- [ ]
4- [ ]
5- [ ]
6- [ (IVAN) (ROSA) (LUIS) ]
7- [ (OLGA) (JOSE) (ANA) ]
8- [ ]
9- [ ]
10- [ ]
}
Numero total de colisiones al insertar los elementos: 6
Al buscar: ANA, encuentro: ANA, colisiones: 3
Al buscar: LUIS, encuentro: LUIS, colisiones: 3
Al buscar: JOSE, encuentro: JOSE, colisiones: 2
Al buscar: OLGA, encuentro: OLGA, colisiones: 1
Al buscar: ROSA, encuentro: ROSA, colisiones: 2
Al buscar: IVAN, encuentro: IVAN, colisiones: 1
No encuentro: CARLOS, colisiones: 3

** TEST TABLA CERRADA LINEAL
{
0- [ (IVAN) ]
1- [ ]
2- [ ]
3- [ ]
4- [ ]
5- [ ]
6- [ (LUIS) ]
7- [ (ANA) ]
8- [ (JOSE) ]
9- [ (OLGA) ]
10- [ (ROSA) ]
}
Numero total de colisiones al insertar los elementos: 12
Al buscar: ANA, encuentro: ANA, colisiones: 0
Al buscar: LUIS, encuentro: LUIS, colisiones: 0
Al buscar: JOSE, encuentro: JOSE, colisiones: 1
Al buscar: OLGA, encuentro: OLGA, colisiones: 2
Al buscar: ROSA, encuentro: ROSA, colisiones: 4
Al buscar: IVAN, encuentro: IVAN, colisiones: 5
No encuentro: CARLOS, colisiones: 6

*** TEST TABLA CERRADA CUADRÁTICA
{
0- [ (OLGA) ]
1- [ ]
2- [ ]
3- [ ]
4- [ (IVAN) ]
5- [ ]
6- [ (LUIS) ]
7- [ (ANA) ]
8- [ (JOSE) ]
9- [ ]
10- [ (ROSA) ]
}
Numero total de colisiones al insertar los elementos: 8
Al buscar: ANA, encuentro: ANA, colisiones: 0
Al buscar: LUIS, encuentro: LUIS, colisiones: 0
Al buscar: JOSE, encuentro: JOSE, colisiones: 1
Al buscar: OLGA, encuentro: OLGA, colisiones: 2
Al buscar: ROSA, encuentro: ROSA, colisiones: 2
Al buscar: IVAN, encuentro: IVAN, colisiones: 3
No encuentro: CARLOS, colisiones: 5

*** TEST TABLA CERRADA DOBLE
{
0- [ (IVAN) ]
1- [ ]
2- [ (OLGA) ]
3- [ (ROSA) ]
4- [ ]
5- [ ]
6- [ (LUIS) ]
7- [ (ANA) ]
8- [ ]
9- [ ]
10- [ (JOSE) ]
}
Numero total de colisiones al insertar los elementos: 9
Al buscar: ANA, encuentro: ANA, colisiones: 0
Al buscar: LUIS, encuentro: LUIS, colisiones: 0
Al buscar: JOSE, encuentro: JOSE, colisiones: 1
Al buscar: OLGA, encuentro: OLGA, colisiones: 2
Al buscar: ROSA, encuentro: ROSA, colisiones: 2
Al buscar: IVAN, encuentro: IVAN, colisiones: 4
No encuentro: CARLOS, colisiones: 5
