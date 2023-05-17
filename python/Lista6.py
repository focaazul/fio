lista=[]
num=int(input("Ingrese el total de elmentos: "))
mayor=0
menor=0
for x in range(num):
    n=int(input("Ingrese un valor entero: "))
    lista.append(n)
    if n>mayor:
        mayor=n
    if n<menor or menor==0:
        menor=n
lista.sort()
print(lista)
print("El numero mayor es ",mayor)
print("El numero menor es ",menor)

