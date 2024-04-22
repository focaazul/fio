lista=[{'nombre':'juan','edad':22}, {'nombre':'jorge','edad':30}]

print("Ahora accedemos a mostar a cada elemento ( diccionario) de la lista..")   
for i in lista:
    print(i) # esto muestra c/diccionario que está representado por i

print("Ahora usamos el indice de la lista para acceder a cada elemento ( diccionario)")   
for i in range(len(lista)):
    print(lista[i]) # esto muestra c/diccionario que está representado por i

print("Ahora mostrar como acceder a cada clave de cada lista")   
print(lista[0]['nombre'])
print(lista[0]['edad'])
print(lista[1]['nombre'])
print(lista[1]['edad'])

print("Ahora mostrar como acceder a cada clave de cada lista usando un for")  
for i in lista:
    print(i['nombre'], "tiene :", i['edad']) # i es un diccionario
#Para poder acceder de manera generica a las clave, podemos usar el método .key 
print("Ahora mostrar las claves del cada diccionario..")  
for i in lista:
    print("las claves del diccionario son :", i.keys()) # i es un diccionario
#Para poder acceder de manera generica a las clave, podemos usar el método .key 

#Esta opcion que se muestra continuación NO es recomendada!!!
# se recomienda usar la función enumerate en lugar de range, esto escapa al contenido de nuestra materia.
print("Ahora mostrar las claves del cada diccionario..")  
for i in range(len(lista)):
    print("las claves del diccionario son :", lista[i].keys()) # i es un diccionario
    
print("Ahora mostrar las claves del cada diccionario usando enumerate..") 
for i in lista:
    print(enumerate(i)) # i es un diccionario

print("Ahora mostrar las claves del cada diccionario ..")  
for i in lista:
    print("Lista: ", i)
    for j in i.keys():
        print("los valores de cada claves del diccionario son :", i,"tiene como clave: ", j, " y valen:", i.values()) # i es un diccionario

print("Ahora mostrar las claves del cada diccionario y sus valores..")  
for i in lista:
    print("Lista: ", i)
    for j in i: #j son las claves del diccionario de la cada lista
                #i representa cada lista
        print("La clave :-",j," tiene como valor: ", [j])
        #print("los valores de cada claves del diccionario: ", j.keys(), "y tiene como valor:", j.values()) # i es un diccionario