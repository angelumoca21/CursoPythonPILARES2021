#Nueva forma de crear diccionariocon ayuda de un ciclo
"""
dic = {
    "llave1": "valor1",
    "llave2": "valor2",
    "llave3": "valor3",
    "llave4": "valor4",
}
"""
persona = {}
continuar = True
while continuar:
    llave = input("Que llave quieres introducir al diccionario?: ")
    valor = input(llave + ": ")
    persona[llave] = valor
    print(persona)
    continuar = input("Quieres añadir mas relaciones llave-valor al diccionario? (si/no) ") == "si"

