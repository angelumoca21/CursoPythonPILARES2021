#Funcion sin parametro y sin retono de datos 
def saludar():
    print("Hola!")
    print("Bienvenidos")
    print("Saludos")
#Funcion con parametros y sin retono de datos 
def saludar2(nombre):
    print("Hola " + nombre)
#Funcion sin parametros y con retono de datos 
def suma():
    num1 = 1.25
    num2 = 789
    resultado = num1 + num2
    return resultado
#Funcion con parametros y con retono de datos 
def areaTriangulo(base,altura):
    area = base*altura / 2
    return area
#saludar()
# nombre = input("Ingresa tu nombre: ")
# saludar2(nombre)
# saludar2("Gerson")
# saludar2("Sefora")
# saludar2("Richard")
# RESULTADO = suma()
# print(RESULTADO)
AREA = areaTriangulo(5,3)
print("El area del tringulo es " + str(AREA) + " cm2.")
AREA = areaTriangulo(13,4)
print("El area del tringulo es " + str(AREA) + " cm2.")
AREA = areaTriangulo(7,6.4)
print("El area del tringulo es " + str(AREA) + " cm2.")