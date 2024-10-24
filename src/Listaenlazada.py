class Nodo:
    def __init__(self, data=None, next=None):
        self.data = data
        self.next = next

    def __str__(self):
        return str(self.data)


class Lista_enlazada:
    def __init__(self):
        self.head = None

    def add(self, data):
        """Añade un nodo al final de la lista enlazada."""
        if not self.head:
            self.head = Nodo(data=data)
            return
        temporal = self.head
        while temporal.next:
            temporal = temporal.next
        temporal.next = Nodo(data=data)

    def buscar(self, data):
        """Busca un dato en la lista y devuelve su posición (desde 0)."""
        temporal = self.head
        posicion = 0

        while temporal:
            if temporal.data == data:
                return posicion
            temporal = temporal.next
            posicion += 1

        return -1

    def obtener_por_index(self, index):
        """Obtiene el dato en la posición indicada por el índice."""
        temporal = self.head
        posicion = 0

        while temporal:
            if posicion == index:
                return temporal.data
            temporal = temporal.next
            posicion += 1

        return None

    def editar_por_index(self, index, nuevo_valor):
        """Edita el dato en la posición indicada por el índice."""
        temporal = self.head
        posicion = 0

        while temporal:
            if posicion == index:
                temporal.data = nuevo_valor
                return True
            temporal = temporal.next
            posicion += 1

        return False

    def a_lista(self):
        """Convierte la lista enlazada en una lista normal de Python."""
        lista_normal = []
        temporal = self.head

        while temporal:
            lista_normal.append(temporal.data)
            temporal = temporal.next

        return lista_normal

    def eliminar_por_index(self, index):
        """Elimina el nodo en la posición indicada por el índice."""
        if not self.head:
            return False  # La lista está vacía

        # Si se quiere eliminar el primer nodo (índice 0)
        if index == 0:
            self.head = self.head.next  # Cambia la cabeza al siguiente nodo
            return True

        # Recorrer la lista para encontrar el nodo anterior al que se eliminará
        temporal = self.head
        posicion = 0

        while temporal.next:
            if posicion == index - 1:
                # Eliminar el nodo siguiente al actual
                temporal.next = temporal.next.next
                return True  # Eliminación exitosa
            temporal = temporal.next
            posicion += 1

        return False  # Índice fuera de rango