i = 1
numElefantes = int(input("Ingresa un de numero de elefantes: "))
if numElefantes < 0:
    print("El numero que ingresate es invalido.")
elif numElefantes == 0:
    print("Bye, aguafiestas.")
elif numElefantes > 10:
    print("La telaraña no aguanta tantos elefantes.")
elif numElefantes == 1:
    print(str(i) + " elefante se balanceada sobre la tela de una araña...")
else:
    while i <= numElefantes:
        if i == 1:
            print(str(i) + " elefante se balanceada sobre la tela de una araña")
            print("como veia que resistia fue a llamar a otro elefante")
        elif i>1 and i<=numElefantes-1:
            print(str(i) + " elefantes se balanceadan sobre la tela de una araña")
            print("como veian que resistia fueron a llamar a otro elefante")
        else:
            print(str(i) + " elefantes se balanceadan sobre la tela de una araña...")
        i = i + 1