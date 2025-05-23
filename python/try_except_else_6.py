#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
@author: daniel
"""

#Este codigo ESTA BIEN ,es como se debe hacer !!!!
try:
    a =float(input("Ingrese un número  Real: "))#ver que esta línea puede generar Excepción!!)
except ValueError:
    print("Por favor ingrese número solamente.\n")
else:
    print("Ud. ingresó:",a )
#aqui temina try/except, pero el programa continúa!
print("Esta línea SIEMPRE se ejecuta !!!") #por mas que haya excepcion se ejecuta!!



#Este codigo ESTA MAL ,es como NO se debe hacer !!!!!!!!
try:
    a =float(input("Ingrese un número  Real: "))#ver que esta línea puede generar Excepción!!)
except ValueError:
    print("Por favor ingrese número solamente.\n")
#aqui temina try/except, pero el programa continúa!
print("Ud. ingresó:",a )#si hay error de excepción esta línea se ejecuta y tira ERROR!!!
