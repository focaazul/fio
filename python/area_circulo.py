import math #importo math para usar valor de pi.

#Función que calcula el área.
def area_circulo(radio):
    return (radio**2) * math.pi

#Funcion que valia el ingreso de radio.
def radio():
    while True:
        try:
            x=float(input("Ingrese el radio:"))
            if x>0:
                return x
            else:
                print("El radio ingresado no es válido.")
        except ValueError:
            print("Error en tipo de dato ingresado.")



#Función main.
r=radio()
print("El area de un círculo de radio {} es : {}".format(r,area_circulo(r)))
