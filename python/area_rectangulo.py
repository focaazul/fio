def area_rectangulo(base, altura):
    return base*altura


#Funcion que valia el ingreso
def valida():
    while True:
        try:
            x=float(input("Ingrese el valor :"))
            if x>0:
                return x
            else:
                print("El valor ingresado no es válido.")
        except ValueError:
            print("Error en tipo de dato ingresado.")

#Funcion principal
altura=valida()
base=valida()
#Llamo a la función dentro del print
print("El rectangulo de {} por {} tiene un área de {}".format(altura,base, area_rectangulo(base,altura) ))
