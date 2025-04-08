#coding = utf-8
#Un deposito de materiales de constuccion desea implementar  un sistema que le permita identificar la cantidad de materiales que se 
#despachan por 5 grandes categorías que se utilizan en la construcción de viviendas: 
#1.Cimentación
#2.Estructura
#3.Techos
#4.Acabados
#5.Tuberías
#Para ello, simulará el despacho de 1000 ordenes que contienen combinaciones de valores de cada una de las categorías. La orden contiene para cada categoría una cantidad de
#productos con valor aleatorio que puede ser entre el rango [0;10]. Todas las ordenes tienen registros de cada categoría de producto, aún si tienen valor cero.
#Se desea identificar de ese total de órdenes, cuantas son consideradas “ordenes nulas”, es decir, aquellas que tienen el valor de 0 en cada una de las categorías.
#Se sea identificar de ese total de órdenes, cuantas son consideradas “prioritarias”, es decir, aquellas que tienen el valor de 10 en cada una de las categorías.
#El programa al final visualizará entre los resultados, cuantas ordenes fueron “nulas” y cuántas fueron “prioritarias”, así como el porcentaje que representan del total de ordenes simuladas.
#El programa debe:
#Implementar una función calcula_total_ordenes, que recibe como parámetros un diccionario de órdenes y el criterio de búsqueda. Si el criterio es “nulas”, se contabilizarán todas las ordenes que tienen valor “0”. Si el criterio es “prioritaria”, se
#contabilizarán todas las ordenes que tienen valor “10”.
import random

def calcula_total_ordenes(diccionario_ordenes, criterio):
    total = 0
    for orden in diccionario_ordenes.values():
        if orden["Criterio"] == criterio:
            total += 1
    return total

# Crear el diccionario de órdenes
diccionario_ordenes = {}
for i in range(1, 1001):
    valores_categorias = {
        "cimentacion": random.randint(0, 10),
        "estructura": random.randint(0, 10),
        "techos": random.randint(0, 10),
        "acabados": random.randint(0, 10),
        "tuberias": random.randint(0, 10),
    }
    if all(valor == 0 for valor in valores_categorias.values()):
        criterio = "nula"
    elif all(valor == 10 for valor in valores_categorias.values()):
        criterio = "prioritaria"

diccionario_ordenes[i] = {"Valores": valores_categorias, "Criterio": criterio}

print(diccionario_ordenes)
# Calcular totales
total_nulas = calcula_total_ordenes(diccionario_ordenes, "nula")
total_prioritarias = calcula_total_ordenes(diccionario_ordenes, "prioritaria")

# Calcular porcentajes
porcentaje_nulas = (total_nulas / 1000) * 100
porcentaje_prioritarias = (total_prioritarias / 1000) * 100

# Mostrar resultados
print(f"Total de órdenes nulas: {total_nulas} ({porcentaje_nulas:.2f}%)")
print(f"Total de órdenes prioritarias: {total_prioritarias} ({porcentaje_prioritarias:.2f}%)")