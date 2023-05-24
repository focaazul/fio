"Cargar una lista de 5 elementos con valores reales y string"
#Aternativa 1 , usando try/except
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
    print(j,"-",type(j))#para mostrar valores y tipos cargados en la lista

#Alternativa 2 , usando un método de string, llamado isdecimal()
valores1=[]
for i in range(5):
    dato=input("Ingrese dato: ")
    if dato.isdecimal(): #si solo hay numeros esto es True
        valores1.append(float(dato)) # convierte string a float.
    else:
        valores1.append(dato)
for j in valores1:
    print(j,"-",type(j))#para mostrar valores y tipos cargados en la lista
