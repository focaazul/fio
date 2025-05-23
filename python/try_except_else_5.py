#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
@author: daniel
"""
a = input("Ingrese un número  Real: ")#ver que esta línea NO puede generar Excepción!!
b = input("Ingrese un número  Real: ")#ver que esta línea NO puede generar Excepción!!
#hasta aqui a y b son datos del tipo string!
try:
    a =float(a)#Esta línea puede generar excepción!
    b =float(b)#Esta línea puede generar excepción!
except ValueError:
    print("Por favor ingrese número solamente.\n")
else:# <--else del try!!
    if b!=0: 
        #Si no hay excepción a y b son ahora reales :-
        print("El cociente {}/{} es:{}".format(a,b,a/b))#Esta línea puede generar excepción!
    else:
        print("No se puede dividir por CERO!!")
#aqui temina try/except, pero el programa continúa!
print("Esta línea SIEMPRE se ejecuta !!!") #por mas que haya excepcion se ejecuta!!
