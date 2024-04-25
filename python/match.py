opcion=input("Ingrese una opcion A, B, C, 1, 2, 3:")
match(opcion):
    case "A":
        print( " Ud ingreso A")
    case "B":
        print( " Ud ingreso B")
    case "1":
        print( " Ud ingreso 1")
    case "2":
        print( " Ud ingreso 2")
    case "3":
        print( " Ud ingreso 3")
    case _:# opcion que no hizo match.
        print( " Ud ingresó una opcion no listada..")