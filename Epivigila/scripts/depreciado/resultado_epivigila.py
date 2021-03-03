"""
Created on Tue Sep 22 22:05:43 2020

@author: egidio
"""

import pandas as pd
import numpy as np
import os

epi = pd.read_pickle('../Producto/BD_regiones.pkl')



datos_rutificado = [
        'etapa_clinica', 'estado_paciente',
        'RUT', 	'Nombre_full',
        'tipo_identificacion', 'identificacion_paciente',
        'nombres_paciente', 'primer_apellido_paciente',
        'segundo_apellido_paciente',  'edad'
        
        ]
        
# Exporto todos aquellos casos válidos como 'POSITIVOS'
epi.loc[
        (epi.etapa_clinica == 'CONFIRMADA') |
        (epi.etapa_clinica == 'SOSPECHA') |
        (epi.etapa_clinica == 'PROBABLE')         
        ][datos_rutificado].to_csv('../Producto/Rutificado_positivos.csv')


os.system('play -nq -t alsa synth 0.1 sine 440')