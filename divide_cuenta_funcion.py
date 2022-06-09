#Convertir codigo a funcion con parametros y sin retorno de datos.

def divideCuenta(TOTALCUENTA,PERSONAS,PROPINA):
    totalConImpuesto = TOTALCUENTA*1.16
    pagoxpersona = (totalConImpuesto+PROPINA)/PERSONAS
    print("A cada persona le toca pagar $" + str(pagoxpersona))

# totalCuenta = int(input("Ingresa el total de la cuenta: "))
# personas = int(input("Ingresa la cantidad de personas que comieron: "))
# propina = int(input("Ingresa la cantidad de propina a dar: "))
#divideCuenta(totalCuenta,personas,propina)
divideCuenta(5000,15,1000)
divideCuenta(365,2,25)
divideCuenta(896,4,150)