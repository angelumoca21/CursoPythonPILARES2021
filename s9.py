#Escribir una función que reciba un número entero positivo y devuelva su factorial.
#parametros y con rectorno de datos

def factorial(numero):
    resultado = 1
    for i in range(numero,0,-1):
        resultado *= i
        #resultado = resultado * i
    return resultado


num = int(input("Ingresa el numero del cual quieres calcular el factorial: "))
resultadoFactorial = factorial(num)
print(str(num) + "!=" + str(resultadoFactorial))