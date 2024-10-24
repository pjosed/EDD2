class Nodo:
    def __init__(self, data = None, next = None):
        self.data = data
        self.next = next

    def __str__(self):
        return str(self.data)

class Lista_enlazada:
    def __init__(self):
        self.head = None

    def add(self, data):
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
        posicion = 0  # Contador de la posición

        while temporal:
            if temporal.data == data:
                return posicion  # Retorna la posición si encuentra el dato
            temporal = temporal.next
            posicion += 1

        return -1  # Retorna -1 si el dato no está en la lista
    def obtener_por_index(self, index):
        """Obtiene el dato en la posición indicada por el índice."""
        temporal = self.head
        posicion = 0

        while temporal:
            if posicion == index:
                return temporal.data  # Retorna el dato si encuentra la posición
            temporal = temporal.next
            posicion += 1

        return None  # Retorna None si el índice es inválido

    def editar_por_index(self, index, nuevo_valor):
        """Edita el dato en la posición indicada por el índice."""
        temporal = self.head
        posicion = 0

        while temporal:
            if posicion == index:
                temporal.data = nuevo_valor  # Cambia el dato del nodo
                return True  # Retorna True si la edición fue exitosa
            temporal = temporal.next
            posicion += 1

        return False  # Retorna False si el índice no es válido
    
    def a_lista(self):
        """Convierte la lista enlazada en una lista normal de Python."""
        lista_normal = []
        temporal = self.head

        while temporal:
            lista_normal.append(temporal.data)  # Agregar el dato a la lista normal
            temporal = temporal.next

        return lista_normal  # Devolver la lista normal

