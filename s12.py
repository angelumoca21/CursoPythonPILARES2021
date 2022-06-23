palabraUser = input("Bienvienido al codificador de palabras, ingresa tu palabra a codificar: ")
primeraLetra = palabraUser[0]
primeraLetra = primeraLetra.lower()
if primeraLetra == "a" or primeraLetra == "e" or primeraLetra == "i" or primeraLetra == "o" or primeraLetra == "u":
    #letra es vocal
    palabraUserCod = palabraUser + "way"
else:
    #letra no es vocal
    palabraUserSPriLetra = palabraUser[1:]
    palabraUserCod = palabraUserSPriLetra + primeraLetra + "ay"
print(f"""
Codificacion:
{palabraUser}    {palabraUserCod}
""")
print("Codificacion" + "\n" + palabraUser + "\t" + palabraUserCod)