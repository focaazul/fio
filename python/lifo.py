def menu():
     while True:
        print ("Menú: ") 
        print("i-Ingresar un elemento a LIFO")
        print("s-Sacar un elemento a LIFO")
        print("m-mostrar LIFO")
        print("f-fin del programa...")
        opc=str(input("Ingrese su opción: "))
        if opc=='i' or opc=='s' or opc=='m'or opc=='f':
          return opc
        else:
            print("Opción no válida")

def pila(lifo, accion):
    if accion=="i":
        lifo.append(int(input("Ingrese valor LIFO: ")))#ver que como NO hay = es el mismo objeto!!
        return True
    elif accion=="s":
        if len(lifo)==0:
            print("La lista esta vacia, no se pueden sacar elementos..")
        else:
            lifo.pop()#ver que como NO hay = es el mismo objeto!!
        return True
    elif accion=="m":
        print(lifo)
        return True
    elif accion=="f":
        print("Finalizando...")
        return(False)
    else:
        print("Argumento invalido...")
        return (True)


lifo=[]#Lista local de main
while True:
    opc=menu()
    if (pila(lifo,opc)):
        print("Continuando...")
    else:
        break
