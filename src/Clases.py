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
    def agregar_al_carrito(self, restaurante, nombre_comida, cantidad):
        comida = restaurante.menu.head
        while comida:
            if comida.data.nombre.lower() == nombre_comida.lower():
                if comida.data.cantidad >= cantidad:
                    comida_carrito = Comida(comida.data.id, comida.data.nombre, cantidad, comida.data.precio, comida.data.categoria)
                    self.carrito.add(comida_carrito)
                    comida.data.cantidad -= cantidad
                    return f"Se agregaron {cantidad} unidades de {comida.data.nombre} al carrito."
                else:
                    return f"No hay suficiente cantidad disponible de {comida.data.nombre}. Disponible: {comida.data.cantidad}"
            comida = comida.next
        return f"{nombre_comida} no se encuentra en el menú del restaurante {restaurante.nombre}."
    def eliminar_del_carrito(self, restaurante, nombre_comida):
        nodo = self.carrito.head
        previo = None
        while nodo:
            if nodo.data.nombre.lower() == nombre_comida.lower():
                # Devolver la cantidad al inventario del restaurante
                comida_menu = restaurante.menu.head
                while comida_menu:
                    if comida_menu.data.id == nodo.data.id:
                        comida_menu.data.cantidad += nodo.data.cantidad
                        break
                    comida_menu = comida_menu.next

                # Eliminar el nodo del carrito
                if previo:
                    previo.next = nodo.next
                else:
                    self.carrito.head = nodo.next

                return f"{nodo.data.nombre} ha sido eliminado del carrito."
            previo = nodo
            nodo = nodo.next

        return f"{nombre_comida} no está en el carrito."

    def pagar(self):
        total = 0
        nodo = self.carrito.head
        while nodo:
            total += nodo.data.precio * nodo.data.cantidad
            nodo = nodo.next

        if total == 0:
            return "El carrito está vacío. No hay nada que pagar."

        # Vaciar el carrito después del pago
        self.carrito.clear()
        return f"El total a pagar es: ${total:.2f}. Pago realizado exitosamente."

    def __str__(self):
        return str(self.nombre)