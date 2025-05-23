#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
@author: daniel
"""
try:
    a = int(input("Ingrese un número  ENTERO: "))
except ValueError:
    print("Por favor ingrese número ENTERO solamente.\n")
else:#Si no hay excepción hago todo lo del else del try !!
    print("Ud. ingresó el número entero :", a)
print("Esta línea SIMPRE se ejecuta!!!") #por mas que haya excepcion se ejecuta!!
