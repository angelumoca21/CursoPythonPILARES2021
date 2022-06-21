#Detector de palindromos

def run():
    fraseUser = input("Bienvenido al detector de palindromos, ingresa tu frase: ")
    fraseUser = fraseUser.lower()
    #print(fraseUser)
    fraseUser = fraseUser.replace(" ","")
    print("fraseUser sin espacios y solo minusculas: " + fraseUser)
    fraseContraria = fraseUser
    #print(fraseContraria)
    fraseContraria = fraseContraria[::-1]
    print("fraseUser sin espacios, solo minusculas y con sentido reversa: " + fraseContraria)
    if fraseUser == fraseContraria:
        print("Tu frase es palindromo")
    else:
        print("Tu frase no es palindromo")

if __name__ == '__main__':
    run()