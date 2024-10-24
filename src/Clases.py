from Listaenlazada import Lista_enlazada


class Restaurante:
    def __init__(self, nombre, ruta):
        self.nombre = nombre
        self.menu = Lista_enlazada()
        self.ruta = ruta

    def __str__(self):
        return str(self.nombre)


class Comida:
    def __init__(self, id, nombre, cantidad, precio, categoria):
        self.nombre = nombre
        self.cantidad = cantidad
        self.precio = precio
        self.categoria = categoria
        self.id = id

    def __str__(self):
        return str(self.nombre)


class Comprador: # Esta es la clase comprador
    def __init__(self, nombre):
        self.nombre = nombre
        self.carrito = Lista_enlazada()

    def __str__(self):
        return str(self.nombre)