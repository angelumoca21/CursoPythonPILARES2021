num = int(input("Hola, bienvenido al detector de numeros primos: "))
acumulado = 0 #Variable que almacena la cantidad de divisores que 
#arrojan residuo 0. 
for divisor in range(1,num+1):
    resultado = num % divisor
    if resultado == 0:
        acumulado = acumulado + 1
    if acumulado > 2:
        print("Tu numero es no primo.")
        break
if acumulado == 2:
    print("Tu numero es primo.")
