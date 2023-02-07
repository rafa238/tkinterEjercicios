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
encabezado.grid(row=0, column=0, columnspan=12, sticky=W)

label = Label(ventana, text="Nombre")
label.grid(row=1, column=0, padx=5, pady=5, sticky=W)

campo_texto = Entry(ventana)
campo_texto.grid(row=1, column=1, padx=5, pady=5, sticky=W)
campo_texto.config(justify="left", state="normal")

#campo para apellidos
label = Label(ventana, text="Apellidos")
label.grid(row=2, column=0, padx=5, pady=5, sticky=W)


campo_texto = Entry(ventana)
campo_texto.grid(row=2, column=1, padx=5, pady=5, sticky=W)
campo_texto.config(justify="left", state="normal")


#campo para descripcion
label = Label(ventana, text="Descripcion")
label.grid(row=3, column=0, padx=5, pady=5, sticky=N)

#campo de textArea
campo_grande = Text(ventana)
campo_grande.grid(row=3, column=1)
campo_grande.config(
    width=30,
    height = 5,
    font=("Arial", 10),
    padx=15,
    pady=15,
)

Label(ventana, text=" ").grid(row=4, column=1)

boton = Button(ventana, text="Enviar")
boton.grid(row=5, column=1, sticky=W)
boton.config(pady=10, padx=10, bg="green", fg="white")

ventana.mainloop()