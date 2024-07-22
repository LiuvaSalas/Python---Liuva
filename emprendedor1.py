#Librerias
import math

#Actividad 2 - Rentabilidad - General
#Solicitamos al usuario los datos a ingresar

#Presentacion
print("Bienvenido(a) \n> Calculadora para las utilidades de un proyecto - Generico")
#P~Precio de Suscripción
P = float(input("Ingrese el precio de suscripción:\n>"))

#U~Número de Usuarios
U = float(input("Ingrese el número de usuarios:\n>"))

#GT~Gastos Totales
GT = float(input("Ingrese los gastos totales:\n>"))

#Operacion
utilidades = P * U - GT

#Resultados
print(f"Las utilidades serian de: {round(utilidades, 2)}")