#Funcion que calcula el factorial SIN recursividad!!
def factorial(num):
    if num==0:
        return 1 
    else:
        resultado = num
        for i in range(num-1,1,-1): #interpretar los argumentos de range!
            resultado = resultado * i
        return resultado

#Funcion que valia el ingreso
def valida():
    while True:
        try:
            x=int(input("Ingrese entero positivo:"))
            if x>=0:
                return x
            else:
                print( "El número debe ser igual o mayor que cero. Reingrese")
        except ValueError:
            print("Error en tipo de dato ingresado.")

#Función principal
x=valida()
print("El factorial de {} es: {}.".format(x,factorial(x)))
