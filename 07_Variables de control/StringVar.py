#basicamente las variables de control son objetos especiales en tkinter que nos permite mantener y gestionar los valoes
#de los widgets, como campos de texto o bordes de opcion
#estas variables nos van a facilitar la comunicacion entre los widgets y nuestro codigo en py
#empecemos con StringVar que esta nos sirven como cadenas de texto
import tkinter as tk

ventana = tk.Tk()
ventana.title("Ejemplo StringVar")

texto = tk.StringVar(value="Hola mundo")
#luego esta set que de este modo cambiamos el valor de la variable
texto.set("Nuevo texto")


#de este modo no se deberia de mandar para imprimir porque estamos imprimiendo la viariable y no el valor
print(texto)
#debemos de usar get debido a que es una variable dentro de otra -> texto = StringVar = value = Hola mundo
#entonces con get obtenemos el valor de la varible
print(texto.get())

#ahora como lo podemos aplicar?, osea a un widget para ejecucion en ventana y no en consola
#por ejemplo podria ser asi(aunque hay mucho otros modos
#hacemos un entry que asignamos a ventana y una textvariable este es importante ya que enviamos una variable de control
#aunque tambien podriamos usar un get del siguiente modo -> tk.Entry(ventana, variable=text.get), pero en este caso usamos textvariable
#debido a que usamos un set para actualizar el widget de forma programada
entrada = tk.Entry(ventana, textvariable=texto)
entrada.pack()

#otro ejemplo, tambien podemos ver funciones callback en esto
etiqueta = tk.Label(ventana)
etiqueta.pack()

def actualizar_etiqueta(*args):
    etiqueta.config(text=texto.get())#esto actualiza el texto, oesa el label en pantalla

#lo que hace trace es que detecta el cambio en la variable texto, por lo tanto detecta con la w y pasa a actualizar etiqueta
texto.trace("w", actualizar_etiqueta)

ventana.mainloop()