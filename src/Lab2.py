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
    
def entrarEscogerVista():
    frameUsuario.pack_forget()  # Oculta el frame restaurante
    frameEscogerVista.pack(fill="both", expand=True)  # Muestra el frame agregar producto
    
def mostrar_menu(restauranteActual):
    try:
        menu_df = pd.read_excel(restauranteActual.ruta) 
        
        print(f"Menú completo de {restauranteActual.nombre}:")
        for index, row in menu_df.iterrows():
            print(f"Id: {row['Id']}, Categoría: {row['Categoria']}, Comida: {row['Comida']}, Cantidad disponible:: {row['Cantidad Disponible']}, Precio: {row['Precio']}")
    
    except Exception as e:
        print("Error al cargar el menú:", e)
        
    
    
    # ENTRYS
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

""" def agregar_producto(restaurante):
    # Obtener los valores de los Entry
    categoria = entryCategoria.get()
    nombre = entryNombre.get()
    cantidad = entryCantidad.get()
    precio = entryPrecio.get()
    
    # Leer el menú actual
    menu = pd.read_excel(restaurante.ruta)
    id = menu.shape[0] + 1
    comidaNew = Comida(id, nombre, cantidad, precio, categoria)
    nueva_comida = pd.DataFrame({"Id": [id], "Categoria": [categoria], "Comida": [nombre], "Cantidad Disponible": [cantidad], "Precio": [precio]})
    
    # Actualizar el menú
    menuactualizado = pd.concat([menu, nueva_comida], ignore_index=True)
    menuactualizado.to_excel(restaurante.ruta, index=False)
    restaurante.menu.add(comidaNew)
    
    print("Se ha agregado la nueva comida correctamente.")


 """
# Botón Entrar en frame iniciar sesión usuario
botonEntrarUsuario = Button(frameIniciarSesionUsuario, text="Entrar", width=20, height=2, command= entrarComoUsuario)
botonEntrarUsuario.pack(pady=20)

# Frame iniciar sesión restaurante
frameIniciarSesionRestaurante = Frame(raiz, width="600", height="1200")
frameIniciarSesionRestaurante.config(bg="White")
tituloIniciarSesionRestaurante = Label(frameIniciarSesionRestaurante, text="¡Inicia sesión!")
tituloIniciarSesionRestaurante.pack(pady=20)

# Añadir los labels y entries en el frame de iniciar sesión restaurante usando pack()
# Frame para contener las etiquetas y entradas de usuario y contraseña
frameCampos1 = Frame(frameIniciarSesionRestaurante, bg="White")
frameCampos1.pack(pady=20)

# Etiqueta y entrada para Usuario
labelUsuario1 = Label(frameCampos1, text="Usuario:", bg="White")
labelUsuario1.pack(anchor="w", pady=5)

entryUsuario1 = Entry(frameCampos1)
entryUsuario1.pack(fill="x", pady=5)

# Etiqueta y entrada para Contraseña
labelContrasena1 = Label(frameCampos1, text="Contraseña:", bg="White")
labelContrasena1.pack(anchor="w", pady=5)

entryContraseña1 = Entry(frameCampos1, show="*")
entryContraseña1.pack(fill="x", pady=5)

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

botonModificar = Button(frameRestaurante, text="Modificar", width=20, height=2)
botonModificar.pack(pady=10, side=TOP)

botonEliminar = Button(frameRestaurante, text="Eliminar", width=20, height=2)
botonEliminar.pack(pady=10, side=TOP)

botonRevisarProductosVendidos = Button(frameRestaurante, text="Productos Vendidos", width=20, height=2)
botonRevisarProductosVendidos.pack(pady=10, side=TOP)

botonRevisarCantidadProductosVendida = Button(frameRestaurante, text="Cantidad Vendida", width=20, height=2)
botonRevisarCantidadProductosVendida.pack(pady=10, side=TOP)

botonRevisarGanancia = Button(frameRestaurante, text="Cantidad Vendida", width=20, height=2)
botonRevisarGanancia.pack(pady=10, side=TOP)

botonVerProductos = Button(frameRestaurante, text="Ver productos", width=20, height=2)
botonVerProductos.pack(pady=10, side=TOP)

# Boton frame agregar producto
botonAñadirProducto = Button(frameAgregarProducto, text="Agregar", fg="black", bg="white", font=("Arial", 16), command=lambda: agregar_producto(restauranteActual))
botonAñadirProducto.pack(side = TOP)

#Botones frame usuario
nombres_restaurantes = ["ElSaborJose", "ElSaborAna", "ElSaborAlexander", "ElSaborAlejandro", "ElSaborJudith"]
for nombre in nombres_restaurantes:
    boton = Button(frameUsuario, text=nombre, width=20, height=2, command = entrarEscogerVista)
    boton.pack(pady=10)  # Añade un margen vertical entre los botones
    
# Botones escoger vista
botonVerProductoEspecifico = Button(frameEscogerVista, text="Ver producto específico", width=20, height=2)
botonVerProductoEspecifico.pack(pady=10)
botonVerMenu = Button(frameEscogerVista, text="Ver menú", width=20, height=2, command = lambda: mostrar_menu(restauranteActual))
botonVerMenu.pack(pady=10)

# Ejecutar el bucle principal
raiz.mainloop()
