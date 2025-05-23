print("Bienvenido a la calculadora. Puede sumar, restar, multiplicar y dividir.")
print("Escriba 'salir' como operación para finalizar.\n")

activo = True  #<---Bandera !!

while activo: #<---Bandera !!
    operacion = input("Ingrese la operación (sumar, restar, multiplicar, dividir, salir): ").lower()
    
    if operacion == "salir":
        activo = False  #<---Bandera !!
        print("Gracias por usar la calculadora.")
    
    elif operacion in ["sumar", "restar", "multiplicar", "dividir"]:
        try:
            a = float(input("Ingrese el primer número: "))
            b = float(input("Ingrese el segundo número: "))
        except ValueError:
            print("Por favor ingrese números válidos.\n")
        else:   
            if operacion == "sumar":
                resultado = a + b
            elif operacion == "restar":
                resultado = a - b
            elif operacion == "multiplicar":
                resultado = a * b
            elif operacion == "dividir":
                if b != 0:
                    resultado = a / b
                else:
                    print("Error: no se puede dividir por cero.")
                    continue  # vuelve al inicio del while
            print(f"Resultado: {resultado}\n")
    else:
        print("Operación no reconocida. Intente nuevamente.\n")
