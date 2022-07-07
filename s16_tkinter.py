import tkinter
def saludo():
    textoCaja = cajaTexto.get()
    print(textoCaja)
    etiqueta2["text"]=textoCaja

ventana = tkinter.Tk()
ventana.geometry("600x600")
etiqueta = tkinter.Label(ventana,text="Taller de Python.",font="Ubuntu 30")
etiqueta.pack()
boton1 = tkinter.Button(ventana,text="Oprimeme",padx=100,pady=100,font="Helvetica 20",command=saludo)
boton1.pack()
cajaTexto = tkinter.Entry(ventana,font="Ubuntu 25")
cajaTexto.pack()
etiqueta2 = tkinter.Label(ventana,font="Ubuntu 40")
etiqueta2.pack()

ventana.mainloop()