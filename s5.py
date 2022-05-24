"""
if 1==0:
    print("Son iguales")#Bloque que se ejecuta si la condicion es True
else:
    print("Son diferentes")#Bloque que se ejecuta si la condicion es False
"""

#Programa que determina si el numero ingresado por teclado es par o impar.

"""
num = int(input("Hola, ingresa un número: "))
if num%2==0:
    print("Tu numero es par.")
else:
    print("Tu numero es impar.")
"""    
#Introduccion a IF-ELIF-ELSE
#El usurio introducirá su promedio final y el programa determinará si esta aprobado, reprobado o es alumno de excelencia
calificacion = float(input("Hola, ingresa tu califacion final de Mate: "))
if calificacion==10:
    print("Eres un alumno de regular.")
elif calificacion<10 and calificacion>=6:
    print("Eres un alumno de excelencia.")
else:
    print("Eres un alumno reprobado.")