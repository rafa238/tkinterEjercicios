from tkinter import *

ventana = Tk()
ventana.title("Marcos")
ventana.geometry("700x400")

marco = Frame(ventana, width = 250, height = 250)
marco.config(
    bg="red",
    bd=5,
    relief = "solid"
)
marco.pack(side=RIGHT, anchor=SE)
ventana.mainloop()