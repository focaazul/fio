# -*- coding: utf-8 -*-
"""
Created on Fri Apr 10/2020

Este código fue hecho en época de cuarentena por el COVID-19

Se muestra la utilización de Python para realizar un ejercicio de fisica 1 sobre
tiro parabólico. Se asume que el lector conoce los conceptos físicos básicos
sobre el tema.

@author: Eduardo S. Diaz
"""
import numpy as np
import math as mt
import matplotlib.pyplot as plt

print("Se verá un ejemplo de tiro parabolico, donde se hallaran los diferentes parametros caracteristicos del mismo.","\n")
print("Para comenzar, necesitamos que se ingresen algunos datos.")
#----------------------------------TOMA DE DATOS--------------------------------
#Datos iniciales, necesitamos la gravedad, altura, angulo y velocidad inicial
g=9.8 #gravedad en [m/s]
h=float(input("Ingrese la altura desde donde será lanzada el objeto en [m]:"))
ang=float(input("Ingrese el angulo con el cual sera lanzado el objeto (en grados):"))
alpha=(ang*mt.pi)/180 #pasamos los grados a radianes 
v0=float(input("Ingrese la velocidad inicial del objeto (modulo) en [m/s]:"))


#------------------------------------CALCULOS-----------------------------------
#Componentes de la velocidad inicial en ejes X e Y
v0_x=v0*mt.cos(alpha)
v0_y=v0*mt.sin(alpha)

"""
De la expresion que rige el movimiento en y(t) despejamos el tiempo, para hallar
el tiempo que tardara en llegar al suelo. Notar que se tiene dos soluciones posibles,
verificar cuál es la correcta.
"""

t_final1=(v0_y-(mt.sqrt((v0_y**2)+2*g*h)))/g #solución 1
t_final2=(v0_y+(mt.sqrt((v0_y**2)+2*g*h)))/g #solución 2

"""
Hallamos la distancia recorrida en x(t) para el tiempo final
"""
x_final=v0_x*t_final2
"""
Hallamos 't' para el cual se produce la altura máxima, con Vy(t)=0. Con este calculamos
la altura máxima (y_max) y la distancia que lleva recorrida hasta ese punto (x_ymax)
"""
t_hmax=v0*mt.sin(alpha)/g        #[s]
y_max=h+v0_y*t_hmax-(0.5)*g*t_hmax**2 #[m]
x_ymax=v0_x*t_hmax               #[m]

"""
Definimos t dándole un rango de valores, con estos podremos graficar el ejercicio
"""
t1=float(input("Ingrese el tiempo inicial t1 para realizar la grafica:"))
t2=float(input("Ahora ingrese el tiempo final t2:"))
p=float(input("Ingrese el incremento que tomará la variable t entre t1 y t2:"))
#se puede modificar el paso que toma el vector modificando el valor 0.01
t=np.arange(t1,t2,p)

vx=v0_x
vy=v0_y-g*t

"""
Se calculan los vectores de X e Y para todos los valores de tiempo que se formaron
en el vector t
"""
x=vx*t
y=h+v0_y*t-(0.5)*g*t**2
#---------------------------------MUESTRA DE RESULTADOS-------------------------
print("La maxima distancia recorrita en X por el proyectil es:",x_final,"[m]")
print("El tiempo que le llevo al proyectil recorrer esta distancia es de:",t_final2,"[s]")
print("La altura maxima del proyectil fue de:",y_max,"[m]",", le tomo ",t_hmax,"[s]","y recorrio",x_ymax,"[m] al llegar a esa altura",)

#Coordenadas del punto de maxima altura 
px_ymax=x_ymax
py_max=y_max

#Coordenadas del punto de maxima distancia recorrida
px_final=x_final
py_xmax=0

#Grafico todo
plt.ion()
plt.plot(x,y,px_final,py_xmax,'ro',px_ymax,py_max,'bo')

#Con esto agrego las flechas y anotaciones en la gráfica
plt.annotate("Altura maxima",
         xy=(px_ymax, py_max),
         xycoords='data',
         xytext=(px_ymax, py_max-3),
         fontsize=9,
         arrowprops=dict(arrowstyle="->",
         connectionstyle="arc3,rad=.2"))

plt.annotate("Distancia maxima",
         xy=(px_final, py_xmax),
         xycoords='data',
         xytext=(px_final, py_xmax+3),
         fontsize=9,
         arrowprops=dict(arrowstyle="->",
         connectionstyle="arc3,rad=.2"))

#Pongo títulos a los ejes y guardo la imagen
plt.xlabel("Distancia en [X]")
plt.ylabel("Distancia en [Y]")
plt.title("Tiro parabólico")
plt.savefig("tiro_parabolico.png")
plt.grid()
# plt.show()
input()
