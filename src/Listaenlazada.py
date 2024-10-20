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