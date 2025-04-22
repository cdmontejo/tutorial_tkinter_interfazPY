import tkinter as tk

ventana = tk.Tk()
#vamos a definir una funcion onclick
def on_click(event):
    #aca no vamos a entregar un evento aislado sino que nos sirve para traer el texto que esta asociado a cada widget
    #por ejemplo hacemos un boton 1 entonces este mada a llamar el texto de ese boton
    print(f" {event.widget['text']} presionado")

#bueno aca utilizamos un for para generar 3 botones en ventana donde cada uno tendra text=boton y 'i' nos sirve para el indice
botones = [tk.Button(ventana, text=f"Boton {i}") for i in range(3)]

#aca recorremos los botones y los empaquetamos(pack), dentro de la ventana
for button in botones:
    button.pack()
    #aca nuestro evento del click izquierdo
    button.bind("<Button-1>", on_click)

ventana.mainloop()