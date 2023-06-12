import pandas as pd #Importamos la librería como pd
import matplotlib.pyplot as plt
try:
    df=pd.read_csv('/home/daniel/Codigo/py/evaluaciones.csv')#aoscio a un objeto file con el método read_csv
    print("En formato lindo, creado por panda sería: ")
    print("agregamos una columna mas para poner mas tarde el promedio de cada alumno...")
    df=df.assign(Promedio=0)#Creo una nueva columna en un nuevo objeto
except FileNotFoundError:
    print("No exise el archivo en el lugar indicado")
print("Calculo el promedio")
#creo una columna llamada Promedio y le calculo en promedio de la fila
df=df.assign(Promedio=df[["parcial1","parcial2","parcial3"]].mean(axis=1))
print(df)
#Mostramos los nombres y promedios de los alumnos.
#print(nuevo_file.iloc[:,[0,5]])
#Creamos una columna mas para la condición, por defecto ponemos libre.."
df=df.assign(Condicion="Libre")
#Reemplazamos "Libre" por "Regular" si el promedio es 6 o mas.
df.loc[df['Promedio']>=6, "Condicion"]="Regular"
#Grabamos el archivo nuevo como evaluaciones_nuevo.csv
df.to_csv('/home/daniel/Codigo/py/evaluaciones_nuevo.csv')
#Vamos a crear un grafico de torta con Libres / Regulares con matplitlib.pyplot
#Convierto el DataFrame a una lista.
sizes =df.to_numpy().transpose().tolist()
#Cuento la cantidad de regulares y de libres-
regulares=0
libres=0
for i in sizes[:][6]:#para cada fila miro la columna de condición
    if i=='Regular':
        regulares+=1
    else:
        libres+=1
sizes=[]#creo una lista con la cantidad de regulares y libres.
sizes.append(regulares)
sizes.append(libres)
labels='Regulares','Libres'#Creo unas etiquetas para el grafico
fig1, ax1=plt.subplots()
ax1.pie(sizes, shadow=True,labels=labels,  startangle=90)
ax1.axis('equal')
plt.show()
