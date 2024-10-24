import pandas as pd
from Listaenlazada import Lista_enlazada
def LeerRestaurante (ruta):
    res = Lista_enlazada()

    ids = Lista_enlazada()
    categorias = Lista_enlazada()
    comidas = Lista_enlazada()
    cantidad_disponibles = Lista_enlazada()
    precios = Lista_enlazada()

    # Leer el archivo Excel
    datos = pd.read_excel(ruta, engine='openpyxl')

    # Mostrar las filas y agregar a las listas enlazadas
    for index, fila in datos.iterrows():
        ids.add(fila[0])
        categorias.add(fila[1])
        comidas.add(fila[2])
        cantidad_disponibles.add(fila[3])
        precios.add(fila[4])

  

    res.add(ids)
    res.add(categorias)
    res.add(comidas)
    res.add(cantidad_disponibles)
    res.add(precios)



    return res


def limpiar_frame(frame):
    """Elimina todo el contenido del frame."""
    for widget in frame.winfo_children():
        widget.destroy()  # Borra cada widget dentro del frame




def guardar_datos_en_excel(lista_de_columnas, ruta ):
    """
    Recibe una lista de listas, donde cada lista corresponde a una columna.
    Crea un DataFrame con las 5 columnas y lo guarda como Excel en la ruta especificada.
    """
    
    # Crear un DataFrame con las columnas
    columnas = ['Id', 'Categoria', 'Comida', 'Cantidad Disponible', 'Precio']
    df = pd.DataFrame({columnas[i]: lista_de_columnas.a_lista()[i].a_lista() for i in range(5)})


    print(lista_de_columnas.a_lista()[1].a_lista())
    # Guardar el DataFrame en la ubicación especificada
    ruta_excel = ruta
    df.to_excel(ruta_excel, index=False)  # Guardar sin el índice en el Excel

    print(f"Archivo guardado exitosamente en: {ruta_excel}")