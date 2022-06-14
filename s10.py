def run():
    precioDolar = 20.61 #1dolar = 20.61 pesosMX
    precioCol = 191.96 
    opcion = input("""
    Hola, bienenido al conversor de unidades:
    1. Pesos mexicanos a dolares
    2. Pesos mexicanos a pesos colombianos
    Que conversion quieres realizar
    """)
    pesos = float(input("Cuantos pesos MX quieres convertir: "))
    if opcion == "1":
        mxToUsd(pesos,precioDolar)
    else:
        mxToCol(pesos,precioCol)


def mxToUsd(pesos,precioDolar):
    conversion = pesos / precioDolar
    print("Tus $" + str(pesos) + " equivalen a " + str(conversion) + " USD.")


def mxToCol(pesosMx,col):
    conversion = pesosMx * col
    print("Tus $" + str(pesosMx) + " equivalen a " + str(conversion) + " pesos colombianos.")

#Entry point
if __name__ == '__main__':
    run()


# def mxToUsd(pesosMx):
#     conversion = pesosMx / precioDolar
#     print("Tus $" + str(pesosMx) + " equivalen a " + str(conversion) + " USD.")


# def mxToCol(pesosMx):
#     conversion = pesosMx * precioCol
#     print("Tus $" + str(pesosMx) + " equivalen a " + str(conversion) + " pesos colombianos.")

# precioDolar = 20.61 #1dolar = 20.61 pesosMX
# precioCol = 191.96 #1pcol = 0.0052 pesosMX  
# opcion = input("""
# Hola, bienenido al conversor de unidades:
# 1. Pesos mexicanos a dolares
# 2. Pesos mexicanos a pesos colombianos
# Que conversion quieres realizar
# """)
# pesos = float(input("Cuantos pesos MX quieres convertir: "))
# if opcion == "1":
#     mxToUsd(pesos)
# else:
#     mxToCol(pesos)