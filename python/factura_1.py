
# punto carga de facturas
def cargar(facturas):
    continua = "s"
    while continua=="s":
        nro = valida_nro(1,100000)
        importe = valida_importe()
        facturas[nro] = importe
        continua = input("Quiere cargar otra factura:[s/n]")


def valida_importe():
    while True:
            try:
                valor=float (input("Ingrese importe de factura: "))
                if 0<valor:
                    return valor
                else:
                    print("El monto de la factura no es válido.")
            except ValueError:
                print("Tipo de dato no valido. Reingrese.")
            


def valida_nro(min,max):#Valida Nro de Factura.
    while True:
        try:
            valor=int(input("Ingrese nro. factura, valor entre [{} ,{}]: ".format(min,max)))
            if min<=valor<=max:
                if valor not in facturas:
                    return valor
                else:
                    print("Nro de factura ya cargado. Ingrese otro.")
            else:
                print("El numero de factura no es valido")
        except ValueError:
            print("Tipo de dato no valido. Reingrese.")
        

#Muestra del dicionario
def mostrar(facturas):
    print("Listado de todos las facturas")
    for x in facturas:
        print(x, facturas[x])

#Muestra de facturas mayores a 1000

def imprimir_mayor(facturas):
    print("Listado de facturas con importes mayores a 1000")
    for nro in facturas:
        if facturas[nro]>1000:
            print(nro)

''' Busqueda de facturas por nro de factura'''
def buscar(facturas):
    while True:
            try:
                buscado=int(input("Ingrese nro de factura a buscar "))
                if 0<buscado:
                    if buscado in facturas:
                        print(" La factura se ha encontrado y el importe es {}".format(facturas[buscado]))
                        break
                    else:
                        print(" No se ha encontrado")
                else:
                    print("El valor ingresado no es válido.")
            except ValueError:
                print("Tipo de dato no valido. Reingrese.")
            
    
   

#Función principal
facturas = {}
fact=cargar(facturas)
mostrar(facturas)
imprimir_mayor(facturas)
buscar(facturas)
