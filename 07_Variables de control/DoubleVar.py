#doublevar = para numeros de punto flontante, quiere decir decimales

import tkinter as tk

from Widgets_basicos_03.label import ventana

ventana = tk.Tk()
ventana.title("ejemplo doublevar")

decimal = tk.DoubleVar(value=3.14)

#voy explicando esto que no lo habia echo es un control deslizante a eso refiere Scale, donde tenemos que poner el tipo de variable, en este caso la que creamos que es decimal
#el maximo y minimo valor y en que sentido va a estar este control deslizante en este caso horizontal y resolution que es la velocidad a la que se mueve el controlador
control_deslizaante = tk.Scale(ventana, variable=decimal, from_=0, to=10, resolution=0.01, orient=tk.HORIZONTAL)
control_deslizaante.pack()

ventana.mainloop()