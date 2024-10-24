from tkinter import ttk
import tkinter as tk
import pandas as pd
from LeerRestaurante import LeerRestaurante, guardar_datos_en_excel
from Listaenlazada import Lista_enlazada
from PlotRestaurante import agregar_tabla

def crear_frame_modificar_producto(parent, archivo_excel):
    # Crear el frame principal
    frame_modificar_producto = tk.Frame(parent)
    frame_modificar_producto.pack(fill=tk.BOTH, expand=True)

    # Título del frame
    titulo = tk.Label(frame_modificar_producto, text="Modificar Producto", font=("Arial", 16))
    titulo.pack(pady=10)

    # Crear un frame contenedor para los dos subframes
    contenedor_horizontal = tk.Frame(frame_modificar_producto)
    contenedor_horizontal.pack(fill=tk.BOTH, expand=True, padx=2, pady=2)

    # Configurar layout para dividir al 50%
    contenedor_horizontal.columnconfigure(0, weight=1, uniform="col")  # Subframe izquierdo
    contenedor_horizontal.columnconfigure(1, weight=1, uniform="col")  # Subframe derecho
    contenedor_horizontal.rowconfigure(0, weight=1)  # Asegurar expansión vertical

    # Crear el subframe izquierdo
    subframe_izquierdo = tk.Frame(contenedor_horizontal, bg="lightblue", relief="ridge", borderwidth=2)
    subframe_izquierdo.grid(row=0, column=0, sticky="nsew", padx=(0, 1))  # Pequeño margen derecho
    subframe_izquierdo.grid_propagate(False)  # Evitar expansión automática

    # Crear el subframe derecho
    subframe_derecho = tk.Frame(contenedor_horizontal, bg="lightgreen", relief="ridge", borderwidth=2)
    subframe_derecho.grid(row=0, column=1, sticky="nsew", padx=(1, 0))  # Pequeño margen izquierdo
    subframe_derecho.grid_propagate(False)  # Evitar expansión automática

    # Añadir la tabla en el subframe derecho
    agregar_tabla(subframe_derecho, archivo_excel)

    res = LeerRestaurante(archivo_excel)

    ##Crear botones y entry
    # Entradas para modificar un producto
    tk.Label(subframe_izquierdo, text="Ingrese el índice del producto:", font=("Arial", 12)).pack(pady=5)
    id_entry = tk.Entry(subframe_izquierdo, font=("Arial", 12))
    id_entry.pack(pady=5)

    tk.Label(subframe_izquierdo, text="Ingrese la característica a cambiar:", font=("Arial", 12)).pack(pady=5)
    caracteristica_entry = tk.Entry(subframe_izquierdo, font=("Arial", 12))
    caracteristica_entry.pack(pady=5)

    tk.Label(subframe_izquierdo, text="Ingrese su nuevo valor:", font=("Arial", 12)).pack(pady=5)
    nuevo_valor_entry = tk.Entry(subframe_izquierdo, font=("Arial", 12))
    nuevo_valor_entry.pack(pady=5)

    

    def modificar_recargar():
        caracteristicas  =Lista_enlazada()
        caracteristicas.add("Id")
        caracteristicas.add("Categoria")
        caracteristicas.add("Comida")
        caracteristicas.add("Cantidad Disponible")
        caracteristicas.add("Precio")

        index_carac = caracteristicas.buscar(caracteristica_entry.get())
        index_carac_producto = res.obtener_por_index(0).buscar(int(id_entry.get())) 
           
        nuevo_valor = nuevo_valor_entry.get()  

        res.obtener_por_index(index_carac).editar_por_index( index_carac_producto, nuevo_valor) 

        guardar_datos_en_excel(res, archivo_excel)

        for widget in subframe_derecho.winfo_children():
            widget.destroy()  # Borra cada widget dentro del frame

        agregar_tabla(subframe_derecho , archivo_excel )



    # Botón para cambiar el texto del label
    boton = tk.Button(subframe_izquierdo, text="Cambiar Texto", command=modificar_recargar)
    boton.pack(pady=10)



 


    




    return frame_modificar_producto    
    """
    Crea un frame con el título "Modificar Producto" y muestra los datos de un archivo Excel.

    Parámetros:
    - parent: el widget padre donde se colocará el frame.
    - archivo_excel: la ruta del archivo Excel.

    Retorna:
    - frame_modificar_producto: el frame creado.
    
 
    

    # Inicializar listas enlazadas
    ids = Lista_enlazada()
    categorias = Lista_enlazada()
    comidas = Lista_enlazada()
    cantidad_disponibles = Lista_enlazada()
    precios = Lista_enlazada()

  

    

    # Mostrar las columnas
    tk.Label(frame_modificar_producto, text="¿Qué producto desea modificar?", font=("Arial", 12)).pack(pady=5)

    columnas = ", ".join(datos.columns)
    tk.Label(frame_modificar_producto, text=f"Columnas: {columnas}", font=("Arial", 10)).pack(anchor='w')



        texto_fila = ', '.join(map(str, fila.tolist()))
        tk.Label(frame_modificar_producto, text=texto_fila, font=("Arial", 10)).pack(anchor='w')

    # Entradas para modificar un producto
    tk.Label(frame_modificar_producto, text="Ingrese el índice del producto:", font=("Arial", 12)).pack(pady=5)
    id_entry = tk.Entry(frame_modificar_producto, font=("Arial", 12))
    id_entry.pack(pady=5)

    tk.Label(frame_modificar_producto, text="Ingrese la característica a cambiar:", font=("Arial", 12)).pack(pady=5)
    caracteristica_entry = tk.Entry(frame_modificar_producto, font=("Arial", 12))
    caracteristica_entry.pack(pady=5)

    tk.Label(frame_modificar_producto, text="Ingrese su nuevo valor:", font=("Arial", 12)).pack(pady=5)
    nuevo_valor_entry = tk.Entry(frame_modificar_producto, font=("Arial", 12))
    nuevo_valor_entry.pack(pady=5)

    # Label para mostrar resultado después de presionar el botón
    resultado_label = tk.Label(frame_modificar_producto, text="Presiona el botón para cambiar el texto", font=("Arial", 12))
    resultado_label.pack(pady=10)

 

    # Botón para cambiar el texto del label
    boton = tk.Button(frame_modificar_producto, text="Cambiar Texto", command=cambiar_texto)
    boton.pack(pady=10)
        """



        




# - 1 . frame_agregar_producto = crear_frame_modificar_producto(raiz)

# 2. def mostrar_frame_modificar_producto():
    #    pppppppppppppppppppppppppppppppp.pack_forget()
    #    frame_agregar_producto.pack(fill="both", expand=True)

# 3. botonModificar = Button(frameRestaurante, text="Modificar", width=20, height=2, command = mostrar_frame_modificar_producto)
##   botonModificar.pack(pady=10, side=TOP)
##




