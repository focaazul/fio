print("Bienvenido a la calculadora. Puede sumar, multiplicar y dividir.")

#ver que la línea 4 NO tiene posibilidad de excepción!!!
operacion = input("Ingrese la operación (sumar, multiplicar, dividir, salir): ").lower()
if operacion == "salir":
    print("Gracias por usar la calculadora.")
elif operacion=="sumar" or operacion=="multiplicar" or operacion=="dividir":
     try:
         #ver que las líneas 10 y 11 TIENEN posibilidad causar excepción!!
         a = float(input("Ingrese el primer número: "))
         b = float(input("Ingrese el segundo número: "))
     except ValueError:
         print("Por favor ingrese números solamente.\n")
     else:#Si no hay excepción hago todo lo del else del try !!
         if operacion == "sumar":
             resultado = a + b
             print("Resultado:",resultado)
         elif operacion == "restar":
             resultado = a - b
             print("Resultado:",resultado)
         elif operacion == "multiplicar":
             resultado = a * b
             print("Resultado:",resultado)
         elif operacion == "dividir":
             if b != 0: #Ver que si no analizo esto PODRÍA existir excepción
                 resultado = a / b
                 print("Resultado:",resultado)
             else:
                 print("Error: no se puede dividir por cero.")       
else:
     print("Operación no reconocida. Finalizando...")
