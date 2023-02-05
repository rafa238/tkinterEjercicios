from tkinter import *
from PIL import Image, ImageTk

ventana = Tk()
ventana.geometry("700x500")
Label(ventana, text="Hola soy rafa").pack(anchor=W)

imagen = Image.open("./imagenes/rafachu2.jpg")
render = ImageTk.PhotoImage(imagen)
Label(ventana, image=render).pack(anchor=E)
ventana.mainloop()