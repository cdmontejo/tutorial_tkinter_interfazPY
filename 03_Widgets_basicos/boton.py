import tkinter as tk

ventana = tk.Tk()
ventana.title("ejemplos de widgets-boton")

boton = tk.Button(ventana, text="Presiona aqui")
#estilo del boton
boton.config(fg='white', bg='green', font=('Arial', 12))

boton.pack()

#funcion del botnmo
#esta funcion lo que hace es que va a imprimir el print en consola cuando se presione el boton
def boton_presionado():
    print("Presion en el boton")

#mandamos a llamar nuestra funcion dentro del boton para drle accion
boton.config(command=boton_presionado)

ventana.mainloop()