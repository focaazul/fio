'''Consigna:
Cargar una una matriz con números reales definiendo las dimensiones durante la ejecución.'''

def menu():
     while True:
        print("Menú: ") 
        print("1-Cargar un vector")
        print("2-Mostrar el vector")
        print("f o F -Finalizar el  programa...")
        opc=input("Ingrese su opción: ").lower()
        if opc=='1' or opc=='2' or opc=='f'or opc=='F':
          return opc
        else:
            print("Opción no válida")

def dimension():
    while True:
        dimensiones=[]
        try:
            while True:
                while True:
                    try:
                        fila=input('Ingrese la cantidad de Filas de la matriz: ')
                        fila=int(fila) # me aseguro que sea entero.
                        break
                    except ValueError:
                        print("Error en tipo de datos.")
                if fila >0:#para validar nro. fila
                    break
                else:
                    print("La cantidad de filas debe ser un número positivo ")
            
            while True: #para valida nro de columna
                while True:
                    try:
                        columna=input('Ingrese la cantidad de Columnas de la matriz: ')
                        columna=int(columna) # me aseguro que sea entero.
                        break
                    except ValueError:
                        print("Error en tipo de datos.")
                if columna >0:
                    break
                else:
                    print("La cantidad de columnas debe ser un número positivo ")
            dimensiones.append(fila)
            dimensiones.append(columna)
            return dimensiones # regreso una lista con la cant. de filas y columnas
        except ValueError:
            print("Error, el valor ingresado no es valido. Reingrese.")


def carga(matriz,dimension):
    for x in range(dimension[0]): #dimensión[0] es nro de filas
            lista=[]
            matriz.append(lista)
            for z in range(dimension[1]): #dimensión[1] es nro de columnas
                while True:
                    try:
                        dato=float(input("Ingrese valor:"))
                        break
                    except ValueError:
                        print("Ingrese un valor numérico..")
                matriz[x].append(dato)
    

def mostrar(matriz,dimension):
    for x in range(dimension[0]): #dimensión[0] es nro de filas
        print(matriz[x], end='\n')
            



cargado=False #para saber si la matriz se cargó
while True:
    opcion=menu()
    if opcion=='1':
        matriz=[]# ver que pasa si se pone esta línea antes de línea 46, fuera del while
        dimensiones=dimension() # la función regresa un lista con nro de filas y columnas
        carga (matriz, dimensiones)
        cargado=True
    elif opcion=='2'and cargado:
        print("Ud. cargó la matriz con los siguientes elementos:")
        mostrar(matriz, dimensiones)
    elif opcion=='2'and not cargado:
        print("Ud. no cargó la matriz no hay nada que mostrar.")
    elif opcion=='F'or opcion=='f':
        print("Finalizando..")
        break
    #else: NO es necesario, ya que menú asegura las opciones de retorno.
