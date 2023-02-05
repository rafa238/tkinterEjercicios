# Tkinter
# modulo para crear interfaces graficas de usuarion
import os
from tkinter import *
import os


class Ventana:

    def __init__(self):
        self.ventana = Tk()
        self.title = "Ventana"
        self.icon = "/imagenes/icono.ico"
        self.size = "770x440"
        self.resizable = False

    def cargar(self):
        # crear la ventana raiz

        # titulo de la ventana
        self.ventana.title(self.title)

        # setear icono
        BASE_DIR = os.path.dirname(os.path.abspath(__file__))
        self.ventana.iconbitmap(BASE_DIR + self.icon)

        # cambiar tamaño de la ventana
        self.ventana.geometry(self.size)

        # Bloquear el tamaño de la ventana
        if self.resizable:
            self.ventana.resizable(1, 1)
        else:
            self.ventana.resizable(0, 0)


    def addTexto(self, text):
        texto = Label(self.ventana, text = text)
        texto.pack()

    def mostrar(self):
        # arrancar y mostrar la ventana hasta que se cierre
        self.ventana.mainloop()

programa = Ventana()
programa.cargar()
programa.addTexto("Buenas noches")
programa.mostrar()