"""for i in range(0,20):
    if i%2 == 0:
        print(i)
    else:
        continue"""


#Definiciion de diccionario
miDiccionario = {
    "Carro":"DefinicionCarro",
    "Perro":"DefinicionPerro",
    "Hombre":"DefinicionHombre",
}

#Impresion de diccionario
print(type(miDiccionario))
print(miDiccionario)

#Recuperar cierto valor por medio de la clave
print(miDiccionario["Carro"])

#Impresion de valores con ciclo for
for valor in miDiccionario.values():
    print(valor)

#Impresion de llaves con ciclo for
for valor in miDiccionario.keys():
    print(valor)

#Impresion de llaves y valores con ciclo for
for llave,valor in miDiccionario.items():
    print(llave + ": " + valor)

#crear diccionario por funcion dict()
dicccionario2 = dict(nombre="Angel",apellido="Morales",edad=25)
print(dicccionario2)
print(type(dicccionario2))

#Crear diccionario a partir de 2 listas (elementos iterables)
listaKeys = ["Mexico","Colombia","EUA","Argentina"]
listaValores = [123,456,789,876]
dicccionario3 = dict(zip(listaKeys,listaValores))
print(dicccionario3)
print(type(dicccionario3))