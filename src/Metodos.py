import pandas as pd

from Clases import Comida, Comprador, Restaurante

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