from tkinter import *

raiz = Tk()

# RAIZ
raiz.geometry("1200x600")
raiz.config(bg="Black")

# FRAMES

# Frame principal
framePrincipal = Frame(raiz, width="600", height="1200")
framePrincipal.pack(fill="both", expand=True)
framePrincipal.config(bg="White")
framePrincipal.config(cursor="hand2")  # PARA LOS BOTONES SE CAMBIA EL ESTILO DE MOUSE

# Labels de frame principal
titulo = Label(framePrincipal, text="Escoja si es usuario o administrador:")
titulo.pack(pady=20)  # Se añade un margen vertical

# Botones
imagenUsuario = PhotoImage(file="C:/Users/Usuario/PycharmProjects/EDD2/images/Usuario.png")
botonUsuario = Button(framePrincipal, image=imagenUsuario)
botonUsuario.pack(side="left", fill="both", expand=True)  # Botón de usuario a la izquierda

imagenRestaurante = PhotoImage(file="C:/Users/Usuario/PycharmProjects/EDD2/images/Restaurante.png")
botonRestaurante = Button(framePrincipal, image=imagenRestaurante)
botonRestaurante.pack(side="right", fill="both", expand=True)  # Botón de restaurante a la derecha

# Ejecutar el bucle principal
raiz.mainloop()
