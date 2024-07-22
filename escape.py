#Librerias
import math
from math import sqrt

#Actividad 1 - Velocidad de escape
#Solicitamos al usuario los datos a ingresar

#Presentacion
print("Bienvenido(a) \n> Calculadora para definir la Velocidad de Escape de un planeta")
#g~Constante gravitacional en m/s^2
g = float(input("Ingrese la constante gravitacional:\n>"))
#r~radio del planeta en [m]
r = float(input("Ingrese el radio en Kilómetros del planeta:\n>"))

#Operacion
V = sqrt(2 * g * r)

#Resultados
print(f"La velocidad de escape es: {round(V, 1)} [m/s]")