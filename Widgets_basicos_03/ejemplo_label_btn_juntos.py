import tkinter as tk

ventana = tk.Tk()
ventana.title("ejemplos de widgets-boton")

boton = tk.Button(ventana, text="Presiona aqui")
import tkinter as tk

ventana = tk.Tk()
ventana.title("ejemplos de widgets-boton")

boton = tk.Button(ventana, text="Presiona aqui")
#estilo del boton
boton.config(fg='white', bg='green', font=('Arial', 12))
boton.pack()

etiqueta = tk.Label(frame1, text="Hola, me presento soy label")
etiqueta.pack()

def cambiar_texto():
    etiqueta.config(text='Presiono el boton')

boton.config(command=cambiar_texto)
ventana.mainloop()