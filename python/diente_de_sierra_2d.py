#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jun 14 14:59:37 2023

@author: daniel
"""

import matplotlib.pyplot as plt


def funcion(tipo, periodos):
    lista = []
    if tipo == "triangular":
        for i in range(periodos):
            lista += list(range(0,5,1))
            lista += list(range(3,0,-1))
        lista += [0]
    elif tipo == "sierra":
        for i in range(periodos):
            lista += list(range(0,5,1))
        lista += [0]
    elif tipo == "cuadrado":
        for i in range(periodos):
            lista += [1]*5
            lista += [0]*5
    return lista

    
lista = funcion("triangular",3)

plt.plot(lista, 'ko')
plt.plot(lista)
plt.show
