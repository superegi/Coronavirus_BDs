
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
#print(archivos)
archivos


archivo_BD = 'Descargar registros COVID-19 20200922.xlsx'
carpeta = '../BDs/Covid19/'
current = carpeta+archivo_BD
print(current)

BD_covid19_ugcc = pd.read_excel(current)
print(BD_covid19_ugcc.head())

res = BD_covid19_ugcc['TIPO DE EGRESO'].value_counts()
print(res)

####
####  Convierto a fecha
####
cols = BD_covid19_ugcc.columns
cols_fechas = [ string for string in cols if  "FECHA" in string]
print(cols)
print(cols_fechas)

for dates in cols_fechas:
	BD_covid19_ugcc[dates] = pd.to_datetime(BD_covid19_ugcc[dates], dayfirst=True)


####
####  RUT y nombre y sexo
####

BD_covid19_ugcc['RUT'] =  pd.to_numeric(BD_covid19_ugcc.RUN, errors='coerce').astype('Int32').astype(str)
BD_covid19_ugcc['RUT'] =  BD_covid19_ugcc['RUT'] + '-' + BD_covid19_ugcc['DV'].astype(str)

BD_covid19_ugcc['Nombre_full'] =  BD_covid19_ugcc['NOMBRES'] + ' ' + BD_covid19_ugcc['APELLIDO PATERNO'] + ' ' +  BD_covid19_ugcc['APELLIDO MATERNO']

BD_covid19_ugcc['SEXO'] = BD_covid19_ugcc['SEXO'].replace({	
	'M': 'Hombre',
	'F': 'Mujer'
	})


print(BD_covid19_ugcc.info())


#####
##### Selecciono y exporto
#####

ugcc_c19 = BD_covid19_ugcc[['ESTADO CASO', 'SSALUD COMUNA PACIENTE', 'TIPO ESTABLECIMIENTO','ESTABLECIMIENTO',
							'SERVICIOSALUD PRESTADOR',	'REGION PRESTADOR',
							
							'Nombre_full', 'SEXO', 'RUT', 'EDAD', 'REGION PACIENTE', 'COMUNA',
								'PREVISION', 'FECHA NACIMIENTO',
							'TIPO DE EGRESO', 'DIAS DE ESTADA',
							'FECHA CONFIRMACION', 'FECHA DE INGRESO', 'FECHA DE EGRESO', 
							'VM FECHA CONEXION', 'VMNI CONEXION']]
print(ugcc_c19.head())


ugcc_c19.to_pickle('../ugcc_c19.pkl')
ugcc_c19.to_excel('../ugcc_c19.xls')

# BD_covid19_ugcc.groupby([pd.Grouper(key='FECHA DE EGRESO', freq='D'), 'TIPO DE EGRESO']).Nombre_full.count()#.unstack().plot()
os.system('play -nq -t alsa synth 0.1 sine 440')
