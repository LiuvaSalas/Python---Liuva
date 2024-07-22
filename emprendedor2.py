#Librerias
import math

#Actividad 2 - Rentabilidad - Usuario normal
#Solicitamos al usuario los datos a ingresar

#Presentacion
print("Bienvenido(a) \n> Calculadora para las utilidades de un proyecto para 'Usuarios Normales'")
#P~Precio de Suscripción Base
P = float(input("Ingrese el precio de suscripción:\n>"))

#UN~Número de Usuarios normales
UN = float(input("Ingrese el número de usuarios normales:\n>"))

#UP~Número de Usuarios Premium
UP = float(input("Ingrese el número de usuarios premium:\n>"))

#GT~Gastos Totales
GT = float(input("Ingrese los gastos totales:\n>"))

#PA~Precio de suscripcion aumentado en un 50%
PA = P * 0.5


#Operacion
utilidades = ((P * UN) + ((P + PA) * UP)) - GT

#Resultados
print(f"Las utilidades serian de: {round(utilidades, 2)}")