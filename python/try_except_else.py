
try:
    opcion=int(input("ingrese algo por teclado :"))
except:
    print("Ud. no ingreso un entero..")
else:#Se ejecuta SOLO si no hay excepcion!!
    print("Continúo con else del try") #solo ejecuto SI NO hay excepción


#SIEMPRE EJECUTO ESTA LINEA!!
print("Continuo fuera del try/except/else")