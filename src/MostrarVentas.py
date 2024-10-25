from tkinter import ttk
import tkinter as tk
import pandas as pd
from LeerRestaurante import LeerRestaurante, guardar_datos_en_excel
from Listaenlazada import Lista_enlazada
from PlotRestaurante import agregar_tabla, agregar_tabla_ventas

def crear_frame_ventas_producto(parent, name):
    # Crear el frame principal
    archivo_excel ="Files/ElSaborAlexander.xlsx"
    frame_modificar_producto = tk.Frame(parent)
    frame_modificar_producto.pack(fill=tk.BOTH, expand=True)

    # Título del frame
    titulo = tk.Label(frame_modificar_producto, text="Ventas de productos.", font=("Arial", 16))
    titulo.pack(pady=10)

    # Crear el frame derecho que ahora ocupará el 100% del espacio
    subframe_derecho = tk.Frame(frame_modificar_producto, bg="lightgreen", relief="ridge", borderwidth=2)
    subframe_derecho.pack(fill=tk.BOTH, expand=True, padx=2, pady=2)

    # Añadir la tabla en el frame derecho
    agregar_tabla_ventas(subframe_derecho, archivo_excel)

    res = LeerRestaurante(archivo_excel)

    # Entradas para modificar un producto
    tk.Label(subframe_derecho, text="Ingrese el Id del producto:", font=("Arial", 12)).pack(pady=5)
    id_entry = tk.Entry(subframe_derecho, font=("Arial", 12))
    id_entry.pack(pady=5)

    tk.Label(subframe_derecho, text="Ingrese la característica a cambiar:", font=("Arial", 12)).pack(pady=5)
    caracteristica_entry = tk.Entry(subframe_derecho, font=("Arial", 12))
    caracteristica_entry.pack(pady=5)

    tk.Label(subframe_derecho, text="Ingrese su nuevo valor:", font=("Arial", 12)).pack(pady=5)
    nuevo_valor_entry = tk.Entry(subframe_derecho, font=("Arial", 12))
    nuevo_valor_entry.pack(pady=5)

    def modificar_recargar():
        caracteristicas = Lista_enlazada()
        caracteristicas.add("Id")
        caracteristicas.add("Categoria")
        caracteristicas.add("Comida")
        caracteristicas.add("Cantidad Disponible")
        caracteristicas.add("Precio")

        index_carac = caracteristicas.buscar(caracteristica_entry.get())
        index_carac_producto = res.obtener_por_index(0).buscar(int(id_entry.get())) 
        nuevo_valor = nuevo_valor_entry.get()

        res.obtener_por_index(index_carac).editar_por_index(index_carac_producto, nuevo_valor)

        guardar_datos_en_excel(res, archivo_excel)

        # Limpiar el contenido del frame derecho y recargar la tabla
        for widget in subframe_derecho.winfo_children():
            widget.destroy()

        agregar_tabla(subframe_derecho, archivo_excel)

    # Botón para modificar el producto
    boton = tk.Button(subframe_derecho, text="Modificar Producto", command=modificar_recargar)
    boton.pack(pady=10)

    return frame_modificar_producto
