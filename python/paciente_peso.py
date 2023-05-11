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
            print ("Nombre conmenos  de {} kg: {}". format(peso,j))
    if (not band):
            print("No hubo personas con menos del peso ingresado")
    
def prom():
    suma=0
    for j in pacientes:
        suma+=pacientes[j]
    print ("El promedio de pesos es ", suma/len(pacientes))
    
      
N = int (input ("Ingrese cantidad de pacientes: "))
while N<0:
    N = int (input ("Error. Re Ingrese el valor cantidad de pacientes"))
pacientes= {}
for i in range(N):
    clave=input('Ingrese el nombre del paciente: ')
    peso=float(input('Ingrese el peso del paciente [0;250]: '))
    while peso < 0 or peso >250:
         peso=float(input('Error. ReIngrese el peso del paciente: '))
    pacientes[clave]=peso
print (pacientes)
opc=(input("Menu...\n1.- cantidad \n2.- hay  \n3.- Promedio \nF.- Fin"))
while opc!='F'and opc!='f':
    if (opc=='1'):
        a = float(input('Ingrese el peso A a buscar: '))
        c = ejer(a)
        print("la cantidad de valores que supera los {} kg es {}".format(a,c))
    elif (opc=='2'):
        X=float(input('Ingrese el peso X a buscar: '))
        fun2(X)
    elif (opc=='3'):
        prom()
    elif (opc=='F') or (opc=='f'):
        print ("chauuu")
    else:
        print ("error. opcion incorrecta")
    opc=(input("Menu...\n1.- cantidad \n2.- hay  \n3.- Promedio \nF.- Fin"))    
