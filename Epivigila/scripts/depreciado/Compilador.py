import pandas as pd
import numpy as np
from pandas_ods_reader import read_ods

import matplotlib.pyplot as plt
import matplotlib.dates as mdates
import matplotlib.cm as cm
import os

import scipy 
from scipy import stats
import datetime as dt

fecha_lectura = '20210215'
direccion = '../BDs/' + fecha_lectura + '_bases_por_region_PM'
direccion = '../BDs/Epi V - 20210215.xlsx'


print('Inicio lectura de archivos')
lista_archivos = []
for dirname, dirnames, filenames in os.walk(direccion):
    for filename in filenames:
        lista_archivos.append(os.path.join(dirname, filename))
archivos = lista_archivos
print(archivos)


archivos_regiones = [f for f in archivos if 'Región' in f]
print(archivos_regiones)

BD_regiones = pd.DataFrame()
for f in archivos_regiones:
    print (f)
    data = pd.read_csv(f,
                       sep = ';',
                       #encoding= 'latin',
                       encoding='utf-8-sig',
                       dayfirst=False,
                       dtype=str)
    print(data.shape)
    BD_regiones = BD_regiones.append(data)
    del data

BD_regiones.info()
print(BD_regiones.shape)

##limpio un poquito.....


valores_clinicos = ['gb_24', 'gb_48', 'porcentaje_neutrofilos_24',
 'porcentaje_neutrofilos_48',
 'porcentaje_linfocitos_24', 'porcentaje_linfocitos_48',
 'porcentaje_hematocrito_24', 'porcentaje_hematocrito_48',
 'hemoglobina_24', 'hemoglobina_48', 'plaquetas_24', 'plaquetas_48',
 'vsg_24', 'vsg_48', 'na_24', 'na_48', 'k_24', 'k_48', 'cl_24', 'cl_48',
 'glucosa_24', 'glucosa_48', 'urea_24', 'urea_48', 'creatinina_24',
 'creatinina_48', 'tgp_24', 'tgp_48', 'tgo_24', 'tgo_48', 'cpk_24',
 'cpk_48', 'ldh_24', 'ldh_48', 'ph_24', 'ph_48', 'pco2_24', 'pco2_48',
 'hco3_24', 'hco3_48', 'pao2_24', 'pao2_48', 'fio2_24', 'fio2_48',
 'ttpa_24', 'ttpa_48', 'tp_inr_24', 'tp_inr_48', 'fibrinogeno_24'
 ]

medicamentos = ['antivirales', 'tipos_antivirales',
	'fecha_inicio_antivirales', 'fecha_termino_antivirales',
	'antibioticos', 'tipos_antibioticos', 'fecha_inicio_antibioticos',
	'fecha_termino_antibioticos', 'esteroides', 'tipos_esteroides',
	'fecha_inicio_esteroides', 'fecha_termino_esteroides',
	'otros_medicamentos', 'tipos_otros_medicamentos',
	'fecha_inicio_otros_medicamentos',
	'fecha_termino_otros_medicamentos']

otros_drop = ['id_enfermedad_eno','enfermedad_notificada',
	'run_profesional', 'nombre_profesional', 'telefono_contacto_profesional',
	'email_contacto_profesional', 'consumo_tabaco', 'uso_vapeadores',
	'antecedente_viaje_internacional', 'uso_medicamentos_antipireticos',
	'fecha_inicio_toma_antipireticos',
	'uso_medicamentos_antibioticos', 'fecha_inicio_toma_antibioticos',
	 'uso_medicamentos_antivirales', 'fecha_inicio_toma_antivirales'
]



BD_regiones.drop(columns=valores_clinicos, inplace=True)
BD_regiones.drop(columns=medicamentos, inplace=True)
BD_regiones.drop(columns=otros_drop, inplace=True)
BD_regiones.set_index('id_formulario_eno', inplace =True)

####
####  RUT y nombre y sexo
####
BD_regiones['RUT'] =  BD_regiones['identificacion_paciente'].astype(str) + '-' + BD_regiones['dv']

BD_regiones['Nombre_full'] =  BD_regiones['nombres_paciente'] + ' ' + BD_regiones['primer_apellido_paciente'] + ' ' +  BD_regiones['segundo_apellido_paciente']

BD_regiones['sexo'].replace({	
	'hombre': 'Hombre',
	'mujer': 'Mujer'
	}, inplace = True)

####
####  Convierto a fecha
####
cols = BD_regiones.columns
cols_fechas = [ string for string in cols if  "fecha" in string]
print(cols)
print(cols_fechas)

for dates in cols_fechas:
	BD_regiones[dates] = pd.to_datetime(BD_regiones[dates],
										format = '%Y-%m-%d',
										errors='coerce')


epiV = BD_regiones[BD_regiones.region == 'Región de Valparaíso'].copy()
epiV = epiV[
        ['numero_folio', 'estado_caso','fecha_notificacion',
         'etapa_clinica', 'establecimiento_salud', 'region',
		'fecha_ingreso_sistema',
        
        'identificacion_paciente', 'RUT', 'Nombre_full', 'sexo',
        'edad', 'fecha_nacimiento', 'prevision',
        'region_residencia', 'comuna_residencia',

		'fecha_primeros_sintomas', 'motivo_examen', 'fecha_primera_consulta', 
		'fecha_ingreso_hospital', 'fecha_egreso_hospital',
        'dias_estadia', 'tipo_egreso',
        
        'fecha_toma_muestra_1', 'resultado_pcr_1', 'lugar_reposo'
        ]
        ]



print('Incio Limpieza MINSAL')

print('Guardo la BD')
print(BD_regiones.info())
BD_regiones.to_pickle('../Producto/BD_regionesSUCIO.pkl')

BD_regiones = BD_regiones.loc[~(BD_regiones.vigente_no_eliminado == 'FALSE')]
BD_regiones = BD_regiones.loc[~(BD_regiones.estado_caso == 'No validada')]

BD_regiones.to_pickle('../Producto/BD_regiones.pkl')
BD_regiones.sample(1000).to_excel('../BD_epivigilaSAMPLE.xlsx')

epiV.to_pickle('../Producto/epiV.pkl')
epiV.to_excel('../Producto/epiV.xlsx')

del epi
del epiV

veces = 5
for x in range(0,veces):
	os.system('play -nq -t alsa synth 0.1 sine 440')



