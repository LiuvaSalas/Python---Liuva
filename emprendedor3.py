#Librerias
import math

#Actividad 2 - Rentabilidad - Version 3
#Solicitamos al usuario los datos a ingresar

#Presentacion
print("Bienvenido(a) \n> Calculadora para las utilidades de un proyecto")
#P~Precio de Suscripción Base
P = float(input("Ingrese el precio de suscripción:\n>"))

#UN~Número de Usuarios normales
UN = float(input("Ingrese el número de usuarios normales:\n>"))

#GT~Gastos Totales
GT = float(input("Ingrese los gastos totales:\n>"))

#UA Utilidades correspondientes al año anterior.
UA = float(input(f"Ingrese las utilidades correspondientes al año anterior:\n>"))

#Operacion
utilidades = (P * UN - GT)

razon = utilidades / UA

#Resultados
print(f"Las utilidades de este año serian de: {round(utilidades, 2)}")
print(f"La razon entre las utilidades de este año y las del año anterior son de: {round(razon, 2)}")