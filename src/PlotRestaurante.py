import tkinter as tk
from tkinter import ttk

import pandas as pd

def agregar_tabla(frame,archivo_excel ):
        # Leer el archivo Excel
    
    df = pd.read_excel(archivo_excel)

    # Definir las columnas para la tabla con base en el archivo Excel
    columnas = list(df.columns)  # Extraer los nombres de las columnas del DataFrame

    # Crear el widget Treeview para la tabla
    tabla = ttk.Treeview(frame, columns=columnas, show="headings")

    # Definir los encabezados y columnas
    for col in columnas:
        tabla.heading(col, text=col)  # Título de la columna
        tabla.column(col, anchor=tk.CENTER, stretch=True)  # Centrar contenido

    # Insertar los datos del DataFrame en la tabla
    for index, row in df.iterrows():
        tabla.insert("", tk.END, values=list(row))  # Insertar cada fila del Excel

    # Colocar la tabla en el frame con scroll
    tabla.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

    # Crear scrollbars vertical y horizontal
    scroll_y = ttk.Scrollbar(frame, orient=tk.VERTICAL, command=tabla.yview)
    scroll_x = ttk.Scrollbar(frame, orient=tk.HORIZONTAL, command=tabla.xview)

    # Configurar los scrollbars en la tabla
    tabla.configure(yscrollcommand=scroll_y.set, xscrollcommand=scroll_x.set)

    # Colocar la tabla y los scrollbars en el frame usando grid
    tabla.grid(row=0, column=0, sticky="nsew")  # Expandir la tabla
    scroll_y.grid(row=0, column=1, sticky="ns")  # Scroll vertical a la derecha
    scroll_x.grid(row=1, column=0, sticky="ew")  # Scroll horizontal abajo

    # Configurar la distribución del frame
    frame.grid_rowconfigure(0, weight=1)  # Permitir expansión vertical
    frame.grid_columnconfigure(0, weight=1)  # Permitir expansión horizontal


def agregar_tabla_ventas(frame,name ):
        # Leer el archivo Excel
    
    df = pd.read_excel("Files/Ventas.xlsx")
    df = df[df["Restaurante"] == name]
    df = df.drop("Restaurante", axis=1)
    df = df.groupby('Comida')[['Cantidad Vendida', 'Precio Total']].sum().reset_index()

    # Definir las columnas para la tabla con base en el archivo Excel
    columnas = list(df.columns)  # Extraer los nombres de las columnas del DataFrame

    # Crear el widget Treeview para la tabla
    tabla = ttk.Treeview(frame, columns=columnas, show="headings")


    # Definir los encabezados y columnas
    for col in columnas:
        
        tabla.heading(col, text=col)  # Título de la columna
        tabla.column(col, anchor=tk.CENTER, stretch=True)  # Centrar contenido

    # Insertar los datos del DataFrame en la tabla
    for index, row in df.iterrows():
        tabla.insert("", tk.END, values=list(row))  # Insertar cada fila del Excel

    # Colocar la tabla en el frame con scroll
    tabla.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

    # Crear scrollbars vertical y horizontal
    scroll_y = ttk.Scrollbar(frame, orient=tk.VERTICAL, command=tabla.yview)
    scroll_x = ttk.Scrollbar(frame, orient=tk.HORIZONTAL, command=tabla.xview)

    # Configurar los scrollbars en la tabla
    tabla.configure(yscrollcommand=scroll_y.set, xscrollcommand=scroll_x.set)

    # Colocar la tabla y los scrollbars en el frame usando grid
    tabla.grid(row=0, column=0, sticky="nsew")  # Expandir la tabla
    scroll_y.grid(row=0, column=1, sticky="ns")  # Scroll vertical a la derecha
    scroll_x.grid(row=1, column=0, sticky="ew")  # Scroll horizontal abajo

    # Configurar la distribución del frame
    frame.grid_rowconfigure(0, weight=1)  # Permitir expansión vertical
    frame.grid_columnconfigure(0, weight=1)  # Permitir expansión horizontal