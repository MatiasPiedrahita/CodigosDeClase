#coding=utf-8
#Programa para cacular IMC, con el objetivo de realizar el control de excepciones
from os import system
errorDatos = ""
ocurrioError = True
while ocurrioError is not False:
    try:
        peso = float(input("Ingrese su peso en KG: \n"))
        altura = float(input("Ingrese su altura en M: \n"))
        system("cls")
        IMC = peso / (altura ** 2)
        print(f"Su IMC es de: {IMC:.2f}")
        if IMC < 18.5:
            print("Usted tiene bajo peso")
        elif IMC >= 18.5 and IMC < 25:
            print("Usted tiene peso normal")
        elif IMC >= 25 and IMC < 30:
            print("Usted tiene sobrepeso")
        elif IMC > 30:
            print("Usted tiene obesidad")
        ocurrioError = False
    except ValueError as errorDatos:
        system("cls")
        print(errorDatos)
        print("Ha ocurrido un error, vuelve a ingresar los datos de manera correcta")
    except ZeroDivisionError as errorDatos:
        system("cls")
        print(errorDatos)
        print("Ha ocurrido un error, vuelve a ingresar los datos de manera correcta")
