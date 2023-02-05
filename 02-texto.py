from tkinter import *

ventana = Tk()
ventana.geometry("500x500")


texto = Label(ventana, text="Bienvenido a mi programa")
texto.config(
    fg="white",
    bg="black",
    padx=500,
    pady=20,
    font=("Arial", 16)
)
texto.pack()

texto2 = Label(ventana, text="Buenas noches")
texto2.config(
    height = 3,
    bg="orange",
    font=("Arial", 10),
    padx = 10,
    pady = 20,
    cursor= "spider"
)
texto2.pack(anchor=E)
ventana.mainloop()