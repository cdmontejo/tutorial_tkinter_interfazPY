#en el checkbuton podemos optar por varias opciones y no solo una

import tkinter as tk

from Widgets_basicos_03.boton import boton

ventana = tk.Tk()
ventana.title("Ejemplo Checkbutton")

check1 = tk.Checkbutton(ventana, text="Opcion 1")

check1.pack()

#ahora vamos a hace uno de opcion multiple
#como son mas variable snecesitamos ahora variables de control
variable_check1 = tk.BooleanVar
variable_check2 = tk.BooleanVar

check_1 = tk.Checkbutton(ventana, text="Opcion 1",  variable= variable_check1)
check_2 = tk.Checkbutton(ventana, text="Opcion 2", variable= variable_check2)

check_1.pack()
check_2.pack()

#ahora haremos un ejemplo donde a traves
def habilitar():
    if variable_check_1.get():
        boton1.config(state="normal")
    else:
        boton1.config(state="disabled")

variable_check_1 = tk.BooleanVar()#del checkbuton habilitamos la accion
check__1 = tk.Checkbutton(ventana, text="Habilitar boton", variable=variable_check_1, command=habilitar)
boton1=tk.Button(ventana, text="Boton", state="disabled")#de este boton

ventana.mainloop()