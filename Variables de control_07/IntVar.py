#IntVar = para numeros enteros
import tkinter as tk

ventana = tk.Tk()
ventana.title("ejemplo IntVar")

entero = tk.IntVar(value=42)
print(entero.get())#se aplica lo mismo ya que es una variable de control

#ejemplo de Intvar con radiobuton
opcion1 = tk.Radiobutton(ventana, text="Opcion 1", variable=entero, value=1)
opcion1.pack()

opcion2 = tk.Radiobutton(ventana, text="Opcion 2", variable=entero, value=2)
opcion2.pack()

def actualizar(*args):
    print(entero.get())

entero.trace("w", actualizar)
#aca lo que hacemos en este es a la hora de seleccionar la opcion de radiobuton reasignamos el valor de entero osea seleccionamos opcion 1 pasa de 42 a valor 1

#otro ejemplo con checkbutton
casilla = tk.Checkbutton(ventana, text="Aceptar", variable=entero, onvalue=1, offvalue=0)

ventana.mainloop()