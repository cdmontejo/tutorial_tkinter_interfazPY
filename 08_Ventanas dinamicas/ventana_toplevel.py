#una ventana toplevel es una ventana independiente, extra o nueva en el programa
import tkinter as tk


ventena_tlej = tk.Tk()
ventena_tlej.title("Ventana Principal - ejemplo")
ventena_tlej.geometry("600x600")

#las ventanas toplevel se crean de esta manera, donde se guarda en una variable y se manda a llamar toplevel de tkinter
#esta se asocia a la principal y tiene las mismas opciones que la principal
ventana_toplevel1 = tk.Toplevel(ventena_tlej)
ventana_toplevel1.title("Ventana nueva Toplavel")
ventana_toplevel1.geometry("300x200+100+200")


#esta es otra ventana que esta en el otro archivo otra_asociada_principal.py

def ejecutar_otro_modulo():
    from otra_asociada_principal import abrir_ventana_toplevel
    abrir_ventana_toplevel()

boton1 =tk.Button(ventena_tlej, text="abrir otra ventana toplavel", command=ejecutar_otro_modulo)
boton1.pack()


ventena_tlej.mainloop()