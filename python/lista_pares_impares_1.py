def carga_lista(n):
    lista=[]
    for i in range(n):
        while True:
            try:
                x=float((input("-Ingrese un número a la lista en posición {}: ".format(i+1))))
                lista.append(x)
                break
            except ValueError:
                print("Error en tipo de dato ingresado.")
    return lista




def valida():
    while True:
        try:
            x=int(input("Ingrese cantidad de valores a carga en la lista:"))
            if x>0:
                return x
            else:
                print("El valor ingresado no es válido.")
        except ValueError:
            print("Error en tipo de dato ingresado.")


def separar(lista):
    lista.sort()# método ordenar lista
    pares = [] # creo una lista vacia
    impares = [] # creo una lista vacia
    for n in lista:
        if n%2 == 0:
            pares.append(n) #método append(), agrega elementos a la lista
        else:
            impares.append(n) #método append(), agrega elementos a la lista
    return pares, impares # ver que retorna 2 listas!


#Función Principal
numeros = [] #Lista vacia
numeros=carga_lista(valida()) #ver que como argumento de una función hay otra llamada a función
pares, impares = separar(numeros)
print("Números pares de la lista: ",pares)
print("Números impares de la lista:", impares)
