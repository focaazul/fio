## FUNCIONES ##
def mostrar(matriz):
    # Recibe matriz y muestra por filas. No devuelve nada
    for fila in matriz:
        print(fila)
def media(matriz):
    acumulador = 0
    for x in matriz:
        for i in x:
            acumulador += i
    media = acumulador / (len(matriz) * len(matriz))
    return(media)
def buscaPositivo(matriz,reverse=False):
    positivos = 0
    negativos = 0
    for i in matriz:
        for j in i:
            if j > 0:
                positivos +=1                
            if j < 0:
                negativos +=1                
                
    if reverse == False and positivos != 0:
        return True
    if reverse == False and positivos == 0:
        return False
    if reverse == True and negativos != 0:
        return True
    if reverse == True and negativos == 0:
        return False
def buscaMayor(matriz, reverse=False):
    if reverse==False:
        maximos=[]
        for i in matriz:
            maximos.append(max(i))        
        maximo=max(maximos)
        return maximo
    else:
        minimos=[]
        for i in matriz:
            minimos.append(min(i))
        for j in minimos:
            minimo=min(minimos)
        return minimo
def mayoresQue(m,valor,reverse=False):
    c = 0
    for i in m:
        for j in i:
            if reverse==False:
                if j>valor:
                    c+=1
            if reverse==True:
                if j<valor:
                    c+=1
    return c    
## PROGRAMA PRINCIPAL ##
# Definición de la "matriz cuadrada" para la prueba de las funciones
matriz = [[1,2,3,4],
          [5,6,7,8],
          [9,2,3,4],
          [6,7,8,2]]
# matriz = [[-1,1,1,1],
#           [2,-2,2,2],
#           [3,3,-3,3],
#           [4,-4,4,4]]
# matriz = [[-1,-2,-3],
#           [-5,-6,-7],
#           [-9,-2,-8]]
print("-----------------INFORME:--------------")
print("La matriz es:")
mostrar(matriz)
print("La media de los valores de la matriz es: {}" .format(media(matriz)))
print("Existen {} valores Mayores que la media" .format(mayoresQue(matriz, media(matriz), reverse = False)))
print("Existen {} valores Menores que la media" .format(mayoresQue(matriz, media(matriz), reverse = True)))
if buscaPositivo(matriz, reverse = False):
    print("La Matriz tiene valores Positivos")
else:
    print("La Matriz no tiene Valores Positivos")
if buscaPositivo(matriz, reverse = True):
    print("La Matriz tiene valores Negativos")
else:
    print("La Matriz no tiene Valores Negativos")
print("El Mayor valor encontrado es: {}" .format(buscaMayor(matriz, reverse = False)))
print("El Menor valor encontrado es: {}" .format(buscaMayor(matriz, reverse = True)))
