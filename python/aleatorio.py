#importo solo el método randint de la  librería random
#Este método me permite crear números aleatorios entre dos valores pasados como argumento.
#Le cambio el nombre de randit a entero_aleatorio solo para hacerlo mas facil
from random import randint as entero_aleatorio

def generaNumeroAleatorio(minimo,maximo):
 
    try:
        if minimo > maximo:
            aux = minimo
            minimo = maximo
            maximo = aux
            #invoco el método (ranint entero aleatorio) de la librería random
        return entero_aleatorio(minimo, maximo) 
    except TypeError:
        print("Debes escribir numeros")
        return -1

#Funcion que valia el ingreso
def valida():
    while True:
        try:
            x=int(input(":"))
            return x
        except ValueError:
            print("Error en tipo de dato ingresado.")

#Función principal
N=10 # cantidad de números aleatorios.
print("Ingrese un argumento: ")
x=valida()
print("Ingrese otro argumento: ")
y=valida()
print(" Ahora mostaremos unos números aleatorios entre {} e {}".format(x,y))
i=0
while i<N:
    print(generaNumeroAleatorio(x,y),end=" ")
    i=i+1
print(end="\n")
