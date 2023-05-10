'''Consigna: Crear usando funciones una pila tipo FIFO que permita 
cargar, sacar y mostrar valores enteros de la misma.'''


def menu():
     while True:
        print("Menú: ") 
        print("1-Ingresar un elemento a FIFO")
        print("2-Sacar un elemento de FIFO")
        print("3-Mostrar pila FIFO")
        print("f o F -Finalizar el  programa...")
        opc=input("Ingrese su opción: ").lower()
        if opc=='1' or opc=='2' or opc=='3'or opc=='f'or opc=='F':
          return opc
        else:
            print("Opción no válida")

def pila(opcion):
    if opcion=='1':
        while True:
            try:
                fifo.append(int(input("Ingrese valor LIFO: ")))
                break
            except ValueError:
                print("Ingreso de tipo de dato erroneo..")
    elif opcion=='2' and len(fifo): #ver que si len(lifo)=0 no puedo sacar nada.
        fifo.pop(0)
    elif opcion=='3':
        print(fifo)
    

fifo=[] #esta pila FIFO es global por eso la puedo usar en función pila
while True:
        opc=menu()
        if opc=="1" or opc=='2' or opc=='3':
            pila(opc)
        else:
            print("Finalizando el programa...")
            break
