
# Dependiencias iniciales
from funciones import *

import pandas as pd
import numpy as np

import os

import scipy 
from scipy import stats
import datetime as dt
from datetime import timedelta  

# para tratar de poner espanol
from datetime import date, datetime, time
from babel.dates import format_date, format_datetime, format_time, format_timedelta, Locale
import locale                                    # para tratar de poner espanol
locale.setlocale(locale.LC_ALL,'es_CL.utf8')  



# Funciones para el programa
import funciones

import logging
logging.basicConfig(filename='example.log',level=logging.DEBUG)

print('Inicio')

#########################################################
#########################################################
# Listo archivos y los asigno a un dict según sus nombres

print('Lector de archivos')

exec(open(
	'./01_lectorBDs.py'
	).read())

for i, a in enumerate(archivos):
    print (a)

print(pd.DataFrame.from_dict(laboratorios, orient='index'))


#########################################################
#########################################################
# Creo un dict vacío y comienzo a agregar a los
# distintos laboratorios

print('Creador de laboratorios')

Laboratorios_dict = {}

##########
##########  Barnafi
##########
current = 'Barnafi'
archivo = './lab_barnafi.py'

print(str('x'*20), '\n', current,   'inicio', '\n', str('x'*20))
exec(open(archivo).read())
print(str('x'*20), '\n', current,   'fin', '\n', str('x'*20))


##########
##########  Integramedica
##########
current = 'Integramedica'
archivo = './lab_integramedica.py'


print(str('x'*20), '\n', current,   'inicio', '\n', str('x'*20))
exec(open(archivo).read())
print(str('x'*20), '\n', current,   'fin', '\n', str('x'*20))

##########
##########  PUCVmolecular
##########
current = 'PUCVmolecular'
archivo = './lab_PUCVmolecular.py'


print(str('x'*20), '\n', current,   'inicio', '\n', str('x'*20))
exec(open(archivo).read())
print(str('x'*20), '\n', current,   'fin', '\n', str('x'*20))



exit()


##########
##########  XXXXXXXXXXXXXXX
##########

exec(open(
	'./.py'
	).read())


##########
##########  XXXXXXXXXXXXXXX
##########

exec(open(
	'./.py'
	).read())
