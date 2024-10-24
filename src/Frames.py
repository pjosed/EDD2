from tkinter import *
from Metodos import *
import openpyxl
from Clases import Restaurante, Comida

# Ventana principal
raiz = Tk()
raiz.geometry("1200x600")
raiz.config(bg="Black")

# Frame principal
framePrincipal = Frame(raiz, width="600", height="1200")
framePrincipal.pack(fill="both", expand=True)
framePrincipal.config(bg="White")

# Labels de frame principal
titulo = Label(framePrincipal, text="Escoja si es usuario o administrador:")
titulo.pack(pady=20)  # Se añade un margen vertical

# Frame usuario
frameUsuario = Frame(raiz, width="600", height="1200")
frameUsuario.config(bg="Black")
# Título en el frame usuario
tituloSeleccion = Label(frameUsuario, text="Escoge el restaurante que quieres ver!", fg="White", bg="Black", font=("Arial", 16))
tituloSeleccion.pack(pady=20)  # Añade un margen vertical

# Frame escogerVista
frameEscogerVista = Frame(raiz, width="600", height="1200")
# Labels en escoger vista
tituloEscogerVista = Label(frameEscogerVista, text="Escoge como quieres buscar tus productos:", fg="White", bg="Black", font=("Arial", 16))
tituloEscogerVista.pack(pady=20) 

# Frame mostrarMenu
frameMostrarMenu = Frame(raiz, width="600", height="1200")
# Labels en mostrarMenu
tituloMostrarMenu = Label(frameMostrarMenu, text="El menú de este restaurante es:", fg="White", bg="Black", font=("Arial", 16))
tituloMostrarMenu.pack(pady=20) 
labelMenu = Label(frameMostrarMenu, text="", justify="left", anchor="w")
labelMenu.pack(pady=20, padx=20)

# Frame ver producto especifico
frameVerProductoEspecifico = Frame(raiz, width="600", height="1200")
frameVerProductoEspecifico.pack_forget()
# Labels en verProductoEspecifico
labelVerProductoEspecifico = Label(frameVerProductoEspecifico, text="", justify="left", anchor="w")
labelVerProductoEspecifico.pack(pady=20, padx=20)
# Entry para ver producto especifico
entryVerProductoEspecifico = Entry(frameVerProductoEspecifico)
entryVerProductoEspecifico.pack( pady=20, padx=20)

# Frame restaurante
frameRestaurante = Frame(raiz, width="600", height="1200")
frameRestaurante.config(bg="White")

# Frame agregar producto
frameAgregarProducto = Frame(raiz, width="600", height="1200")
frameAgregarProducto.config(bg="White")
# Titulo del frame
tituloAgregarProducto = Label(frameAgregarProducto, text="Agregar Producto", fg="black", bg="white", font=("Arial", 16))
tituloAgregarProducto.pack(pady=20)
# Entrys para la categoría, nombre, cantidad y precio
Label(frameAgregarProducto, text="Categoría:", bg="White").pack(anchor="w", padx=10, pady=5)
entryCategoria = Entry(frameAgregarProducto)
entryCategoria.pack(fill="x", padx=10, pady=5)
Label(frameAgregarProducto, text="Nombre:", bg="White").pack(anchor="w", padx=10, pady=5)
entryNombre = Entry(frameAgregarProducto)
entryNombre.pack(fill="x", padx=10, pady=5)
Label(frameAgregarProducto, text="Cantidad:", bg="White").pack(anchor="w", padx=10, pady=5)
entryCantidad = Entry(frameAgregarProducto)
entryCantidad.pack(fill="x", padx=10, pady=5)
Label(frameAgregarProducto, text="Precio:", bg="White").pack(anchor="w", padx=10, pady=5)
entryPrecio = Entry(frameAgregarProducto)
entryPrecio.pack(fill="x", padx=10, pady=5)




# Frame iniciar sesión usuario
frameIniciarSesionUsuario = Frame(raiz, width="600", height="1200")
frameIniciarSesionUsuario.config(bg="White")
tituloIniciarSesionUsuario = Label(frameIniciarSesionUsuario, text="¡Inicia sesión!")
tituloIniciarSesionUsuario.pack(pady=20)

# Añadir los labels y entries en el frame de iniciar sesión usuario usando pack()
# Frame para contener las etiquetas y entradas de usuario y contraseña
frameCampos = Frame(frameIniciarSesionUsuario, bg="White")
frameCampos.pack(pady=20)

# Etiqueta y entrada para Usuario
labelUsuario = Label(frameCampos, text="Usuario:", bg="White")
labelUsuario.pack(anchor="w", pady=5)
