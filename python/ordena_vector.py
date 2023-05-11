def menu():
     while True:
        print("Menú: ") 
        print("1-Cargar un vector")
        print("2-Ordenar el vector")
        print("3-Mostrar el vector")
        print("f o F -Finalizar el  programa...")
        opc=input("Ingrese su opción: ").lower()
        if opc=='1' or opc=='2' or opc=='3'or opc=='f'or opc=='F':
          return opc
        else:
            print("Opción no válida")

def dimension():
    while True:
        try:
            dimension=input('Ingrese la cantidad de elementos del Vector: ')
            dimension=int(dimension) # me aseguro que sea entero.
               if dimension>1:
                    return dimension
               else:
                    print("Ingrese una dimensión mayor a 1")
        except ValueError:
            print("Error, el valor ingresado no es valido. Reingrese.")


def carga(vector,dimension):
    for x in range(dimension):
        while True:
            try:
                dato=float(input("Ingrese valor:"))
                break
            except ValueError:
                print("Ingrese un valor numérico..")
        vector.append(dato)
    return(vector)

def ordena(vector):#ordena por método de burbuja de mayor a menor
    cant=len(vector)
    for j in range(cant-1):
        for i in range(j,cant):
            if vector[j]<vector[i]:
                vector[i],vector[j]=vector[j],vector[i]
    return vector



cargado=False
while True:
    opcion=menu()
    print("main")
    if opcion=='1':
        vector=[]# ver que pasa si se pone esta línea antes de línea 46, fuera del while
        vector=carga(vector, dimension())
        cargado=True
    elif opcion=='2' and cargado:
        ordena(vector)
    
    elif opcion=='3':
        print("Ud. cargó el vector con los siguientes elementos:")
        print(vector)
    elif opcion=='F'or opcion=='f':
        print("Finalizando..")
        break
