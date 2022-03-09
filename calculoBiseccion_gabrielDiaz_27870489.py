
# UNIVERSIDAD DE ORIENTE - NUCLEO NVA. ESPARTA
# ESCUELA DE INGENIERIA Y CIENCIAS APLICADAS
# LIC. INFORMATICA
# CALCULO NUMERICO
# PROYECTO 1
# ALUMNO: GABRIEL DIAZ - 27870489

# Importamos sympy para podr implementar funciones con variables simbólicas
from sympy import *

# Importamos math para poder implementar funciones matematicas
from math import * 

# Funcion de ejemplo 
f = lambda x : (x**4) + (3*(x**3)) - 2 

# Funcion bic que aplica una sola iteracion de la biseccion

def bic(f,xa,xb):
  xr = (xa + xb) / 2                            # formula de biseccion
  fxr = f(xr)                                   # sustitumos x en la funcion con el valor obtenido
  fxa = f(xa)                                   # evaluamos la funcion en xa
  tvi = fxa * fxr                               # calculamos un valor tvi con la formula del terema del valor intermedio

  if tvi > 0:                                   # usamos tvi para acotar por arriba o por abajo a el conjunto de valores
    xa = xr
  else:
    xb = xr

  return [xa,xb,xr]

# Funcion biseccion que aplica bic en varias iteraciones hasta optener un margen de error aceptable
# Parametros
#   - f  = la funcion
#   - xa = valor minimo del dominio acotado
#   - xb = valor maximo del dominio acotado
#   - p  = minimo porcentual aceptable para el margen de error

def biseccion(f,xa,xb,p):
  print("Calculando el algoritmo de biseccion par la funcion dada")
  print("Con acotacion [", xa, ",", xb,"]")
  print("Con un margen de error del ", p, "%")
  i = 1
  print("Iteracion ", i, ":")
  print("xa =", xa)
  print("xb =", xb)
  erp = 100                                       # error relativo porcentual
  aux = bic(f,xa,xb)
  xa = aux[0]
  xb = aux[1]
  xr = aux[2]
  print("xr (actual) =", xr)
  print()

  while erp > p:
    i = i + 1
    print("Iteracion ", i, ":")
    xra = xr
    aux = bic(f,xa,xb)
    xa = aux[0]
    xb = aux[1]
    xr = aux[2]
    print("Valor actual =", xr)

    erp = abs(200 - abs((xr + xra) / xr * 100))    # error relativo porcentual
    print("error porcentual =", "{:.2f}".format(erp),"%")
    print()

  print("El valor ", xr, "es optimo con un margen de error de ", erp, "% para un minimo de ", p, "%")

biseccion(f,0,1,10)