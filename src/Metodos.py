import pandas as pd

from Clases import Comida, Comprador, Restaurante
from Listaenlazada import Lista_enlazada

def iniciar_sesion(usuario, contraseña, n): #n=1 restaurante y n=2 comprador
    ingreso=0
    if(n==1):
        usuarios= pd.read_excel("Files/Restaurantes.xlsx")
        for i in range(usuarios.shape[0]-1):
            if((usuario==usuarios.iloc[i+1,0]) & (contraseña==usuarios.iloc[i+1,1])):
                restaurante= Restaurante(usuarios.iloc[i+1,2], usuarios.iloc[i+1,3]) #Crea un restaurante
                print("Ha ingresado como" , restaurante)
                menu= pd.read_excel(restaurante.ruta)#Recibe la ruta del archivo del restaurante y la lee
                ingreso=1
                for i in range(menu.shape[0]-1): #Crea las comidas y las agrega al menú del restaurante
                    comida_res= Comida(menu.iloc[i+1,0],menu.iloc[i+1,2],menu.iloc[i+1,3], menu.iloc[i+1,4], menu.iloc[i+1,1])
                    restaurante.menu.add(comida_res)
                return restaurante
        if(ingreso==0):
            print("Usuario o contraseña incorrecto.")
    else:
        if(n==2):
            usuarios= pd.read_excel("Files/Compradores.xlsx")
            for i in range(usuarios.shape[0]-1):
                if((usuario==usuarios.iloc[i+1,0]) & (contraseña==usuarios.iloc[i+1,1])):
                    comprador = Comprador(usuarios.iloc[i+1,2])
                    print("Ha ingresado como" , comprador)
                    ingreso=1
                    return comprador
            if(ingreso==0):
                print("Usuario o contraseña incorrecto.")

def agregar_producto(restaurante):
    menu= pd.read_excel(restaurante.ruta)
    categoria= input("Ingrese la categoría: ")
    nombre = input("Ingrese el nombre: ")
    cantidad = input("Ingrese la cantidad: ")
    precio = input("Ingrese el precio: ")
    id= menu.shape[0]+1
    comidaNew= Comida(id,nombre, cantidad, precio, categoria)
    nueva_comida= pd.DataFrame({"Id": [id], "Categoria":[categoria], "Comida":[nombre], "Cantidad Disponible":[cantidad], "Precio":[precio]})
    menuactualizado= pd.concat([menu, nueva_comida], ignore_index=True)
    menuactualizado.to_excel(restaurante.ruta, index=False)
    restaurante.menu.add(comidaNew)
    print("Se ha agregado la nueva comida correctamente.")

def agregar_al_carrito(self, restaurante, nombre_comida, cantidad):
       
        # Buscar la comida en el menú del restaurante
        comida = restaurante.menu.head
        while comida:
            if comida.data.nombre.lower() == nombre_comida.lower():
                if comida.data.cantidad >= cantidad:
                    # Crear una copia de la comida para agregar al carrito
                    comida_carrito = Comida(comida.data.id, comida.data.nombre, cantidad, comida.data.precio, comida.data.categoria)
                    self.carrito.add(comida_carrito)
                    comida.data.cantidad -= cantidad  # Reducir la cantidad disponible en el restaurante
                    print(f"Se agregaron {cantidad} unidades de {comida.data.nombre} al carrito.")
                else:
                    print(f"No hay suficiente cantidad disponible de {comida.data.nombre}. Disponible: {comida.data.cantidad}")
                return  # Salir después de encontrar el producto
            comida = comida.next
        
        print(f"{nombre_comida} no se encuentra en el menú del restaurante {restaurante.nombre}.")

def eliminar_del_carrito(self, nombre_comida):
       
        temporal = self.carrito.head
        anterior = None

        while temporal:
            if temporal.data.nombre.lower() == nombre_comida.lower():
                if anterior:
                    anterior.next = temporal.next
                else:
                    self.carrito.head = temporal.next
                print(f"{nombre_comida} fue eliminado del carrito.")
                return
            anterior = temporal
            temporal = temporal.next
        
        print(f"{nombre_comida} no se encuentra en el carrito.")

def mostrar_carrito(self):
        
        print("Carrito de Compras:")
        temporal = self.carrito.head
        if not temporal:
            print("El carrito está vacío.")
        else:
            while temporal:
                c = temporal.data
                print(f"{c.nombre} - Cantidad: {c.cantidad}, Precio unitario: {c.precio}, Total: {c.precio * c.cantidad}")
                temporal = temporal.next

def pagar(self):
       
        total = 0
        temporal = self.carrito.head

        while temporal:
            producto = temporal.data
            total += producto.precio * producto.cantidad
            temporal = temporal.next
        
        if total > 0:
            print(f"Total a pagar: {total:.2f}")
            self.carrito = Lista_enlazada()  # Vaciar el carrito después de pagar
            print("Pago realizado con éxito. Gracias por tu compra.")
        else:
            print("El carrito está vacío. No hay nada que pagar.")
