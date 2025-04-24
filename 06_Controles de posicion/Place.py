#Place ofrece mayor control sobre la posicion de los widgets al permitirnos ubicarlos en coordenadas especificas
import tkinter as tk

ventana = tk.Tk()
ventana.title("ejemplo de place")

ventana.geometry("600x600")

#Creamos labels y posicionamos con place
#adentro de placehay dos formas de hacerlo con coordenadas que seria con x y y
label3 = tk.Label(ventana, text="Label 3")
label3.place(x=20, y=50)

label4 = tk.Label(ventana, text="Label 4")
label4.place(x=100, y=100)

#y con coordenadas relativas que serian rel, una cordenada relativa refiere a un porcentaje del contenedor
label1 = tk.Label(ventana, text="Label 1")
label1.place(relx=0.25, rely=0.25)

label2 = tk.Label(ventana, text="Label 2")
label2.place(relx=0.5, rely=0.5)