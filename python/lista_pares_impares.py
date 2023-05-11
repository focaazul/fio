def menu():
    op = (input("Menu...\n1.-Cargar \n2.-Buscar \nF.-Fin\nIngrese una opcion: "))
    while (op != '1' and op != '2' and op != 'f' and op != 'F'):
        op = (input("Error, opcion no válida..\nMenu...\n1.-Cargar \n2.-Buscar \nF.-Fin\nIngrese una opcion: "))
    return (op)


def ingreso():  # Esta función valida de sea un entero
    while True:
            try:
                n = int(input("ingrese un nro. entero: "))
                return n
            except ValueError:
                print("Tipo de dato no valido. Reingrese.")


def carga():
        n = 1 # Solo para que ingrese al while
        while (n !=0):
            n = ingreso()
            if n==0:
                break
            if (n%2 ==0):
                pares.append(n)
            else:
                impares.append(n)
        print("Valores pares cargados: ", pares)
        print("Valores pares cargados: ", impares)


def buscar(x):
    b = False
    if(x%2 ==0):
        for i in range(len(pares)):
            if (x ==pares[i]):
                b = True
                print ("El valor {} se encuentra en la posicion {} de los pares".format(x, i+1))
        if not b:
            print("el valor no se encuentra en la lista de pares")
    else:
        for i in range(len(impares)):
            if (x ==impares[i]):
                b = True
                print ("El valor {} se encuentra en la posicion {} de los impares".format(x, i+1))
        if not b:
            print("el valor no se encuentra en la lista de impares")


#Funcion principal
op = menu()
while (op !='f' and op!='F'):
    if (op =='1'):
        pares = []#ver que al estar aqui siempre se resetean antes de cargar
        impares = [] #ver que al estar aqui siempre se resetean antes de cargar
        carga()
    elif (op =='2'):
        x = int(input('Ingrese el nro a buscar: '))
        buscar(x)
    else:
        print("chauuu")
    op = menu()
