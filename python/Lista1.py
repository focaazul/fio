lista=[] #Lista vacia

nro=int(input("Numero:")) #Ingreso un nro.

while nro!=0: #mientras no sea cero, voy a agregar valores a la lista.

    lista.append(nro) #agrego a la lista con método append

    nro=int(input("Número: ")) #Ingreso un nro y luego evalúa el while

print (lista) #muestro los valores de la lista.

nroeliminar=int(input("Ingrese Numero a eliminar: ")) #Ingreso nro a eliminar.

if nroeliminar in lista: #¿Existe ese nro en la lista?

    lista.remove(nroeliminar) #si existe => Borro!

else:

    print("Ese número no está entre los ingresados")

