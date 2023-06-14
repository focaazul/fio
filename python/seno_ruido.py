#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jun 12 15:43:14 2023

@author: daniel
"""

# Importamos el módulo para graficar
import matplotlib.pyplot as plt

# FUNCIONES
def media(lista):
    # Funcion para obtener el promedio de una lista de números
    return sum(lista)/len(lista)

def quitaCC(lista):
    # Función que recorre un lista y resta a cada elemento la media del conjunto
    promedio = media(lista)
    for i in range(len(lista)):
        lista[i] = lista[i] - promedio

def filtro(lista, orden):
    # Implementación de un filtro por media movil
    # Así como está, si el orden no es divisor de la cantidad de elementos,
    # Los últimos quedan sin filtrar
    for indice in range(len(lista)):
        if indice+orden < len(lista):
            acu = 0
            for i in range(orden):
                acu += lista[indice+i]
            promedio = acu/orden
            for i in range(orden):
                lista[indice+i] = promedio

# NOTA: ver que estas 2 últimas funciones no retornan nada, porque trabajamos
#       sobre la misma lista. Pasaje por referencia sería
        
# PROGRAMA
lista = [] # Lista utilizada para guardar los datos y procesarlos
# Se abre el archivo y se cargan en memoria los datos
with open("/home/daniel/Codigo/py/seno_ruido.txt", 'r') as archivo:
    for valor in archivo:
        lista.append(float(valor))
        

quitaCC(lista) # Quitamos la componente de continua de la señal

N = 10 # Orden para filtrar
filtro(lista, N) # Filtramos con un orden N

# Grafica
plt.plot(lista)
plt.xlabel("Muestras")
plt.ylabel("Amplitud")
plt.title("Gráfica del archivo 'seno_ruido.txt' filtrado. N={}".format(N))
plt.show()
