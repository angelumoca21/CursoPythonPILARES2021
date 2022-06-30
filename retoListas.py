def main():
    alumnos = []
    while True:
        opcion = input("""
        Oprime:
        [1] Para añadir estudiante.
        [2] Para salir.
        """)
        if opcion == "1":
            nombre = input("Ingresa el nombre del estudiante a añadir:")
            alumnos.append(nombre)
        elif opcion == "2":
            break
        else:
            continue
    numEstudiantes = len(alumnos)
    if numEstudiantes == 0:
        print("Tu lista esta vacia.")
    else:
        print("Tu lista quedo asi: ")  
        print(alumnos)


if __name__ == '__main__':
    main()