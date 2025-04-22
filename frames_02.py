#que es un frame, son cuadros o contenedores donde pueden ir poniendo cosas
import tkinter as tk

ventana = tk.Tk()

#en este caso creamos otra ventana para el ejemplo
ventana.title("Ventana Frame ejemplo")
ventana.geometry("600x400")
ventana.configure(bg='skyblue')

#creamos el objeto frame de la clase Frame y pnempos el atributo que deseamos en este caso ventana
frame1 = tk.Frame(ventana)
#estas serian las caracteristicas del frame (bd es el borde)
frame1.configure(width=300, height=200, bg="red", bd=5)

frame2 = tk.Frame(frame1)
frame2.configure(width=100, height=100, bg="blue", bd=5)

#igual se pone el atributo donde ira y el text nos sirve para poner el texto adentro
boton = tk.Button(frame2, text="Hola")

boton.pack()
frame1.pack()
frame2.pack()

#en general son contenedores que nos serviran para organizar

#luego estan los label frame que son similares a los datagirdview(creo que eran esos en C#)
labelframe = tk.LabelFrame(ventana, text="Grupo de widgets", bg='yellow', padx=10, pady=10)
#el pad hace referencia al pading que son los espacios que se dejan entre los contenedores, hay una imagen ejemplificando
labelframe.configure(width=300, height=200)
labelframe.pack()

ventana.mainloop()