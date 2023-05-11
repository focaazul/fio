def menu():
    while True:
        print("----------------------------------")
        print('1-Cantidad de personas con un peso')
        print('2-Hay personas con menos pesos')
        print('3-Promedio  de pesos')
        print('f o F-Finaliza el programa')
        print("----------------------------------")
        opc=input('Ingrese opcion: ')
        if not(opc=='1' or opc=='2' or opc=='3'or opc=='f' or opc=='F'):
            print('opcion no válida.. reingrese')
        else:
            return opc # regresa 1,2,3,f o F


def ejer (peso):
    cont=0
    for j in pacientes:
        if (pacientes[j]>=peso):
            cont+=1
    return (cont)

def fun2 (peso):
    band = False
    for j in pacientes:
        if (pacientes[j]<=peso):
            band=True
            print ("El paciente con menos de {} kg: {}". format(peso,j))
    if (not band):
            print("No hubo personas con menos del peso ingresado")
    
def prom():
    suma=0
    for j in pacientes:
        suma+=pacientes[j]
    print ("El promedio de pesos es ", suma/len(pacientes))
while True:
    try:       
        N = int (input ("Ingrese cantidad de pacientes: "))
        if N<0:
            print("Error. Re Ingrese el valor cantidad de pacientes")
        else:
            break
    except ValueError:
        print("Error en tipo de ingreso...")


#Función Principal
pacientes= {}
#---------Carga del Diccionario------------
#Solo se carga un vez al incio del script
for i in range(N):
    clave=input('Ingrese el nombre del paciente: ')
    while True:
        try:
            peso=float(input('Ingrese el peso del paciente [0;250]: '))
            if peso < 0 or peso >250:
                print('Error. Reingrese el peso del paciente: ')
            else:
                pacientes[clave]=peso
                break
        except ValueError:
            print("Error en tipo de dato. ")
        
print("Ud. cargó los siguientes pacientes: ")
print (pacientes)
while True:
    opc=menu()
    if (opc=='1'):
        a = float(input('Ingrese el peso a buscar: '))
        c = ejer(a)
        print("la cantidad de personas con {} kg o mas es {}".format(a,c))
    elif (opc=='2'):
        X=float(input('Ingrese el peso a buscar en los pacientes: '))
        fun2(X)
    elif (opc=='3'):
        prom()
    elif (opc=='F') or (opc=='f'):
        print ("Finalizando")
        break
    else:
        print ("Error. Opcion incorrecta")
    
