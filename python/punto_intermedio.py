
#Finción que calcula el punto intermedio
def intermedio(a, b):
    return (a + b) / 2


#Funcion que valida el ingreso
def valida():
    while True:
        try:
            x=float(input(":"))
            if x>0:
                return x
            else:
                print("El valor ingresado no es válido.")
        except ValueError:
            print("Error en tipo de dato ingresado.")

#Función principal

while True:
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
        break
    else:
        break

print("El punto intermedio entre {} y {} es {}.".format(a,b,intermedio(a,b) ))

# Se deja como tarea para el alumno, crear una función que valide el intervalo [A,B]
