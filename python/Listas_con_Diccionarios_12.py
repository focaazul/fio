

alumnos=[]#Lista vacia que tendrá como valores Diccionarios
parcial={'nombre':'','nota':0}# parcial tiene las notas de los alumnos
#Notar que podemos tener varios alumnos con el mismo nombre y notas diferentes
#de cada parcial.abs
#------------------- main----------------------

while True:
    print("------------------------")
    print("1-Cargar nota de parcial")
    print("2-Mostrar alumnos/notas cargadas")
    print("S-Salir del programa")
    print("------------------------")
    print(" ")
    opc=input("Ingrese una opción: ").upper()
    if opc=='1':
        nombre_alumno=input("Ingrese  el nombre del alumno: ")
        while True:
            try:
                nota_alumno=float(input(f"Ingrese la nota de {nombre_alumno}: "))
                #la siguiente forma NO es recomendada!
                #nota_alumno=float(input(("Ingrese la nota de {}:".format(nombre_alumno))))
                if nota_alumno<0 or nota_alumno>10:
                    print("La nota ingresada no es válida, deber pertenecer [0,10]")
                else:
                    break#Este break me permite salir de la carga de notas
            except ValueError:
                print("Debe ingresar un valor numérico..")
        parcial={'nombre':nombre_alumno,'nota':nota_alumno}
        #print(parcial) #descomentar para verificar la carga.
        alumnos.append(parcial)#agrego el diccionario a la lista
    elif opc=='2':
        if len(alumnos)==0: #parcial tiene cargado algo?
            print("\n---->Nada que mostar.. no se cargó nada!!\n")
        else:
            print("Indice\tNombre\t\tNota")#Título de las columnas
            for i in alumnos:# cada i es un diccionario
                #print(i) #forma sencilla de mostar
                print(alumnos.index(i),"\t",i['nombre'],"\t",i['nota'])#con \t los dejo en columnas
    elif opc=='S':
        print("Finalizando el programa..")
        break #Con esto termino el while True
    else:
        print("La opción no valida, reingrese.")#El else DEBE estar para tomar
        #aquellas acciones que no sean consideradas en ningún if/elif!