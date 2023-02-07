"""
Calculadora:
- Dos campos de texto
- 4 botones para las operaciones
- mostrar el resultado en una alerta
"""

from tkinter import *
from tkinter import messagebox

ventana = Tk()
ventana.title("Ejercicio completo con tkinter")
ventana.config(bd=25)

numero1 = IntVar()
numero2 = IntVar()
resultado = StringVar()


def operacion(tipo):
    try:
        int(numero1.get())
        int(numero2.get())
    except:
        messagebox.showwarning("Error con los numeros", "Los datos ingresados no son numeros :(")
        return

    if tipo == "sumar":
        print(numero1.get() + numero2.get())
        resultado.set(numero1.get() + numero2.get())
    elif tipo == "restar":
        print(numero1.get() - numero2.get())
        resultado.set(numero1.get() - numero2.get())
    elif tipo == "multiplicar":
        print(numero1.get() * numero2.get())
        resultado.set(numero1.get() * numero2.get())
    elif tipo == "dividir":
        try:
            print(numero1.get() / numero2.get())
            resultado.set(numero1.get() / numero2.get())
        except ZeroDivisionError:
            messagebox.showwarning("Error matematico, Division por cero no valida", "No se puede realizar la division entre cero")
            return
    numero1.set(0)
    numero2.set(0)
    mostrarResultado()


def mostrarResultado():
    messagebox.showinfo("Resultado", f"El resultado de la operacion es {resultado.get()}")


marco = Frame(ventana, width=250, height=250)
marco.config(
    bd=5,
    relief=SOLID,
    padx=15,
    pady=15
)
marco.pack(side=TOP, anchor=CENTER)

Label(marco, text="Primer numero").pack()
Entry(marco, textvariable=numero1, justify="center").pack()

Label(marco, text="Segundo numero").pack()
Entry(marco, textvariable=numero2, justify="center").pack()

Label(marco, text="").pack()
Button(marco, text="Sumar", command=lambda: operacion("sumar")).pack(side=LEFT, fill=X, expand=YES)
Button(marco, text="Restar", command=lambda: operacion("restar")).pack(side=LEFT, fill=X, expand=YES)
Button(marco, text="Multiplicar", command=lambda: operacion("multiplicar")).pack(side=LEFT, fill=X, expand=YES)
Button(marco, text="Dividir", command=lambda: operacion("dividir")).pack(side=LEFT, fill=X, expand=YES)
ventana.mainloop()
