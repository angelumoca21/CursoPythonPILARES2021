"""i = 1
while i < 201:
    print("Hola")
    i = i+1"""

#Pedir por teclado un numero y mostrar en pantalla las tablas de multiplicar
#(1-10)
#5, 5x1=1,5x2=10,...,5x10=50
i = 1
num = int(input("Ingresa el numero que quieres realizar su tabla: "))
while i < 11:
    resultado = i * num
    print(str(num)+"x"+str(i)+"="+str(resultado))
    i=i+1