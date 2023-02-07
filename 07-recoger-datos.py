from tkinter import *

ventana = Tk()
ventana.geometry("700x700")
ventana.config(
    bd=50,
)

dato = StringVar()
resultado = StringVar()


def get_dato():
    resultado.set(dato.get())

    if len(resultado.get()) >= 1:
        texto_recogido.config(
            bg="green",
            fg="white"
        )


Label(ventana, text="Mete un texto: ").pack(anchor=NW)
Entry(ventana, textvariable=dato).pack(anchor=NW)

Label(ventana, text="Dato recogido: ").pack(anchor=NW)
texto_recogido = Label(ventana, textvariable=resultado)

texto_recogido.pack(anchor=NW)

Button(ventana, text="Mostrar Dato", command=get_dato).pack(anchor=NW)

ventana.mainloop()
