from ventana_toplevel import ventena_tlej
import tkinter as tk

#en esta funcion solo les estoy demostrando que podemos abrir otra ventana a traves del boton
def abrir_ventana_toplevel():
    ventanatoplevel = tk.Toplevel(ventena_tlej)
    ventanatoplevel.title("la otra")
    ventanatoplevel.geometry("300x200+50+50")
    label1 = tk.Label(text="esta ventan fue abierta a traves del boton de la principal")
    label1.pack()