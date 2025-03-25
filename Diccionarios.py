#coding=utf-8
from os import system
system("cls")
diccionario = {
    "Nombre" : "Sara",
    "Edad" : "27",
    "Ciudad" : "Medellin",
    "Carrera" : "Medicina"
}
continuar = "si"

while continuar == "si":
    nuevoElemento = input("Ingresa un nuevo elemento a la lista: \n")
    nuevaDefinicion = input("Ingresa la definicion del elemento: \n")
    diccionario[nuevoElemento] = nuevaDefinicion
    system("cls")
    continuar = (input("¿Desea agregar mas elementos?\nIngrese Si o No\n")).lower()
    system("cls")

print(f"La cantidad de elementos final de la lista es de {len(diccionario)} elementos")
for elemento in diccionario:
    print(f"{elemento}: \n\t {diccionario[elemento]}")