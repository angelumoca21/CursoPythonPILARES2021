#Opcion2
"""from random import randint
numeroAleatorio = randint(0,100)
print(numeroAleatorio)"""
#Opcion3
"""from random import *
numeroAleatorio = randint(0,100)
print(numeroAleatorio)"""
#Opcion1
import random
numeroAleatorio = random.randint(0,100)
print(numeroAleatorio)
numeroUsuario = int(input("Hola, que numero crees que estoy pensando? (0-100): "))
while numeroAleatorio != numeroUsuario:
    if numeroAleatorio > numeroUsuario:
        print("El numero que pensaste no es correcto, prueba uno mas grande.")
    elif numeroAleatorio < numeroUsuario:
        print("El numero que pensaste no es correcto, prueba uno mas chico.")
    numeroUsuario = int(input("Ingresa otro numero: "))
print("Corrrecto! Ganaste.")