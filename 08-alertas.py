from tkinter import *
from tkinter import messagebox as MessageBox
ventana = Tk()
ventana.config(bd=70)
def sacarAlerta():
    MessageBox.showinfo("A", "Hola buenas tardes")

def salir():
    resultado = MessageBox.askquestion("salir", "Quieres continuar ejecutando la aplicacion?")
    if resultado == "yes":
        ventana.destroy()

Button(ventana, text="Mostrar alerta!!", command=salir).pack()

ventana.mainloop()