#pack es mas simple que el grid y util para organizar widgets en bloques, ya sea horizontal o vertical, aunque no es tan preciso como el gridpero facil y rapuido de usar
import tkinter as tk

ventana = tk.Tk()
ventana.title("ejemplo pack")

#creamos frames y los posicionamos con pack
#en el caso de pack se van organizando por si solos tiene un orden lineal el primer pack ira primero y asi hasta el numero de pack que hayan
#los packs tambien se pueden organizar por ejemplo con side y dando la orden como se vana ordenar o con pad margin o border
#por ejemplo con side en este caso estan todos a la izquierda entonces se ordenaran horizontalmente si no se especifica con size(left o right) se ordenara de arriba a abajp
frame_botones = tk.Frame(ventana)
frame_botones.pack(pady=10)

boton1 = tk.Button(frame_botones, text="Boton 1")
boton1.pack(side="left", padx=5)

boton2 = tk.Button(frame_botones, text="Boton 2")
boton2.pack(side="left", padx=5)

boton3 = tk.Button(frame_botones, text="Boton 3")
boton3.pack(side="left", padx=5)

ventana.mainloop()