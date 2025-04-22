import tkinter as tk

#tk dependencia de tkinter y Tk() para mandar a llamar la clase de tkinter
ventana = tk.Tk()

#nombre de la ventana
ventana.title('HELLO WORLD')

#metodo para el tamaño de la ventana y cordenadas, el multiplicar es el tamaño inicial las sumas son las coordenadas donde aparecera la ventana
ventana.geometry("1900x300+100+50")

#metodo para ponerele un limite para hacer chiquita la ventana
ventana.minsize(200, 100)

#lo mismo pero para agrandar
ventana.maxsize(900,1000)

#para cambiar el icono de la ventana
ventana.iconbitmap("icono.png")

#color de fondo se le asigna bg en configura haciendo referencia al backgorund
#mas colores de tkinter https://www.google.com/url?sa=t&rct=j&q=&esrc=s&source=web&cd=&ved=2ahUKEwjWiLGA-uqMAxX3RjABHeyoDf0QFnoECAoQAQ&url=https%3A%2F%2Fcs111.wellesley.edu%2Farchive%2Fcs111_fall14%2Fpublic_html%2Flabs%2Flab12%2Ftkintercolor.html&usg=AOvVaw3OUqRvzq-x5RlFrhVgydrb&opi=89978449
ventana.configure(bg='skyblue')

#metodo para poder bloquear el agrandar o hacer chiquito en este caso lo deje para que se pueda hacer pero si le das false restringe
ventana.resizable(True, True)

#transaparencia de la ventana es alpha y a la par ala transparencia
ventana.attributes("-alpha", 0.9)

#metodo de bucle para que la ventana sea visible
# tod lo que se escriba para la ventana ponganlo antes del ventana.mainloop() porque sino no suceredera en la ventana
ventana.mainloop()
