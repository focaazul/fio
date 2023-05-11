def mostrar_menu():# Este menu solo muestra un texto, no valida ingreso, no reegresa nada
    print("Menu...")
    print("1-CARGA DE DATOS DE PACIENTES")
    print("2-MOSTRAR DATOS DE PACIENTE")
    print("F-FINALIZAR EL PROGRAMA")

def carga():#no recibe como arguemnto el diccionario por que es global.
    dni=int(input("Ingrese el DNI del paciente: "))
    edad=int(input("Ingrese la edad del paciente: "))
    altura=float(input("Ingrese la altura del paciente: "))
    pacientes[dni]=[edad,altura]#Se agrega clave:valor al dicciorio Global

def mostrar_paciente(ndni):
    encontrado=False
    for i in pacientes:
        if ndni==i:
            encontrado=True
            return(pacientes[i])
    if not encontrado:
        return([0,0])

#Función principal
pacientes={}# Diccionario Global

while True:
    mostrar_menu()
    op=input("Ingrese la opcion elegida...")
    
    if op=='1':
        carga()
    elif op=='2':
        numDNI=int(input("Ingrese el DNI del paciente a buscar: "))
        datos=mostrar_paciente(numDNI)
        if not datos==[0,0]:
            print("El paciente con DNI {} tiene {} años y mide {}m.".format(numDNI,datos[0],datos[1]))
        else:
            print("No se encontro al paciente...")
    elif op.upper()=='F':
        print("Finalizando...")
        break
    else:
        print("Opcion incorrecta, reingrese")

