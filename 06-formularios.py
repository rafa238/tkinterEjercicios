from tkinter import *

ventana = Tk()
ventana.geometry("700x400")
ventana.title("Formularios")
#Texto encabezado
encabezado = Label(ventana, text="Formularios con tkinter")
encabezado.config(
    fg="white",
    bg="darkgrey",
    font=("Open Sans", 18),
    padx= 10,
    pady= 10
)
encabezado.grid(row=0, column=0, columnspan=2, sticky=W)

label = Label(ventana, text="Nombre")
label.grid(row=1, column=0, padx=5)
campo_texto = Entry(ventana)
campo_texto.grid(row=1, column=1, padx=5, pady=5, sticky=W)

ventana.mainloop()