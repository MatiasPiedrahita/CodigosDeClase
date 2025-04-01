#coding=utf-8
import random
from os import system
#Programa para comprobar metodos de ordenamiento
system("cls")
listaNumeros = [random.randint(1,100) for i in range(20)]
print("Lista original: ", listaNumeros)

#1.Metodo Burbuja
def burbuja(listaNumeros):
    for i in range(len(listaNumeros)-1):
        for j in range(len(listaNumeros)-1-i):
            if listaNumeros[j] > listaNumeros[j+1]:
                listaNumeros[j], listaNumeros[j+1] = listaNumeros[j+1], listaNumeros[j]
    return listaNumeros

#2.Metodo seleccion
def seleccion(listaNumeros):
    for i in range(len(listaNumeros)-1):
        menor = i
        for j in range(i+1, len(listaNumeros)):
            if listaNumeros[j] < listaNumeros[menor]:
                menor = j
        listaNumeros[i], listaNumeros[menor] = listaNumeros[menor], listaNumeros[i]
    return listaNumeros

#3.Metodo insercion
def insercion(listaNumeros):
    for i in range(1, len(listaNumeros)):
        clave = listaNumeros[i]
        j = i - 1
        while j >= 0 and clave < listaNumeros[j]:
            listaNumeros[j + 1] = listaNumeros[j]
            j -= 1
        listaNumeros[j + 1] = clave
    return listaNumeros

#Ordenando la lista con los metodos de ordenamiento
listaBurbuja = burbuja(listaNumeros.copy())
listaSeleccion = seleccion(listaNumeros .copy())
listaInsercion = insercion(listaNumeros.copy())

#Resultados de las listas ordenadas
print("Lista ordenada por metodo burbuja: ", listaBurbuja)
print("Lista ordenada por metodo seleccion: ", listaSeleccion)
print("Lista ordenada por metodo insercion: ", listaInsercion)