#booleanVar = para valores booleanos(v/f)
import tkinter as tk


ventana = tk.Tk()


booleano = tk.BooleanVar(value=True)

#aca estamos haciendo un ejemplo con el check button en este caso la booleana sera verdadera y aparecera marcada con check
casilla = tk.Checkbutton(ventana, text="Aceptar", variable=booleano)
casilla.pack()

def actualizar(*args):
    print(booleano.get())

#usamos el trace para detectar cambios si se acepta o no y actualizar
booleano.trace("w", actualizar)