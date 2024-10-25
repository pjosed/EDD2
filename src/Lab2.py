from tkinter import *
from EliminarProducto import crear_frame_eliminar_producto
from Metodos import *
import openpyxl
from Clases import Restaurante, Comida
from ModificarProducto import crear_frame_modificar_producto
from tkinter import messagebox
import tkinter as tk
#Frames
# Ventana principal
raiz = Tk()
raiz.geometry("1200x600")
raiz.config(bg="Black")

# Frame principal
framePrincipal = Frame(raiz, width="600", height="1200")
framePrincipal.pack(fill="both", expand=True)
framePrincipal.config(bg="White")



def mostrar_frame_modificar_producto():
    frameRestaurante.pack_forget()
    frame_agregar_producto = crear_frame_modificar_producto(raiz,restauranteActual.ruta)
    frame_agregar_producto.pack(fill="both", expand=True)

def mostrar_frame_eliminar_producto():
    frameRestaurante.pack_forget()
    frame_agregar_producto = crear_frame_eliminar_producto(raiz,restauranteActual.ruta)
    frame_agregar_producto.pack(fill="both", expand=True)

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
tituloMostrarMenu = Label(frameMostrarMenu, text="MENÚ", fg="White", bg="Black", font=("Arial", 16))
tituloMostrarMenu.pack(pady=20) 
labelMenu = Label(frameMostrarMenu, text="", justify="left", anchor="w")
labelMenu.pack(pady=20, padx=20)

"""
"""

# Frame iniciar sesión restaurante
frameIniciarSesionRestaurante = Frame(raiz, width="600", height="1200")
frameIniciarSesionRestaurante.config(bg="White")
tituloIniciarSesionRestaurante = Label(frameIniciarSesionRestaurante, text="¡Inicia sesión!")
tituloIniciarSesionRestaurante.pack(pady=20)

# Añadir los labels y entries en el frame de iniciar sesión restaurante usando pack()
# Frame para contener las etiquetas y entradas de usuario y contraseña
frameCampos1 = Frame(frameIniciarSesionRestaurante, bg="White")
frameCampos1.pack(pady=20)

# Etiqueta y entrada para Restaurante
labelUsuario1 = Label(frameCampos1, text="Usuario:", bg="White")
labelUsuario1.pack(anchor="w", pady=5)

entryUsuario1 = Entry(frameCampos1)
entryUsuario1.pack(fill="x", pady=5)

# Etiqueta y entrada para Contraseña
labelContrasena1 = Label(frameCampos1, text="Contraseña:", bg="White")
labelContrasena1.pack(anchor="w", pady=5)

entryContraseña1 = Entry(frameCampos1, show="*")
entryContraseña1.pack(fill="x", pady=5)

bienvenidaUsuario = Label(frameUsuario, text=f"", fg="white", bg="black")

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

entryUsuario = Entry(frameCampos)
entryUsuario.pack(fill="x", pady=5)

# Etiqueta y entrada para Contraseña
labelContrasena = Label(frameCampos, text="Contraseña:", bg="White")
labelContrasena.pack(anchor="w", pady=5)

entryContraseña = Entry(frameCampos, show="*")
entryContraseña.pack(fill="x", pady=5)

# Frame ver producto especifico
frameVerProductoEspecifico = Frame(raiz, width="600", height="1200")
# Labels en verProductoEspecifico
TituloVerProductoEspecifico = Label(frameVerProductoEspecifico, text="Ingresa el producto que quieres buscar:", justify="left", anchor="w").pack(pady=20, padx=20)
labelVerProductoEspecifico = Label(frameVerProductoEspecifico, text="", justify="left", anchor="w")
labelVerProductoEspecifico.pack(pady=20, padx=20)
# Entry para ver producto especifico
entryVerProductoEspecifico = Entry(frameVerProductoEspecifico)
entryVerProductoEspecifico.pack( pady=20, padx=20)



# Método para abrir la ventana de iniciar sesión usuario y cerrar el frame principal
def iniciarSesionUsuario():
    framePrincipal.pack_forget()  # Oculta el frame principal
    frameIniciarSesionUsuario.pack(fill="both", expand=True)  # Muestra el frame de iniciar sesion

# Método para abrir la ventana de iniciar sesión restaurante y cerrar el frame principal
def iniciarSesionRestaurante():
    framePrincipal.pack_forget()  # Oculta el frame principal
    frameIniciarSesionRestaurante.pack(fill="both", expand=True)  # Muestra el frame de iniciar sesion

# Método para mostrar el frame de usuario y ocultar el frame principal
def entrarComoUsuario():
    ingreso = 0
    usuarios = pd.read_excel("Files/Compradores.xlsx")   
    # Obtener el valor ingresado por el usuario
    usuario_ingresado = entryUsuario.get()
    contrasena_ingresada = entryContraseña.get()  # Asegúrate de que tienes un campo para la contraseña 
# Metodo de agregar producto en restaurante
    # Recorrer todos los usuarios en el DataFrame
    for i in range(usuarios.shape[0]):
        # Comparar el usuario y la contraseña ingresados con los del DataFrame
        if usuario_ingresado == usuarios.iloc[i, 0] and contrasena_ingresada == usuarios.iloc[i, 1]:
            frameIniciarSesionUsuario.pack_forget()  # Oculta el frame principal
            frameUsuario.pack(fill="both", expand=True)  # Muestra el frame de usuario
            comprador = Comprador(usuarios.iloc[i, 2])  # Crea el comprador
            print("Ha ingresado como", comprador)
            global bienvenidaUsuario
            bienvenidaUsuario = Label(frameUsuario, text=f"¡Bienvenido, {comprador.nombre}!", fg="white", bg="black")
            bienvenidaUsuario.pack(pady=20)  # Añade el Label al frame de usuario

            ingreso = 1
            return comprador  # Retorna el comprador si el ingreso es exitoso
            
    # Mensaje si no se encontró el usuario o contraseña
    if ingreso == 0:
        print("Usuario o contraseña incorrecto.")


# Método para mostrar el frame de restaurante y ocultar el frame principal
def entrarComoRestaurante():
    global restauranteActual  # variable global
    ingreso = 0
    usuarios = pd.read_excel("Files/Restaurantes.xlsx")
    for i in range(usuarios.shape[0] - 1):
        if (entryUsuario1.get() == usuarios.iloc[i + 1, 0]) & (entryContraseña1.get() == usuarios.iloc[i + 1, 1]):
            frameIniciarSesionRestaurante.pack_forget()  # Oculta el frame iniciar sesion restaurante
            frameRestaurante.pack(fill="both", expand=True)  # Muestra el frame de restaurante
            restauranteActual = Restaurante(usuarios.iloc[i + 1, 2], usuarios.iloc[i + 1, 3])  # Crea un restaurante
            print("Ha ingresado como", restauranteActual)
            bienvenidaRestaurante = Label(frameRestaurante, text=f"¡Bienvenido, {restauranteActual.nombre}!", fg="white", bg="black")
            bienvenidaRestaurante.pack(pady=20)
            menu = pd.read_excel(restauranteActual.ruta)  # Recibe la ruta del archivo del restaurante y la lee
            ingreso = 1
            for i in range(menu.shape[0] - 1):  # Crea las comidas y las agrega al menú del restaurante
                comida_res = Comida(menu.iloc[i + 1, 0], menu.iloc[i + 1, 2], menu.iloc[i + 1, 3], menu.iloc[i + 1, 4], menu.iloc[i + 1, 1])
                restauranteActual.menu.add(comida_res)
            return restauranteActual
    if ingreso == 0:
        print("Usuario o contraseña incorrecto.")
            
def entrarAgregarProducto():
    frameRestaurante.pack_forget()  # Oculta el frame restaurante
    
    frameAgregarProducto.pack(fill="both", expand=True)  # Muestra el frame agregar producto
    
def agregar_producto(restauranteActual):
    if restauranteActual is None:
        print("No se ha seleccionado ningún restaurante.")
        return
    
    # Obtener los valores de los Entry
    categoria = entryCategoria.get()
    nombre = entryNombre.get()
    cantidad = entryCantidad.get()
    precio = entryPrecio.get()
    
    # Leer el menú actual del restaurante
    menu = pd.read_excel(restauranteActual.ruta)
    id = menu.shape[0] + 1  # Generar un nuevo ID para el producto
    comidaNew = Comida(id, nombre, cantidad, precio, categoria)  # Crear una nueva comida
    
    nueva_comida = pd.DataFrame({
        "Id": [id], 
        "Categoria": [categoria], 
        "Comida": [nombre], 
        "Cantidad Disponible": [cantidad], 
        "Precio": [precio]
    })
    
    # Actualizar el menú
    menuactualizado = pd.concat([menu, nueva_comida], ignore_index=True)
    menuactualizado.to_excel(restauranteActual.ruta, index=False)  # Guardar el archivo actualizado
    
    restauranteActual.menu.add(comidaNew)  # Añadir la nueva comida al menú del restaurante
    print("Se ha agregado la nueva comida correctamente.")
    
def entrarEscogerVista(nombreRestaurante):
    global restauranteActual
    restauranteActual = nombreRestaurante
    frameUsuario.pack_forget()  # Oculta el frame usuario
    frameEscogerVista.pack(fill="both", expand=True)  # Muestra el frame agregar producto
    
def mostrar_menu(restauranteActual):
    frameEscogerVista.pack_forget()  # Oculta el frame escogerVista
    frameMostrarMenu.pack(fill="both", expand=True)  # Muestra el frame para mostrarMenu

    try:
        menu_df = pd.read_excel(restauranteActual.ruta)     
        # Crear una cadena de texto para mostrar en el Label
        menu_texto = f"Menú completo de {restauranteActual.nombre}:\n\n"       
        for index, row in menu_df.iterrows():
            menu_texto += f"{row['Id']}      {row['Categoria']}      {row['Comida']}      {row['Cantidad Disponible']}      {row['Precio']}\n"
        # Mostrar el menú en el Label
        labelMenu.config(text=menu_texto)
    
    except Exception as e:
        # Mostrar el error en el Label
        labelMenu.config(text=f"Error al cargar el menú: {e}")

    # Obtener los valores de los Entry
    categoria = entryCategoria.get()
    nombre = entryNombre.get()
    cantidad = entryCantidad.get()
    precio = entryPrecio.get()
    
    # Leer el menú actual del restaurante
    menu = pd.read_excel(restauranteActual.ruta)
    id = menu.shape[0] + 1  # Generar un nuevo ID para el producto
    comidaNew = Comida(id, nombre, cantidad, precio, categoria)  # Crear una nueva comida
    
    nueva_comida = pd.DataFrame({
        "Id": [id], 
        "Categoria": [categoria], 
        "Comida": [nombre], 
        "Cantidad Disponible": [cantidad], 
        "Precio": [precio]
    })
    
    # Actualizar el menú
    menuactualizado = pd.concat([menu, nueva_comida], ignore_index=True)
    menuactualizado.to_excel(restauranteActual.ruta, index=False)  # Guardar el archivo actualizado
    
    restauranteActual.menu.add(comidaNew)  # Añadir la nueva comida al menú del restaurante
    print("Se ha agregado la nueva comida correctamente.")
    
def entrarVerProductoEspecifico():
    frameEscogerVista.pack_forget()  # Oculta el frame ESCOGER VISTA
    frameVerProductoEspecifico.pack(fill="both", expand=True)  # Muestra el frame ver producto especifico
    
def mostrarProductos(entryVerProductoEspecifico):
    # Obtener el valor del Entry
    valor_busqueda = entryVerProductoEspecifico.get().strip().lower()

    # Establecer la opción para mostrar todas las filas
    pd.set_option('display.max_rows', None)

    # Lista de restaurantes con sus archivos de menú
    restaurantes = [
        Restaurante("ElSaborJose", "Files/ElSaborJose.xlsx"),
        Restaurante("ElSaborAna", "Files/ElSaborAna.xlsx"),
        Restaurante("ElSaborAlejandro", "Files/ElSaborAlejandro.xlsx"),
        Restaurante("ElSaborAlexander", "Files/ElSaborAlexander.xlsx"),
        Restaurante("ElSaborJudith", "Files/ElSaborJudith.xlsx")
    ]

    producto_encontrado = False  # Variable para verificar si se encontró el producto en alguno de los restaurantes

    # Iniciar la cadena que contendrá la información de los productos encontrados
    resultado_producto = f"Buscando información del producto '{valor_busqueda}' en todos los restaurantes...\n\n"

    # Iterar sobre la lista de restaurantes
    for restaurante in restaurantes:
        try:
            # Cargar el menú desde el archivo Excel
            menu_df = pd.read_excel(restaurante.ruta)

            # Asegurarse de que la columna 'Comida' existe en el archivo
            if 'Comida' in menu_df.columns:
                # Eliminar espacios y convertir a minúsculas en la columna 'Comida'
                menu_df['Comida'] = menu_df['Comida'].str.strip().str.lower()

                # Filtrar el DataFrame para encontrar el producto
                producto_info = menu_df[menu_df['Comida'] == valor_busqueda]

                if not producto_info.empty:
                    resultado_producto += f"\nProducto encontrado en el restaurante {restaurante.nombre}:\n"
                    for index, row in producto_info.iterrows():
                        resultado_producto += (f"Id: {row['Id']}, Categoría: {row['Categoria']}, "
                                               f"Comida: {row['Comida']}, Cantidad disponible: {row['Cantidad Disponible']}, "
                                               f"Precio: {row['Precio']}\n")
                    producto_encontrado = True

        except Exception as e:
            resultado_producto += f"Error al cargar el menú del restaurante {restaurante.nombre}: {e}\n"

    # Actualizar el Label con el resultado del producto
    labelVerProductoEspecifico.config(text=resultado_producto)
    
def retrocederAFramePrincipal():
    frameIniciarSesionUsuario.pack_forget()  # Oculta el frame iniciar sesioon
    framePrincipal.pack(fill="both", expand=True)  # Muestra el frame principal
    
def retrocederAIniciarSesion():
    frameUsuario.pack_forget()  # Oculta el frame usuario
    frameIniciarSesionUsuario.pack(fill="both", expand=True)  # Muestra el iniciar sesion de usuario
    global bienvenidaUsuario
    if bienvenidaUsuario is not None:
        bienvenidaUsuario.destroy()  # Destruir el Label existente
        bienvenidaUsuario = None  # Reiniciar a None
        
def retrocederAUsuario():
    frameEscogerVista.pack_forget()  # Oculta el frame escoger vista
    frameUsuario.pack(fill="both", expand=True)  # Muestra el frame usuario
    
def retrocederAEscogerVistaMenu():
    frameMostrarMenu.pack_forget()  # Oculta el frame mostrar menu
    frameEscogerVista.pack(fill="both", expand=True)  # Muestra el frame escogerVista
    
def retrocederAEscogerVistaProducto():
    frameVerProductoEspecifico.pack_forget()  # Oculta el frame escoger vista
    frameEscogerVista.pack(fill="both", expand=True)  # Muestra el frame usuario
    
    
    







# Botón Entrar en frame iniciar sesión usuario
botonEntrarUsuario = Button(frameIniciarSesionUsuario, text="Entrar", width=20, height=2, command= entrarComoUsuario)
botonEntrarUsuario.pack(pady=20)

# Botón Entrar en frame iniciar sesión restaurante
botonEntrarRestaurante = Button(frameIniciarSesionRestaurante, text="Entrar", width=20, height=2, command = entrarComoRestaurante)
botonEntrarRestaurante.pack(pady=20)

# Botones en frame principal
imagenUsuario = PhotoImage(file="images/Usuario.png")
botonUsuario = Button(framePrincipal, image=imagenUsuario, command=iniciarSesionUsuario)
botonUsuario.pack(side="left", fill="both", expand=True)

imagenRestaurante = PhotoImage(file="images/Restaurante.png")
botonRestaurante = Button(framePrincipal, image=imagenRestaurante, command=iniciarSesionRestaurante)
botonRestaurante.pack(side="right", fill="both", expand=True)

# Botones en frame restaurante (organizados de forma vertical)
botonAgregar = Button(frameRestaurante, text="Agregar", width=20, height=2, command = entrarAgregarProducto )

botonAgregar.pack(pady=10, side=TOP)

botonModificar = Button(frameRestaurante, text="Modificar", width=20, height=2, command=lambda:  mostrar_frame_modificar_producto())
botonModificar.pack(pady=10, side=TOP)

botonEliminar = Button(frameRestaurante, text="Eliminar", width=20, height=2, command=lambda:  mostrar_frame_eliminar_producto())
botonEliminar.pack(pady=10, side=TOP)

botonRevisarProductosVendidos = Button(frameRestaurante, text="Productos Vendidos", width=20, height=2)
botonRevisarProductosVendidos.pack(pady=10, side=TOP)


# Boton frame agregar producto
botonAñadirProducto = Button(frameAgregarProducto, text="Agregar", fg="black", bg="white", font=("Arial", 16), command=lambda: agregar_producto(restauranteActual))
botonAñadirProducto.pack(side = TOP)

#Botones frame usuario
restaurantes = [Restaurante("ElSaborJose", "Files/ElSaborJose.xlsx"),
                Restaurante("ElSaborAna", "Files/ElSaborAna.xlsx"),
                Restaurante("ElSaborAlexander", "Files/ElSaborAlexander.xlsx"),
                Restaurante("ElSaborAlejandro", "Files/ElSaborAlejandro.xlsx"),
                Restaurante("ElSaborJudith", "Files/ElSaborJudith.xlsx")]

# Botones frame usuario
for restaurante in restaurantes:
    botonRestaurantes = Button(frameUsuario, text=restaurante.nombre, width=20, height=2, command=lambda r=restaurante: entrarEscogerVista(r))
    botonRestaurantes.pack(pady=10)  # Añade un margen vertical entre los botone
    
# Botones escoger vista
botonVerProductoEspecifico = Button(frameEscogerVista, text="Ver producto en todos", width=30, height=2, command=lambda: entrarVerProductoEspecifico())
botonVerProductoEspecifico.pack(pady=10)
botonVerMenu = Button(frameEscogerVista, text="Ver menú", width=20, height=2, command=lambda: mostrar_menu(restauranteActual))
botonVerMenu.pack(pady=10)

#Boton frame ver producto especifico:
botonObtenerProductoEspecifico = Button(frameVerProductoEspecifico, text="Buscar", width=75, height=2, command=lambda: mostrarProductos(entryVerProductoEspecifico))
botonObtenerProductoEspecifico.pack(pady=10)


#Botones de retroceso
# Retroceder de iniciar sesion a frame principal
botonRetrocederAFramePrincipal = Button(frameIniciarSesionUsuario, text="Volver", command=lambda: retrocederAFramePrincipal())
botonRetrocederAFramePrincipal.place(x=0, y=0) 

# Retroceder de frameUsuario a iniciarSesion
botonRetrocederAIniciarSesion = Button(frameUsuario, text="Volver", command=lambda: retrocederAIniciarSesion())
botonRetrocederAIniciarSesion.place(x=0, y=0) 

# Retroceder de escogerVista a usuario
botonRetrocederAUsuario = Button(frameEscogerVista, text="Volver", command=lambda: retrocederAUsuario())
botonRetrocederAUsuario.place(x=0, y=0) 

# Retroceder de verMenu a EscogerVista
botonRetrocederAEscogerVistaMenu = Button(frameMostrarMenu, text="Volver", command=lambda: retrocederAEscogerVistaMenu())
botonRetrocederAEscogerVistaMenu.place(x=0, y=0) 

# Retroceder de verProductoEspecifico a EscogerVista
botonRetrocederAEscogerVistaProducto = Button(frameVerProductoEspecifico, text="Volver", command=lambda: retrocederAEscogerVistaProducto())
botonRetrocederAEscogerVistaProducto.place(x=0, y=0) 

# Frame comprador/carrito
def interfaz_comprador():
    raiz = Tk()
    raiz.geometry("1200x600")
    raiz.config(bg="Black")
    
    comprador = Comprador("Juan")  # Ejemplo de comprador
    restaurante = Restaurante("Restaurante", "files/Restaurantes.xlsx")  # Ejemplo de restaurante cargado

    # Frames existentes más el nuevo Frame del Carrito
    framePrincipal = Frame(raiz, width="600", height="1200")
    framePrincipal.pack(fill="both", expand=True)
    framePrincipal.config(bg="White")

    # Frame carrito de compras (nuevo)
    frameCarritoCompras = Frame(raiz, width="600", height="1200")
    frameCarritoCompras.config(bg="White")

    tituloCarritoCompras = Label(frameCarritoCompras, text="Carrito de Compras", fg="black", bg="white", font=("Arial", 16))
    tituloCarritoCompras.pack(pady=20)

    # Área para mostrar el carrito
    textCarrito = Text(frameCarritoCompras, height=15, width=60)
    textCarrito.pack(pady=10)
    textCarrito.config(state=DISABLED)

    # Entrys para interactuar con el carrito
    Label(frameCarritoCompras, text="Nombre del Producto:", bg="White").pack(anchor="w", padx=10, pady=5)
    entryNombreProductoCarrito = Entry(frameCarritoCompras)
    entryNombreProductoCarrito.pack(fill="x", padx=10, pady=5)

    Label(frameCarritoCompras, text="Cantidad:", bg="White").pack(anchor="w", padx=10, pady=5)
    entryCantidadProductoCarrito = Entry(frameCarritoCompras)
    entryCantidadProductoCarrito.pack(fill="x", padx=10, pady=5)

    # Funciones para manejar el carrito
    def agregar_al_carrito():
        nombre = entryNombreProductoCarrito.get()
        try:
            cantidad = int(entryCantidadProductoCarrito.get())
            mensaje = comprador.agregar_al_carrito(restaurante, nombre, cantidad)
            messagebox.showinfo("Agregar al Carrito", mensaje)
            actualizar_carrito()
        except ValueError:
            messagebox.showerror("Error", "La cantidad debe ser un número entero.")

    def eliminar_del_carrito():
        nombre = entryNombreProductoCarrito.get()
        mensaje = comprador.eliminar_del_carrito(nombre)
        messagebox.showinfo("Eliminar del Carrito", mensaje)
        actualizar_carrito()

    def actualizar_carrito():
        carrito_info = comprador.mostrar_carrito()
        textCarrito.config(state=NORMAL)
        textCarrito.delete(1.0, END)
        textCarrito.insert(END, carrito_info)
        textCarrito.config(state=DISABLED)

    def pagar():
        mensaje = comprador.pagar()
        messagebox.showinfo("Pagar", mensaje)
        actualizar_carrito()

    # Botones para el Frame del Carrito
    botonAgregarCarrito = Button(frameCarritoCompras, text="Agregar al Carrito", command=agregar_al_carrito)
    botonAgregarCarrito.pack(pady=5)

    botonEliminarCarrito = Button(frameCarritoCompras, text="Eliminar del Carrito", command=eliminar_del_carrito)
    botonEliminarCarrito.pack(pady=5)

    botonPagar = Button(frameCarritoCompras, text="Pagar", command=pagar)
    botonPagar.pack(pady=5)

    botonVolver = Button(frameCarritoCompras, text="Volver", command=lambda: frameCarritoCompras.pack_forget())
    botonVolver.pack(pady=5)

    interfaz_comprador()



# Ejecutar el bucle principal
raiz.mainloop()
