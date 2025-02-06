#coding=utf-8
print("Programa para convertir de horas a minutos")
hora_ingresada = input("Ingresa un valor para la hora")
print(f"La hora ingresada es {hora_ingresada} y el tipo es {type(hora_ingresada)}")

if "." in hora_ingresada:
    hora = float(hora_ingresada)

else:
    hora = int(hora_ingresada)

print(f"La hora es {hora} y la hora ingresada es de tipo {type(hora)}")
