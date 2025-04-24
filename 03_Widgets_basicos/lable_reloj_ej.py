import time
import tkinter as tk

ventana = tk.Tk()
ventana.title("ejemplos de widgets-label")

frame1 = tk.Frame(ventana)
frame1.configure(width=300, height=200, bg="red", bd=5)


etiqueta = tk.Label(frame1, text="Hola, me presento soy label")
etiqueta.pack()

def actualizar_hora():
    etiqueta.config(text=time.strftime("%H:%M:%S"))
    ventana.after(1000, actualizar_hora)

actualizar_hora()

ventana.mainloop()