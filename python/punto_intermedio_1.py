

#Finción que calcula el punto intermedio
def intermedio(a, b):
    return (a + b) / 2


#Funcion que valia el ingreso
def valida():
    while True:
        try:
            x=float(input(":"))
            return x
        except ValueError:
            print("Error en tipo de dato ingresado.")


#Función que busca la ubicación de x en el segmento
def posicion(x, minimo, maximo):
    if x < minimo:
        return "debajo"
    elif x > maximo:
        return "encima"
    return "dentro"

#Funcion que se asegura de tener un segmento [A,B]
def ingresos():
    while True:
        extremos=[]
        print("Ingrese A de [A,B]:")
        a=valida()
        print("Ingrese B de [A,B]:")
        b=valida()
        if b==a:
            print("Los extremos A y B de un intervalo no pueden ser los mismos.")
            print("Reingrese los valores")
        elif a>b:
            print("Intercambiando los extremos para que A < B")
            a,b=b,a
            extremos.append(a)
            extremos.append(b)
            print(extremos)
            return extremos
        else:
            extremos.append(a)
            extremos.append(b)
            print(extremos)
            return extremos

#Función principal
intervalo=[]
intervalo=ingresos()
print(intervalo)
print("Ingrese el valor para ver su ubicación respecto del intevalo:")
x=valida()
print("En número ingresado {} es encuentra {} del segmento [{},{}]".format(x,posicion(x, intervalo[0],intervalo[1]),intervalo[0],intervalo[1]))
