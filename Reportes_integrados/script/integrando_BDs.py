import pandas as pd
import numpy as np
import datetime as dt
from datetime import timedelta  
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
import matplotlib.cm as cm
import os

# listo los archivos disponibles que he bajado
lista_archivos = []
for dirname, dirnames, filenames in os.walk('../BD_source/'):
    for filename in filenames:
        lista_archivos.append(os.path.join(dirname, filename))
archivos = lista_archivos
print(archivos)

###### Cargo BDs
######

   
deis = pd.read_pickle('../BD_source/muertos.bd')
ugcc_c19 = pd.read_pickle('../BD_source/ugcc.bd')
epiV = pd.read_pickle('../BD_source/epi.bd')


print('deis \n', deis.columns)
print('epiV \n', epiV.columns)
print('ugcc_c19 \n', ugcc_c19.columns)

deisSSVQ = deis.loc[(deis.SS_muerte== '7') & (deis.Covid=='Coronavirus')]
ugcc_c19X = ugcc_c19.loc[ugcc_c19['TIPO DE EGRESO'] == 'Fallecimiento'].copy()
epiVX = epiV.loc[epiV.tipo_egreso == 'fallecido'].copy()

print('deisSSVQ', deisSSVQ.shape)
print('ugcc_c19X', ugcc_c19X.shape)
print('epiVX', epiVX.shape)



print('\n')
print('deisSSVQ in epiVX')
print(deisSSVQ.RUT.isin(epiVX.RUT).value_counts())

DEIS_in_EPI = deisSSVQ.loc[
        (deisSSVQ.Nombre_full.isin(epiVX.Nombre_full)==False) | 
        (deisSSVQ.RUT.isin(epiVX.RUT)==False)].copy()
print(DEIS_in_EPI.shape)


print('\n')
print('deisSSVQ in ugcc_c19X')
print(deisSSVQ.RUT.isin(ugcc_c19X.RUT).value_counts())

DEIS_in_UGCC = deisSSVQ.loc[
        (deisSSVQ.Nombre_full.isin(ugcc_c19X.Nombre_full)==False) | 
        (deisSSVQ.RUT.isin(ugcc_c19X.RUT)==False)].copy()
print(DEIS_in_UGCC.shape)


############################################
print('\n')
print('ugcc_Covid19 en DEIS')
nombre  = (ugcc_c19X.Nombre_full.isin(deisSSVQ.Nombre_full)==True)
rut     = (ugcc_c19X.RUT.isin(deisSSVQ.RUT)==True)

UGCC_in_DEIS = ugcc_c19X.loc[
        ~(nombre | rut)
        ].copy()

print('ugcc_c19X', ugcc_c19X.shape)
print('UGCC_in_DEIS', UGCC_in_DEIS.shape)
UGCC_in_DEIS.to_excel('../Pacientes_perdidos/UGCC_in_DEIS.xls')

############################################
print('\n')
print('ugcc_Covid19 en Epivigila')
nombre  = (ugcc_c19X.Nombre_full.isin(epiVX.Nombre_full)==True)
rut     = (ugcc_c19X.RUT.isin(epiVX.RUT)==True)

UGCC_in_epiVX = ugcc_c19X.loc[
        ~(nombre | rut)
        ].copy()

print('ugcc_c19X', ugcc_c19X.shape)
print('UGCC_in_epiVX', UGCC_in_epiVX.shape)
UGCC_in_epiVX.to_excel('../Pacientes_perdidos/UGCC_in_epiVX.xls')

print('\n')
print('...................')

print(deisSSVQ.Tipo_lugar_muerte.value_counts())






























