"Cargar una lista de 5 elementos con valores reales y string"
#Aternativa 1
valores=[]
for i in range(5):
    dato=input("Ingrese dato: ")
    try:
        dato=float(dato) # si puede convierte string a float.
                        # si no puede por que es caracter, levanta una excepción
    except ValueError:
        pass
    valores.append(dato)
for j in valores:
    print(j,"-",type(j))

#Alternativa 2
valores1=[]
for i in range(5):
    dato=input("Ingrese dato: ")
    print("valor",dato.isalnum())
    if dato.isdecimal(): #si solo hay nrumeros 
        valores1.append(float(dato)) # convierte string a float.
    else:
        valores1.append(dato)
for j in valores1:
    print(j,"-",type(j))
