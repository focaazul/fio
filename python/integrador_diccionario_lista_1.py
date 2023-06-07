"""
Created on Wed Jun  7 12:53:38 2023

@author: Daniel Refosco
"""

#Funcion menu-----------------------------------------        
def menu():
     while True:
        print("1-Cargar")
        print("2-Vender")
        print("3-Listar")
        print("4-Caja")
        print("5-Baja")
        print("f o F-Finalizar")
        opc=input("Ingrese su opcion: ")
        if opc=='1' or opc=='2' or opc=='3' or opc=='4' or opc=='5' or opc=='f' or opc=='F':
             return opc
        else:
             print("Opcion ingresada no valida..reingrese")

#Funcion cargar-----------------------------------------
def cargar(stock):
    producto=input("Ingrese el nombre del producto:")
    lista=[]
    if not producto in stock: # si NO estaba cargado cargo precio,cantidad y peso
        while True:
            peso=float(input("Ingrese el peso:"))
            if peso>0:
                break
            else:
                print("Valor no valido, reingrese ")
        while True:
                    cantidad=int(input("Ingrese cantidad:"))
                    if cantidad>0:
                        break
                    else:
                        print("Valor no valido, reingrese ")
        while True:
                    precio=float(input("Ingrese precio unitario:"))
                    if precio>0:
                        break
                    else:
                        print("Valor no valido, reingrese ")
        lista.append(peso)
        lista.append(cantidad)
        lista.append(precio)
        stock[producto]=lista
        print(stock)
        return True
    else: # si ya estaba cargado modifico precio,cantidad y peso
        print("El producto ya fué cagrado previamente..")
        print("vamos a modificar precio, cantidad, peso")
        while True:
            peso=float(input("Ingrese el peso:"))
            if peso>0:
                break
            else:
                print("Valor no valido, reingrese ")
        while True:
                cantidad=int(input("Ingrese cantidad:"))
                if cantidad>0:
                    break
                else:
                    print("Valor no valido, reingrese ")
        while True:
                precio=float(input("Ingrese precio unitario:"))
                if precio>0:
                    break
                else:
                    print("Valor no valido, reingrese ")
        #del stock[producto]
        lista.append(peso)
        lista.append(cantidad)
        lista.append(precio)
        stock[producto]=lista
        print(stock)
        return True
    
#Funcion vender_-----------------------------------------
def vender(x, n):
    lista=[]#lista para almacenar solo una venta.
    if x in stock:#¿existe el producto?
        if stock[x][1]-n<0: #no alcanza stock
            return lista #lista vacia
        else:# si existe.
            stock[x][1]=stock[x][1]-n
            lista.append(n)
            lista.append(n*stock[x][2])
            return lista # regreso lo vendido en lista 
    else:
         return lista


#Funcion listar-----------------------------------------
def listar(n):
     for i in stock:
        if stock[i][1]>n:
             print(i,stock[i])
               

#Funcion caja_-----------------------------------------
#esta función caja podria ser distinta si la lista no carga los totales
#es decir va cargando por cada venta una lista con un par de valores por cada venta
# o una lista con indices pares numeros de venta e indices impares con motnos.
def caja(ventas):
     print("numero de ventas:",ventas[0])
     print("monto total de ventas:",ventas[1])
        
def baja(producto):
    if producto in stock:
          del stock[producto]
          return True
    else:
         return False

        
        
#Funcion principal._-----------------------------------------
stock={} #para almacenar producto:peso,cantidad,peso
ventas=[0,0]#para almacentar las ventas diarias
cargado=False
while True:
    opc=menu()
    if opc=='1':
        cargado=cargar(stock)
        cargado=True
    elif opc=='2':
        if not cargado:
            print("No se cargó el diccionario")
        else:
            temp=[]
            x=input("ingrese en nombre del producto: ")
            while True:
                    n=int(input("Ingrese cantidad:"))
                    if n>0:
                        break
                    else:
                        print("Valor no valido, reingrese ")
            temp=vender(x,n)#analizo que tiene lista de venta temporal
            if len(temp)==0:#si la lista esta vacia no se pudo vender
                 print("No se pudo realizar la venta.")
            else:
                ventas[0]=ventas[0]+temp[0] # sumo número de ventas.
                ventas[1]=ventas[1]+temp[1] # sumo los montos de las ventas
            print("cantidad:", ventas[0],"monto; ", ventas[1])
    elif opc=='3':
        if not cargado:
            print("No se cargó el diccionario")
        else:
            while True:
                    n=int(input("Ingrese cantidad:"))
                    if n>0:
                        break
                    else:
                        print("Valor no valido, reingrese ")
            listar(n)
         
    elif opc=='4':
        if not cargado:
            print("No se cargó el diccionario")
        else:
            caja(ventas)
    elif opc=='5':
        if not cargado:
            print("No se cargó el diccionario")
        else:
            x=input("ingrese en nombre del producto: ")
            if baja(x):
                 print("Se eliminó el producto")
            else:
                 print("No existe el producto a eliminar")
        print(stock)

    elif opc=='f' or opc=='F':
        print("Fin del programa")
        break 
          

