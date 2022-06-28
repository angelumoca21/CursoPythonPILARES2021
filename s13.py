#Creacion de lista
nombresTallerPython = ["Jose Manuel","Eduardo","Richard"]
print(nombresTallerPython)
print(type(nombresTallerPython))

#Creacion de tupla
edades = (10,20,30)
print(edades)
print(type(edades))

#Agragando a Gerson y a Sefora a la lista
nombresTallerPython.append("Sefora")
nombresTallerPython.append("Gerson")
nombresTallerPython.append("Uriel")
print(nombresTallerPython)

#Eliminando a Uriel
nombresTallerPython.pop(5)
print(nombresTallerPython)

numEstudiantes = len(nombresTallerPython)
print("El numero de estudianres es de " + str(numEstudiantes))

#Intento de agregar elemento a la tupla
#edades.append(25)

#Recorrer lista y tupla con ciclo For
for elemento in nombresTallerPython:
    print(elemento)

for item in edades:
    print(item)

#Llenar lista con ciclo For
alumnos = int(input("Hola ingresa la cantidad de estudiantes a agregar a la lista: "))
nombresTallerPython2=[]
for i in range(0,alumnos):
    nombre = input("Ingresa el nombre del primer alumno: ")
    nombresTallerPython2.append(nombre)
print(nombresTallerPython2)

#Listas y tuplas pueden combinar tipos de datos
listaMixta = ["Jose",25,True,3.6521,'t',False,[1,2,3],(4,5,6)]
print(listaMixta)
print(type(listaMixta))

#suma de listas
lista1 = ['A','N','G']
lista2 = ['e','l']
lista3 = lista1 + lista2
print(lista3)

lista4 = [1,2,5,6]
lista5 = [8,7,1,2]
lista6 = lista4 + lista5
print(lista6)

#sumar 2 listas (numericamente)
numeroElementos = len(lista4)
lista7=[]
for j in range(0,numeroElementos):
    lista7.append(lista4[j]+lista5[j])
print(lista7)

lista8=[0,1,2,3,4,5]
print(lista8)
lista8.insert(1,5000000)
print(lista8)