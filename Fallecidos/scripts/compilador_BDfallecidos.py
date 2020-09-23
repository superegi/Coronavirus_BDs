
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
for dirname, dirnames, filenames in os.walk('../BDs/'):
    for filename in filenames:
        lista_archivos.append(os.path.join(dirname, filename))
archivos = lista_archivos
print(archivos)
archivos

current = '../BDs/DEIS fallecidos 20200922 Chile.xlsx'
   
BD_deis = pd.read_excel(current,
                        dtype= str
                       )

def agregador_cero(valor):
    if pd.to_numeric(valor) <10:
        return str('0' + str(valor))
    else:
        return str(valor)

BD_deis.ANO2_NAC = BD_deis.ANO2_NAC.apply(agregador_cero)

# Nacimiento
dum= BD_deis.ANO1_NAC.apply(str) + BD_deis.ANO2_NAC.apply(str) + '-' + BD_deis.MES_NAC.apply(str)+'-'	+ BD_deis.DIA_NAC.apply(str)
BD_deis['TS_nacimiento'] = pd.to_datetime(dum, format='%Y-%m-%d', errors='coerce')
BD_deis['TS_nacimiento'].isna().value_counts()

# Muerte
dum=  BD_deis.ANO_DEF.apply(str) + '-' +BD_deis.MES_DEF.apply(str) + '-' +BD_deis.DIA_DEF.apply(str)
BD_deis['TS_muerte'] = pd.to_datetime(dum, format='%Y-%m-%d', errors='coerce')
BD_deis['TS_muerte']
print(BD_deis['TS_muerte'].isna().value_counts())

# Edad
BD_deis['Edad_dias'] =  BD_deis['TS_muerte'] - BD_deis['TS_nacimiento']
BD_deis['Edad'] = round((BD_deis.Edad_dias.dt.days / 365), 0)

from itertools import cycle

# RUT
def digito_verificador(rut):
    reversed_digits = map(int, reversed(str(rut)))
    factors = cycle(range(2, 8))
    s = sum(d * f for d, f in zip(reversed_digits, factors))
    if (-s) % 11 == 10:
        return 'K'
    else:
        return (-s) % 11

BD_deis['RUT'] = BD_deis.RUN.apply(lambda x : str(x) + '-' + str(digito_verificador(x)))

# Genero los nombres por separado
def nombre_nombre(x):
    res = x.split('/')
    return res[-1][:-1]

def nombre_apellido1(x):
    res = x.split('/')
    return res[0]

def nombre_apellido2(x):
    res = x.split('/')
    return res[1]

BD_deis['Nombre1'] = BD_deis.NOMBRE_LIMPIO.apply(nombre_nombre)
BD_deis['Apellido1'] = BD_deis.NOMBRE_LIMPIO.apply(nombre_apellido1)
BD_deis['Apellido2'] = BD_deis.NOMBRE_LIMPIO.apply(nombre_apellido2)
BD_deis['Nombre_full'] = BD_deis['Nombre1'] + ' ' \
+ BD_deis['Apellido1'] + ' ' + BD_deis['Apellido2']


# Sexo
BD_deis.SEXO.replace(
    {
    '1': 'Hombre',
    '2': 'Mujer',
    '9': np.nan},
    inplace=True
)

# Lugar de Muerte
BD_deis.LOCAL_DEF.value_counts()
BD_deis.LOCAL_DEF.replace(
    {
    '1': 'Hosp/Clinica',
    '2': 'Casa',
    '3': 'Otro',
    '9': np.nan},
    inplace=True
)
print(BD_deis.LOCAL_DEF.value_counts())

# Variable Coronavirus
columnas = BD_deis.columns
glosas = [s for s in columnas if "GLOSA" in s]
glosas

asepciones = ['covid', 'cavid', 'covi', 'covd',
              'civid', 'civd', 'navirus',
              'codiv',
              '19']

for cols in glosas:
    BD_deis[cols] = BD_deis[cols].str.strip()
    BD_deis[cols] = BD_deis[cols].apply(str)
    # Asigno los coronavirus según diagnóstico de muerte
    for palabra_clave in asepciones:
            BD_deis.loc[
                    BD_deis[cols].str.contains(palabra_clave, case=False),
                    'Covid'] = 'Coronavirus'
    
    # Asigno los coronavirus según otros crierios diagnosticos
    BD_deis.loc[
        (BD_deis[cols].str.contains('sars', case=False)),
         'Covid'] = 'Coronavirus'
    BD_deis.loc[
        (BD_deis[cols].str.contains('cov', case=False)) &
        (BD_deis[cols].str.contains('2', case=False)),
         'Covid'] = 'Coronavirus'
    BD_deis.loc[
        (BD_deis[cols].str.contains('c', case=False)) &
        (BD_deis[cols].str.contains('19', case=False)),
         'Covid'] = 'Coronavirus'


BD_deis.loc[BD_deis['Covid'].isnull()== True, 'Covid' ] = 'No'

BD_deis.Covid.value_counts()

# Exporto
muertos = BD_deis[['Nombre1', 'Apellido1', 'Apellido2', 'Nombre_full',
                   'RUT', 'SEXO',
                   'Edad', 'Edad_dias', 'TS_muerte', 'TS_nacimiento',
                   'LOCAL_DEF', 'DEF_DOM_CO', 'LUGAR_DEF',
                   'Covid',  'GLOSA1', 'GLOSA2', 'GLOSA3', 'GLOSA4',
                   'REG_RES',	'SERV_RES']].copy()
muertos.rename(columns = {
        'LOCAL_DEF':    'Tipo_lugar_muerte',
        'DEF_DOM_CO':   'Comuna_muerte',
        'LUGAR_DEF':    'Lugar_muerte',
        'REG_RES':      'RegionNum_muerte',
#        'REGION':       'Region_muerte',
        'SERV_RES':     'SS_muerte',
        'Nombre_completo': 'Nombre_full'        
        }, inplace=True )

muertos.to_pickle('../Muertos_DEIS.pkl')
muertos.to_excel('../Muertos_DEIS.xlsx')

# Finalizado
os.system('play -nq -t alsa synth 1 sine 440')

#grafico 
muertos.groupby([pd.Grouper(key='TS_muerte', freq='W'), 'Covid']).Nombre1.count().unstack().plot()
