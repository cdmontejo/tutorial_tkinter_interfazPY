#los admionistradoes de geometria son herramientas que nos permiten organizar y posicionar los widgets en nustras interfaces
#tkinter ofrese los tres que veremos en la carpeta, aparte de los que ya estan por defalut que vimos muy minimo con anterioridad
#como el margin padding y border
#Grid es ideal para organizar widgets en una estructura de filas y columnas, similar a una tabla asi ofreciendo un control preciso de posicion y tamanio de los widgets
import tkinter as tk

ventana = tk.Tk()
ventana.title("Ejemplo de grid")

#creamos 2 labels y los posicionamos con grid
label = tk.Label(ventana, text='celda A1')
#row es nuestra fila y column es nuestra columna
#luego esta el pad que es padding que seria un relleno interno que se le pone al objeto, en otras palabras se expanden en este caso se expande 10 pixeles
#en cambio un margin que es un margen es un espacio que es externo al objeto para alejar uno al otro
label.grid(row=0, column=0, padx=10, pady=10)

label2 = tk.Label(ventana, text='celda A2')
label2.grid(row=1, column=0, padx=5, pady=5)

label3 = tk.Label(ventana, text='celda B1')
label3.grid(row=0, column=1, padx=5, pady=5)

label4 = tk.Label(ventana, text='celda B2')
label4.grid(row=1, column=1, padx=5, pady=5)