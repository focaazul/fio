lista=[]
cont=0
suma=0
promedio=0
nro=float(input("Numero: "))
while nro!=0:
    lista.append(nro)
    cont=cont+1
    nro=int(input("Numero: "))
print (lista)
for n in lista:
    suma+=n
promedio=suma/cont
print("El promedio es", promedio)

 
