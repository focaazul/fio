#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
@author: daniel
"""
try:
    a = float(input("Ingrese el primer número: "))
    b = float(input("Ingrese el segundo número: "))
except ValueError:
    print("Por favor ingrese números solamente.\n")
else:#Si no hay excepción hago todo lo del else del try !!
    resultado = a + b
    print("esta línea SOLO se ejecuta si NO hay excepciones")
    print("Resultado:",resultado)  
print("Esta línea SIMPRE se ejecuta!!!")
