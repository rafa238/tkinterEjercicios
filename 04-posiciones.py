from tkinter import *

ventana = Tk()
#ventana.geometry("500x500")


texto = Label(ventana, text="Bienvenido a mi programa")
texto.config(
    fg="white",
    bg="black",
    padx=50,
    pady=20,
    font=("Arial", 16)
)
texto.pack(side=TOP)

texto2 = Label(ventana, text="Soy Rafael")
texto2.config(
    height = 3,
    bg="green",
    font=("Arial", 10),
    padx = 10,
    pady = 20,
    cursor= "spider"
)
texto2.pack(anchor=E,  fill=X, expand=YES)

texto2 = Label(ventana, text="Buenas tardes")
texto2.config(
    height = 3,
    bg="orange",
    font=("Arial", 10),
    padx = 10,
    pady = 20,
    cursor= "spider"
)
texto2.pack(side=LEFT, fill=X, expand = YES)

texto2 = Label(ventana, text="Buenos dias")
texto2.config(
    height = 3,
    bg="Yellow",
    font=("Arial", 10),
    padx = 10,
    pady = 20,
    cursor= "spider"
)
texto2.pack(side=LEFT, fill=X, expand = YES)
ventana.mainloop()