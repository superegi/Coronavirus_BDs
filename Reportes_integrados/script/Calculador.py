#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Sep 15 03:01:15 2020

@author: egidio
"""

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

   
deis = pd.read_pickle('../BD_source/Muertos_DEIS.pkl')
ugcc_c19 = pd.read_pickle('../BD_source/ugcc_c19.pkl')
epiV = pd.read_pickle('../BD_source/epiV.pkl')


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
print('Tipo Lugar de muerte',
      '\n')
print(deis.Tipo_lugar_muerte.value_counts())

print('\n')
print('Lugar más mortal',
      '\n')
print(ugcc_c19X.ESTABLECIMIENTO.value_counts())




result = ugcc_c19.groupby([  'TIPO DE EGRESO','ESTABLECIMIENTO'])['ESTADO CASO'].size()
res1 = result.groupby(level=1).apply(lambda x:
                                                 100 * x / float(x.sum()))

result.to_excel('./letalidad.xls')
print('\n')

with open('out.txt', 'w') as f:
    print(result, filename, file=f)  # Python 3.x
#print(
 #     pd.crosstab(ugcc_c19['ESTABLECIMIENTO'], ugcc_c19['TIPO DE EGRESO']).head()
  #    ) sort_values('mygroups', ascending=False)


ugcc_c19.loc[ugcc_c19['VM FECHA CONEXION'].isnull()==False]


























