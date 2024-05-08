""" Mostar el tipo de dato de cada valor del 
Diccionario"""

#Declaro diccionario.
diccio={1:"Hola","2":True,"Lista":["a","b","c"],"D":{"a":1,"b":2}}
#vemos que existen valores de distintos tipos
print("Las claves son:")
for t in diccio: #t asume los valores de las claves.abs
    print(t)
print("Veamos los tipos de los valores...")
#ahora mostramos el tipo de dato de cada valor.
for y in diccio: #t asume los valores de las claves.abs
    if isinstance(y,list):
        print("La clave:",y," es del tipo lista")
    elif isinstance(y,bool):
        print("La clave:",y," es del tipo booleano")
    elif isinstance(y,str):
        print("La clave:",y," es del tipo string")
    elif isinstance(y,dict):
        print("La clave:",y," es del tipo diccionario")
    else:
        print(f"La clave {y} es un tipo distinto de lista,diccionario,str o bool")
