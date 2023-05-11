# Se deja al alumno corregir algunos puntos del programa.
# Cuestiones a considerar
#   Que faltaría para ir mejorando el programa?
#   Que pasa si se carga dos veces un día? 
#   Que pasa si se ingresan valores que no corresponden? letras en lugar de números.
#   Puedo parametrizar los valores de temperatura?
#   Que pasa si no cargue nada y ejecuto puntos 2,3,4?

datos={'Lunes':[],'Martes':[],'Miercoles':[],'Jueves':[],'Viernes':[]} #Diccionario Global
#Ver que las claves ya existen y los valores de cada clave son listas vacias.

#------------------------------------------------------------
def menu():
   while True:
     print('1) Cargar un día de la semana')
     print('2) Mostra temperaturas de un día')
     print('3) Mostrar todo los datos')
     print('4) Mostrar el día con mayor promedio')
     print('5) Salir-finalizar el programa')
     opc=input('Ingrese una opción válida: ')
     if not(opc=='1' or opc=='2'or opc=='3'or opc=='4'or opc=='5'):
         print('La opción ingresada no es válida.. reingrese..')
     else:
        return opc
#------------------------------------------------------------
def cargar(dia):
    for i in range(5):
        temp=float(input('Ingrese la temperatura: '))
        while not((temp>=-10 and temp<=10) or (temp>=20 and temp<=50)):
            print('Ud. ingresó un valor que no pertence al rango..reingrese..')
            temp=float(input('Ingrese la temperatura: '))
        datos[dia].append(temp)

#------------------------------------------------------------
def mostrar_dia(dia):
    dias_semana=['Lunes','Martes','Miercoles','Jueves','Viernes']
    print(datos[dias_semana[dia-1]])
    
#------------------------------------------------------------
def mostrar_todo(): 
    print('-------------Valores cargados------------------')
    for z in datos:
        print(datos[z])
    print('------------------------------------------------')

#------------------------------------------------------------
def mayor_promedio():
    promedio_maximo=0
    for i in datos:
        print('i vale',i)
        acumulador=0
        for x in range(5):
            acumulador=acumulador+datos[i][x]
        if promedio_maximo<(acumulador/5):
            dia=i
    return dia

# Código principal-------------------------------------------------
while True:
    opc=menu()
    if opc=='1':
        while True:
            dia=input('Ingrese un día de la semana: ')
            dia=dia.capitalize()
            if dia in datos:
                cargar(dia)
                break
            else:
                print('El día ingresado no es válido. Reingrese..')
        print(datos)
    elif opc=='2':
        while True:
            dia=int(input('Ingrese un día de la semana: '))
            if dia in range(1,6):
                mostrar_dia(dia)
                break
            else:
                print('El día ingresado no es válido. Reingrese..')
    elif opc=='3':
        print('tres')
    elif opc=='4':
        print(mayor_promedio())
    elif opc=='5':
        break
