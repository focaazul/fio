#-----------------------------SOLUCIÓN-------------------------------------#
#Función que muestra la matriz.
#------------------------------------------------------------------------------#
def mostrar():
    for i in MATRIZ:
        print(i)     
 
#Función que obtiene la transpuesta de la matriz.
#------------------------------------------------------------------------------# 
def transp():
    temp=[]
    for i in range(m):
        temp.append([])
        for j in range(n):
            temp[i].append(MATRIZ[j][i])
    for i in temp:
        print(i)
#Función que calcula el promedio de las filas.
#------------------------------------------------------------------------------#
def promedioF():
    print('El promedio de las FILAS es:')
    c = 0
    for i in MATRIZ:
        acc = 0
        for j in i:
            acc += j
        print('Fila {}: {:.2f}'.format(c,acc/m))
        c += 1
#Función que calcula el promedio de las columnas.
#------------------------------------------------------------------------------#    
def promedioC():
    print('El promedio de las COLUMNAS es:')
    for j in range(m):
        acc = 0
        for i in range(n):
            acc += MATRIZ[i][j]
        print('Columna {}: {:.2f}'.format(j,acc/n))
    
#Función que presenta los datos de la matriz ordenados de mayor a menor o viceversa
#según selección del usuario en una lista.
#------------------------------------------------------------------------------#
def ordenar(orden):
    tempLISTA = []
    for i in MATRIZ:
        tempLISTA = tempLISTA + i
    while True:
        cont = 0
        for i in range(len(tempLISTA)-1):
            if orden.lower() == 'a':
                if tempLISTA[i] > tempLISTA[i+1]:
                    tempLISTA[i] , tempLISTA[i+1] = tempLISTA[i+1] , tempLISTA[i]
                    cont += 1
            else:
                if tempLISTA[i] < tempLISTA[i+1]:
                    tempLISTA[i] , tempLISTA[i+1] = tempLISTA[i+1] , tempLISTA[i]
                    cont += 1                    
        if cont == 0:
            break                
    print(tempLISTA)
    #pass
def reempPrimos():
    for i in range(n):
        for j in range(m):
            temp = (i + j) + 2
            if temp > 1:
                for k in range(2 , temp+1):
                    if temp%k == 0 and k != temp:
                        break
                    elif k == temp:
                        MATRIZ[i][j] = -1
    for i in MATRIZ:
        print(i)
    
#Función que permite modificar todos los elementos de la matriz con restricciones
#para ciertas posiciones..
#------------------------------------------------------------------------------#
def modMatriz():
    for i in range(n):
        for j in range(m):
            if (i+j) % 2 == 0 and (i+j) != 0:
                while True:
                    z = input('Ingrese el nuevo valor del elemento [{}] [{}]: '.format(i,j))
                    z = verificaNUM(z)
                    if z != 'NaN':
                        if z < 10 or z > 15:
                            print('El número ingresado se encuentra fuera del rango admitido para el indice actual.\nVuelva a intentarlo.')
                        else:
                            break
            else:
                while True:
                    z = input('Ingrese el nuevo valor del elemento [{}] [{}]: '.format(i,j))
                    z = verificaNUM(z)
                    if z != 'NaN':
                        break
            MATRIZ[i][j] = z
#Función que verifica que lo que s eingresa por teclado sea númerico.
#------------------------------------------------------------------------------#
def verificaNUM(a):
    try:
        a = int(a)
        return a
    except ValueError:
        print('El valor ingresado no corresponde al tipo numerico.\nVuelva a intentarlo.')
        return 'NaN'                      
    
#-------------------------------PRINCIPAL-------------------------------------#
MATRIZ = [[4,5,6],[8,6,4],[7,1,9],[7,9,7]]
n = len(MATRIZ) #N° FILAS n=4
m = len(MATRIZ[0])#N° COLUMNAS m=3
op = ''
while op.lower() != 's':
        print('\t--------MENU-------\n\
    1 - Mostrar Matriz\n\
    2 - Obtener Transpuesta\n\
    3 - Promedio de FILAS\n\
    4 - Promedio de COLUMNAS\n\
    5 - Ordenar valores\n\
    6 - Reemplazar primos\n\
    7 - Modificar Matriz\n\
    s - SALIR')
        op = input('Seleccione una opción: ')
        if op.lower() == '1':
            mostrar()
        
        elif op.lower() == '2':
            transp()
        
        elif op.lower() == '3':
            promedioF()
        
        elif op.lower() == '4':
            promedioC()
        
        elif op.lower() == '5':
            a = ''
            while a != 'a' and a != 'd':
                a = input('¿Desea ordenar de forma Ascendente [A] o Descendente [D]?: ')
                if a != 'a' and a != 'd':
                    print('La opción ingresada es incorrecta. Vuelva a intentarlo.')
            ordenar(a)
        
        elif op.lower() == '6':
            reempPrimos()
        
        elif op.lower() == '7':
            modMatriz()
        
        elif op.lower() == 's':
            print('¡¡¡ADIOS!!!')
        
        else:
            print('Opción Invalida. Vuelva a intentarlo.')
