from tkinter import ttk
import tkinter as tk
import pandas as pd
from Listaenlazada import Lista_enlazada

def crear_frame_modificar_producto(parent, archivo_excel):
    """
    Crea un frame con el título "Modificar Producto" y muestra los datos de un archivo Excel.

    Parámetros:
    - parent: el widget padre donde se colocará el frame.
    - archivo_excel: la ruta del archivo Excel.

    Retorna:
    - frame_modificar_producto: el frame creado.
    """
    # Crear el frame
    frame_modificar_producto = tk.Frame(parent)

    # Inicializar listas enlazadas
    ids = Lista_enlazada()
    categorias = Lista_enlazada()
    comidas = Lista_enlazada()
    cantidad_disponibles = Lista_enlazada()
    precios = Lista_enlazada()

    # Título del frame
    titulo = tk.Label(frame_modificar_producto, text="Modificar Producto", font=("Arial", 16))
    titulo.pack(pady=20)

    # Leer el archivo Excel
    datos = pd.read_excel("Files/ElSaborAlexander.xlsx", engine='openpyxl')

    # Mostrar las columnas
    tk.Label(frame_modificar_producto, text="¿Qué producto desea modificar?", font=("Arial", 12)).pack(pady=5)

    columnas = ", ".join(datos.columns)
    tk.Label(frame_modificar_producto, text=f"Columnas: {columnas}", font=("Arial", 10)).pack(anchor='w')

    # Mostrar las filas y agregar a las listas enlazadas
    for index, fila in datos.iterrows():
        ids.add(fila[0])
        categorias.add(fila[1])
        comidas.add(fila[2])
        cantidad_disponibles.add(fila[3])
        precios.add(fila[4])

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

    # Función que cambia el texto del label al presionar el botón
    def cambiar_texto():
        indice = int(id_entry.get()) # Obtener texto del Entry del índice
        caracteristica = caracteristica_entry.get()  # Obtener texto del Entry de característica
        nuevo_valor = nuevo_valor_entry.get()  # Obtener texto del Entry de nuevo valor

        # Actualizar el label con los valores obtenidos
        resultado_label.config(text=f"comidas: {comidas.obtener_por_index(ids.buscar(indice))}")

    # Botón para cambiar el texto del label
    boton = tk.Button(frame_modificar_producto, text="Cambiar Texto", command=cambiar_texto)
    boton.pack(pady=10)

    return frame_modificar_producto



# - 1 . frame_agregar_producto = crear_frame_modificar_producto(raiz)

# 2. def mostrar_frame_modificar_producto():
    #    pppppppppppppppppppppppppppppppp.pack_forget()
    #    frame_agregar_producto.pack(fill="both", expand=True)

# 3. botonModificar = Button(frameRestaurante, text="Modificar", width=20, height=2, command = mostrar_frame_modificar_producto)
##   botonModificar.pack(pady=10, side=TOP)
##




