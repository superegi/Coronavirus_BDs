
# Dependiencias iniciales
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
exec(open('./funciones.py').read())


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
incluyo_laboratorio(
    'Barnafi',
    './lab_barnafi.py')
# print(globals())

##########
##########  Integramedica
##########
incluyo_laboratorio(
    'Integramedica',
    './lab_integramedica.py')

##########
##########  PUCVmolecular
##########
incluyo_laboratorio(
    'PUCVmolecular',
    './lab_PUCVmolecular.py')

##########
##########  PUCVmolecular
##########
incluyo_laboratorio(
    'PUCVmolecular',
    './lab_PUCVacuicola.py')

##########
##########  Labocenter
##########
incluyo_laboratorio(
    'Labocenter',
    './lab_Labocenter.py')

##########
##########  UV
##########
incluyo_laboratorio(
    'UV',
    './lab_UV.py')

##########
##########  UV
##########
incluyo_laboratorio(
    'UV',
    './lab_UV.py')


exec(open(
	'./juntadorBD.py'
	).read())

BD.to_excel('./ex.xls')