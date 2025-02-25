#coding=utf-8
#Programa para entender el ciclo for
print("Programa para generar las tablas de multiplicar")
for i in range (1,11):
    print(f"Tabla del numero {i}")
    for j in range(1,11):
        print(f"{i} X {j} = {i*j}")