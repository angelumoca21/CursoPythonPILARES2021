#Escribir un programa que pregunte una fecha en formato dd/mm/aaaa y muestre por pantalla la misma fecha en formato: dd de <mes> de aaaa donde <mes> es el nombre del mes.
meses = {
    "01":"enero",
    "02":"febrero",
    "03":"marzo",
    "04":"abril",
    "05":"mayo",
    "06":"junio",
    "07":"julio",
    "08":"agosto",
    "09":"septiembre",
    "10":"octubre",
    "11":"noviembre",
    "12":"diciembre",
}


def run():
    fecha = input("Ingresa una fecha en formato dd/mm/aaaa que formatearemos: ")
    #fecha = fecha.replace("/","")
    #print(fecha)
    dia = fecha[:2] 
    mes = fecha[3:5]
    anio = fecha[6:]
    print("La fecha con el nuevo formato es: " + dia + " de " + meses[mes] + " de " + anio + ".")


if __name__ == '__main__':
    run()