import tkinter as tk

from Widgets_basicos_03.ejemplo_label_btn_juntos import boton

ventana = tk.Tk()
ventana.title("ejemplos de widgets-entry")

etiqueta = tk.Label(ventana, text="Lo de abajo es un entry")
etiqueta.pack()

entrada = tk.Entry(ventana)
entrada.config(fg='white', bg='green', font=('Arial', 12))

entrada.insert(0, 'text por defecto')
entrada.pack()


#obtenemos lo que ingrese el usuario en el entry y con el boton actualizamos
def aplicar_texto():
    texto = entrada.get()
    etiqueta.config(text=texto)

boton_aplicar = tk.Button(ventana, text="Aplicar Texto", command=aplicar_texto)
boton_aplicar.pack()


ventana.mainloop()