from tkinter import ttk
import tkinter as tk
import pandas as pd
from LeerRestaurante import LeerRestaurante, guardar_datos_en_excel
from Listaenlazada import Lista_enlazada
from PlotRestaurante import agregar_tabla

def crear_frame_eliminar_producto(parent, archivo_excel):
    # Crear el frame principal
    frame_modificar_producto = tk.Frame(parent)
    frame_modificar_producto.pack(fill=tk.BOTH, expand=True)

    # Título del frame
    titulo = tk.Label(frame_modificar_producto, text="Eliminar Producto", font=("Arial", 16))
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
    tk.Label(subframe_izquierdo, text="Ingrese el ID del producto:", font=("Arial", 12)).pack(pady=5)
    id_entry = tk.Entry(subframe_izquierdo, font=("Arial", 12))
    id_entry.pack(pady=5)

   

    def eliminar_recargar():
        caracteristicas  =Lista_enlazada()
        caracteristicas.add("Id")
        caracteristicas.add("Categoria")
        caracteristicas.add("Comida")
        caracteristicas.add("Cantidad Disponible")
        caracteristicas.add("Precio")

        
        index_carac_producto = res.obtener_por_index(0).buscar(int(id_entry.get())) 
           

        for i in range(0,5):   
            res.obtener_por_index(i).eliminar_por_index(index_carac_producto)

    
        guardar_datos_en_excel(res, archivo_excel)

        for widget in subframe_derecho.winfo_children():
            widget.destroy()  # Borra cada widget dentro del frame

        agregar_tabla(subframe_derecho , archivo_excel )



    # Botón para cambiar el texto del label
    boton = tk.Button(subframe_izquierdo, text="Eliminar Producto", command=eliminar_recargar)
    boton.pack(pady=10)



 


    




    return frame_modificar_producto    