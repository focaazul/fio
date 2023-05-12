#Funcion que se asegura de tener un segmento [A,B]
def ingresos():
    while True:
        print("Ingrese A de [A,B]:")
        A=valida()
        print("Ingrese B de [A,B]:")
        B=valida()
        if A==B:
            print("Los extremos A y B de un intervalo no pueden ser los mismos.")
            print("Reingrese los valores")
        elif A>B:
            print("Intercambiando los extremos para que A < B")
            A,b=B,A
            return A,B
        else:
            return A,B
        

    
def valida():
    while True:
        try:
            x=float(input("-> "))
            return x
        except ValueError:
            print("Error en tipo de dato ingresado.")

def numerosEntre(num1, num2):  
    num1=int(num1)
    num2=int(num2)
    for i in range(num1+1, num2):
        print(i)


#Función principal
A,B=ingresos()
numerosEntre(A,B)

