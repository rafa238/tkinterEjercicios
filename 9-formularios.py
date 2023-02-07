from tkinter import *

ventana = Tk()
ventana.geometry("800x500")

encabezado = Label(ventana, text="Formularios 2")
encabezado.config(
    padx=15,
    pady=15,
    fg="white",
    bg="green",
    font=("Arial", 28)
)

encabezado.grid(row=0, column=0, columnspan=5, sticky=W)

def mostrarProfesion():
    texto=""
    if web.get():
        texto += "Desarrollo web"
    if movil.get():
        texto += "Desarrollo movil"
    mostrarr.config(
        text=texto,
        bg="green",
        fg="white"
    )


web = IntVar()
movil = IntVar()
#boton checkbox
Label(ventana, text="¿A que te dedicas?").grid(row=1, column=0)
Checkbutton(
    ventana,
    text="Desarrollo web",
    variable=web,
    onvalue=1,
    offvalue=0,
    command=mostrarProfesion
).grid(row=2, column=0)
Checkbutton(ventana,
    text="Desarrollo movil",
    variable=movil,
    onvalue=1,
    offvalue=0
).grid(row=3, column=0)

mostrarr = Label(ventana, text="")
mostrarr.grid(row=4, column=0)

def marcar():
    marcado.config(text=opcion.get())

opcion = StringVar()

Label(ventana, text="Selecciona tu genero").grid(row=5, column=0)
opcion.set(None)
Radiobutton(
    ventana,
    text="Masculino",
    value="Masculino",
    variable=opcion,
    command=marcar
).grid(row=6)

Radiobutton(
    ventana,
    text="Femenino",
    value="Femenino",
    variable=opcion,
    command=marcar
).grid(row=7)
marcado = Label(ventana)
marcado.grid(row=7)


#option menu
opcion2 = StringVar()
opcion2.set("opcion1")
def seleccionar():
    seleccionado.config(text=opcion2.get())

Label(ventana, text="Selecciona una opcion").grid(row=5, column=1)
OptionMenu(ventana,
           opcion2,  "opcion1", "opcion2").grid(row=6, column=1)
Button(ventana, text="ver", command=seleccionar).grid(row=7, column=1)
seleccionado = Label(ventana)
seleccionado.grid(row=8, column=1)
ventana.mainloop()