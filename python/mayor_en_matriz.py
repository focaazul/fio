"""
Realizar un programa en Python que:
1) Invoque a una funcion menú que SOLO regresa una opcion válida del menu.
2) Que permita invocar a la función carga, que carga una matriz humedad de dimensiones N x M con N y M definidas como constantes
3) Que permita invocar a la funcion mayor el mayor valor de la humedad y su ubicación
4) Que presente una opción para finalizar el programa.
Los valores permitidos para carga en la matriz humedad son [0;100]
"""


#Funcion que valida ingresos, regresa opcion válida solo 1,2,3
def menu():
    while True:
        print('1-Cargar')
        print('2-Buscar Mayor')
        print('3-Salir')
        opc=input('Ingrese opcion: ')
        if not(opc=='1' or opc=='2' or opc=='3'):
            print('opcion no válida.. reingrese')
        else:
            return opc # regresa 1,  2 o 3
#Funcion que carga matriz.
def carga(humedad):
    for x in range(N):#este for recorre CADA fila por lo tanto x va tomar valores 0  y N-1
        humedad.append(list())#lista que oficia de fila
        for y in range(M):
            while True:
                while True:
                    try:
                        ingreso=float(input('ingrese humedad: '))
                        break
                    except ValueError:
                        print("Tipo de dato no válido, reingrese.")
                if ingreso>=0 and ingreso<=100:
                    break
                else:
                    print('valor no valido para humedad [0;100].. reingrese')
            humedad[x].append(ingreso)# si es valido guardo.
    return(True)


#Funcion que busca y regresa  el mayor de la diagonal.
def mayor(humedad):
   #propongo un elemento de la matriz como mayor
    mayor_ubicacion=[humedad[0][0],0,0]
    #El algoritmo que sigue busca si hay algún elemento mayor ...
    for x in range(N):#este for recorre CADA fila por lo tanto x va tomar valores 0  y N-1
        for y in range(M):
            if humedad[x][y]>mayor_ubicacion[0]:
                mayor_ubicacion[0]=humedad[x][y]#cuando encuentro uno mas grande que mayor lo tomo como mayor.
                mayor_ubicacion[1]=x #guardo sus ubicaciones
                mayor_ubicacion[2]=y
    return(mayor_ubicacion) # Regreso un lista con el mayor valor y su ubicación

#Funcion main
N=2 #Defino dimensiones
M=3 #Defino dimensiones
humedad=[]#declaro una lista de nombre humedad.
valores=[]
cargada=False
while True:
    opc=menu()
    if opc=='1':
        print("vamos a cargar una matriz de: ",N," por ",M )
        cargada=carga(humedad)# si regresa True es por que se cargó.
        print("La matriz cargada es: ")
        for x in range(N): 
            print(humedad[x], end='\n')
    elif opc=='2' :
        if cargada:
           valores=mayor(humedad)
           print("El mayor valor es: {} y se encuentar en la fila {} columna {}".format(valores[0],valores[1]+1,valores[2]+1))
    elif opc=='3':
        print('saliendo')
        break



