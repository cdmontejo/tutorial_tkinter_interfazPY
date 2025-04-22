#veremos los basicos que son label, buton y entry
#los widgets son elementos graficos que nos sirven para poder diseñar la interfaz de usuario

import tkinter as tk

ventana = tk.Tk()
ventana.title("ejemplos de widgets-label")
ventana.geometry("1000x800+0+0")


frame1 = tk.Frame(ventana)
frame1.configure(width=300, height=200, bg="red", bd=5)


etiqueta = tk.Label(frame1, text="Hola, me presento soy label")
#para poder cambiar un texto en este caso del label seria asi en teoria de primero se escribe el de arriba luego el que hacemos abajo pero por el timepo de ejecucion lo hace demasiado rapido
#adentro del config tambien podemos ir dandole estilo a nuestro label aparte de suplantar el texto
etiqueta.config(
    fg='blue', #fuente azul
                bg='yellow',#fondo del label amarillo
                font=('Arial', 12, 'bold'),#arial, tamaño 12, negrita(bold)
                text='En que te ayudo?'#nuevo texto
    )


frame1.pack()
etiqueta.pack()


ventana.mainloop()