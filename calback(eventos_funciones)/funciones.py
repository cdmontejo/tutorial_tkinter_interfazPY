#un evento es una accion o suceso que ocurre cunado el usuario interactua con la aplicacion
#una funcion callback es una funcion que se ejecuta cuando se realiza el evento
import tkinter as tk

ventana = tk.Tk()

#por ejemplo uno de los eventos puede ser el dar click izquierdo

#en este caso sera nuestro evento
def on_click(event):
    print("Boton Presionado")

#aca generamos un boton que vamos a usar en la ventana
boton = tk.Button(ventana, text="Haz click aqui")
boton.pack()

#y usamos bind que tiene la funcionalidad de asociar el evento
# en este caso el str es el evento de presionar el click izquierdo del mouse qeu se asocia con el
# on_click (ejecuta una cierta funcionalidad cuando se hace clic en un botón en este caso el buton-1)
#siempre pongan <> para que python pueda interpretar que esto es un evento
boton.bind("<Button-1>", on_click)

#el buton-3 es el click derecho
boton.bind("<Button-3>", on_click)

#otra funcion podria ser a la hora de presionar alguna tecla del teclado

def on_key_press(event):
    if event.char == "a":

        #aqui es simple solo para demostrar
        # como funciona el evento donde si se cumple el evento cumple con el caracter 'a' este imprimira en consola

        print("Tecla 'a' fue presionada")

#lo mismo solo que ya se comprueba con la tecla eso seria KeyPress
# on_key_press refiere al evento que se acciona cuando se presiona la tecla del teclado, cualquier tecla, la comprobacion esta en la funcion
boton.bind("<KeyPress>", on_key_press)

#otro evento es el de redimencionar la ventana
def on_resize(event):
    print(f"La vetana ha sido redimensionada a {event.width}x{event.height}")

#<configure> nos permite definir como se ejecuta o depura en especifico en este caso para nuestro tamanio de la ventana
#el on_resize solo es pra redefinir o cambiar el tamanio
ventana.bind("<Configure>", on_resize)

#la ejecucion de esto va a aparecer cuando cambiemos el tamanio de la ventana a la hora de depurar y aparecera su tamanio cambiado en consola

#el siguiente es para las coordenadas del cursor del mouse
def on_mouse_move(event):
    print(f"mouse movido a {event.x}, {event.y}")

#<Motion> se utiliza para detectar el movimiento del mouse sobre un widget
ventana.bind("<Motion>", on_mouse_move)

#estos no se usa mucho dudo que lo usemos, porque son coordenadas

ventana.mainloop()
