from tkinter import ttk
import tkinter as tk
import pandas as pd
from LeerRestaurante import LeerRestaurante, guardar_datos_en_excel
from Listaenlazada import Lista_enlazada
from PlotRestaurante import agregar_tabla, agregar_tabla_ventas



def crear_frame_ventas_producto(parent, name, frame_anterior):
    # Crear el frame principal
    archivo_excel ="Files/Ventas.xlsx"
    frame_modificar_producto = tk.Frame(parent)
    frame_modificar_producto.pack(fill=tk.BOTH, expand=True)

    # Título del frame
    titulo = tk.Label(frame_modificar_producto, text="Ventas de productos.", font=("Arial", 16))
    titulo.pack(pady=10)

    # Crear el frame derecho que ahora ocupará el 100% del espacio
    subframe_derecho = tk.Frame(frame_modificar_producto, bg="lightgreen", relief="ridge", borderwidth=2)
    subframe_derecho.pack(fill=tk.BOTH, expand=True, padx=2, pady=2)

    # Añadir la tabla en el frame derecho
    agregar_tabla_ventas(subframe_derecho, name)


    def volver():
        frame_modificar_producto.pack_forget()
        frame_anterior.pack(fill="both", expand=True)
        

    

    # Botón 'Atrás' usando place()
    boton_atras = tk.Button(frame_modificar_producto, text="Atrás",command=volver)
    boton_atras.place(relx=0.95, rely=0.025, anchor="ne")  # Posicionar en la esquina superior derecha

    return frame_modificar_producto



