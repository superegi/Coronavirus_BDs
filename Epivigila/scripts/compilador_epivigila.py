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


class Importador_epivigila:
    
    def __init__(self):
        print('Inicio módulo de importación')
        
        # Archivos a leer
        self.archivos = []
        self.archivo_seleccionado = []
        
        self.BD = pd.DataFrame()

    def archivo_busca(self, direccion= None):
        # Me aseguro que la dirección esté definida
        if direccion:
            ruta = direccion
        else:
            ruta = '../BDs/'
        
        print('Inicio lectura de archivos')
        lista_archivos = []
        for dirname, dirnames, filenames in os.walk(ruta):
            for filename in filenames:
                lista_archivos.append(os.path.join(dirname, filename))
        self.archivos = lista_archivos
        print(self.archivos)
        print('\n')
        
    def archivo_selecciona(self, fecha=None, area=None, tipo=None):
        '''dentro del universo de los archivos encontrados
        selecciona a una submuestra definida por los argumentos
        FECHA, AREA y TIPO. 
        Devuelve una lista que idealmente es sólo un archivo'''
        
        files = self.archivos
        
        # elimino archivos temporales
        elimina = [f for f in files if '~lock' in f]
        if elimina:
            for x in elimina:
                print('eliminando:', x)
                files.remove(x)
        
        # las reglas de subset
        if fecha:
            files = [f for f in files if fecha in f]        
        if area:
            files = [f for f in files if area in f]
        if tipo:
            files = [f for f in files if tipo in f]
            
        print(files)
        self.archivo_seleccionado = files
        
    def archivo_carga(self, archivo= None):
        if archivo:
            file = archivo
        else:
            file = self.archivo_seleccionado[0]
        print(file)
        
        # me aseguro que tenga extension csv
        if any([e for e in [file] if 'csv' in e]):
            self.BD = pd.read_csv(file, sep = ';',
                           #encoding= 'latin',
                           #encoding='utf-8-sig',
                           dayfirst=False,
                           dtype=str)
        
class Compilador_epivigila:
    
    def __init__(self):
        print('Inicio módulo de compilación y limpieza')
        
        # Archivos a leer
        self.BD = pd.DataFrame()
    
    def cargadorBD(self, database):
        self.BD = database
        
    def limpieza1(self):
        
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
         'ttpa_24', 'ttpa_48', 'tp_inr_24', 'tp_inr_48', 'fibrinogeno_24']
        
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
        	 'uso_medicamentos_antivirales', 'fecha_inicio_toma_antivirales']

        self.BD.drop(columns=valores_clinicos, inplace=True)
        self.BD.drop(columns=medicamentos, inplace=True)
        self.BD.drop(columns=otros_drop, inplace=True)
        self.BD.set_index('id_formulario_eno', inplace =True)

    def limpieza2(self):
        ####
        ####  RUT y nombre y sexo
        ####
        self.BD['RUT'] =  self.BD['identificacion_paciente'].astype(str) + '-' + self.BD['dv']
        
        self.BD['Nombre_full'] =  self.BD['nombres_paciente'] + ' ' + self.BD['primer_apellido_paciente'] + ' ' +  self.BD['segundo_apellido_paciente']
        
        self.BD['sexo'].replace({	
        	'hombre': 'Hombre',
        	'mujer': 'Mujer'
        	}, inplace = True)

    
    def limpieza3(self):
        ####
        ####  Convierto a fecha
        ####
        cols = self.BD.columns
        cols_fechas = [ string for string in cols if  "fecha" in string]
        print(cols)
        print(cols_fechas)
        
        for dates in cols_fechas:
            	self.BD[dates] = pd.to_datetime(self.BD[dates],
            										format = '%Y-%m-%d',
            										errors='coerce')

    def guardo(self, nombre_pickle=None):
            
        interes = [
#                'id_formulario_eno',
                'numero_folio', 'estado_caso',
                'fecha_notificacion',
                 'etapa_clinica', 'establecimiento_salud', 'region', 'seremi',
                 'fecha_ingreso_sistema', 'tipo_caso_busqueda',
                 'lugar_busqueda_activa', 'vigente_no_eliminado',
                
                
                'identificacion_paciente', 'tipo_identificacion',
                'RUT', 'Nombre_full', 'sexo',
                'edad', 'estado_paciente', 'fecha_nacimiento', 'fecha_fallecimiento',
                'prevision', 'nacionalidad',
                'region_residencia', 'comuna_residencia',
                'via_residencia', 'direccion',	'numero_residencia',
                'dpto_residencia',	'poblacion_villa', 'telefono_celular',
                'trabajador_salud',


                'fecha_primeros_sintomas', 'motivo_examen',
                'fecha_primera_consulta', 'fecha_ingreso_hospital',
                'hospitalizacion', 
                'fecha_egreso_hospital', 'dias_estadia', 'tipo_egreso',
                'lugar_reposo',

                'fecha_toma_muestra_1', 'resultado_pcr_1','nombre_laboratorio_1'
                ]
        
        if nombre_pickle:
            nombre =  nombre_pickle
            self.BD[interes].to_pickle(nombre)
        else:
            print(self.BD.info())
            self.BD.to_pickle('../Producto/Epivigila_BRUTO.pkl')
            print('guardado: ../Producto/Epivigila_BRUTO.pkl')

            print('Incio Limpieza MINSAL')
            self.BD = self.BD.loc[~(self.BD.vigente_no_eliminado == 'FALSE')]
            self.BD = self.BD.loc[~(self.BD.estado_caso == 'No validada')]
            
            # Exporto columnas de interes 
            # genero PKL y XLSX
            self.BD[interes].to_pickle('../Producto/Epivigila_limpio.pkl')
            print('guardado: ../Producto/Epivigila_limpio.pkl')
            self.BD[interes].sample(3000).to_excel('../Producto/EpivigilaSAMPLE.xlsx')
            print('guardado: ../Producto/EpivigilaSAMPLE.xlsx')

        # Genero V región
        #self.BD[self.BD.region == 'Región de Valparaíso'][interes].to_pickle('../Producto/EpiV.pkl')
    
    def finalizo(self):
        veces = 5
        for x in range(0,veces):
            system('play -nq -t alsa synth 0.1 sine 440')


def main():
    load = Importador_epivigila()
    load.archivo_busca()
    load.archivo_selecciona(fecha='20210221', area='EpiV')
    load.archivo_carga()
    
    compila = Compilador_epivigila()
    compila.cargadorBD(load.BD)
    compila.limpieza1()
    compila.limpieza2()
    compila.limpieza3()
    compila.guardo()

    
if __name__ == "__main__":
    main()
