#un entry es un espacio para que el usuario pueda escribir algo en pantalla
import tkinter as tk

ventana = tk.Tk()
ventana.title("ejemplos de widgets-entry")

etiqueta = tk.Label(ventana, text="Lo de abajo es un entry")
etiqueta.pack()

entrada = tk.Entry(ventana)
entrada.config(fg='white', bg='green', font=('Arial', 12))

#metodo para que el entry tenga un texto por defecto
entrada.insert(0, 'text por defecto')

#para poder obtener el dato del insert
texto = entrada.get()
print(texto)

entrada.pack()

ventana.mainloop()
