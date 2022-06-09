#ejercicio1

"""
totalCuenta = int(input("Ingresa el total de la cuenta: "))
personas = int(input("Ingresa la cantidad de personas que comieron: "))
propina = int(input("Ingresa la cantidad de propina a dar: "))

pagoxpersona = (totalCuenta+propina)/ personas

print("A cada persona le toca pagar $" + str(pagoxpersona))
"""
#ejercicio2

totalCuenta = int(input("Ingresa el total de la cuenta: "))
personas = int(input("Ingresa la cantidad de personas que comieron: "))
propina = int(input("Ingresa la cantidad de propina a dar: "))
totalConImpuesto = totalCuenta*1.16
pagoxpersona = (totalConImpuesto+propina)/personas

print("A cada persona le toca pagar $" + str(pagoxpersona))

#Convertir codigo a funcion con parametros y sin retorno de datos.