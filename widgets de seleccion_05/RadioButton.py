#los widgets de seleccion son para seleccionar opciones a traves de una lista de elementos
#en este caso radiobuton son para poder seleccionar una sola opcion que se presente
import tkinter as tk
from statistics import variance


ventana = tk.Tk()
ventana.title

opcion1 = tk.Radiobutton(ventana, text="Opcion 1")
opcion1.pack()


def mostrara_seleccion():
    color_seleccionado = variable_control.get()
    if color_seleccionado == 1:
        ventana.config(bg="red")
    elif color_seleccionado==2:
        ventana.config(bg="blue")

#para crear un radio button con varias opciones se necesita una variable IntVar que es una variable de control que basicamente va guardadno la opcion del usuario
variable_control = tk.IntVar()

opcion_1 = tk.Radiobutton(ventana, text="rojo", variable=variable_control, value=1, command=variable_control)
opcion_2 = tk.Radiobutton(ventana, text="azul ", variable=variable_control, value=2, command=variable_control)

opcion_1.pack()
opcion_2.pack()



#recuerden command nos sirven para llamar la funcion
boton = tk.Button(ventana, text="Mostrar seleccion", command=mostrara_seleccion)
boton.pack()

ventana.mainloop()