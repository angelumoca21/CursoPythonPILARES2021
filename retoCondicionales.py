print(
    """
    Bienvenido a la pizeria BELLA NAPOLI
    Tenemos 2 tipos de pizza:
        1. Vegetariana
        2. No vegetariana
    """
)
tipo = int(input("¿Que tipo de pizza te gustaria? [1 o 2]"))
if tipo == 1:
    ingrediente = input("""
    Los ingredientes disponibles son:
        a)Pimiento
        b)Tofu
    ¿Que ingrediente se te antoja?
    """)
    if ingrediente == "a":
        print("Tu pizza es vegetariana con pimiento, queso y salsa de tomate")
    elif ingrediente == "b":
        print("Tu pizza es vegetariana con tofu, queso y salsa de tomate")
    else:
        print("La opcion que escogiste no es valida. Bye.")
elif tipo == 2:
    ingrediente = input("""
    Los ingredientes disponibles son:
        a)Peperoni
        b)Jamon
        c)Salmon
    ¿Que ingrediente se te antoja?
    """)
    if ingrediente == "a":
        print("Tu pizza es no vegetariana con peperoni, queso y salsa de tomate")
    elif ingrediente == "b":
        print("Tu pizza es no vegetariana con jamon, queso y salsa de tomate")
    elif ingrediente == "c":
        print("Tu pizza es no vegetariana con salmon, queso y salsa de tomate")
    else:
        print("La opcion que escogiste no es valida. Bye.")
else:
    print("La opcion que escogiste no es valida. Bye.")
