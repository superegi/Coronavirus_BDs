# -*- coding: utf-8 -*-
"""
Editor de Spyder

Este es un archivo temporal.
"""

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




import pandas as pd
from itertools import cycle
import difflib as difflib
from fuzzywuzzy import fuzz  
from datetime import datetime
#from datetime import datetime

#from funciones_auxilares import pcolor

class Importador_BASEDATOS:
    
    def __init__(self):
        print('Inicio módulo de importación')
        
        print('Las funciones son:')
        print('archivo_busca')
        print('archivo_selecciona'  )            
        print('archivo_carga'  )
        
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
            
        if any([e for e in [file] if 'xlsx' in e]):
            self.BD = pd.read_excel(
                file)

            
class Cargador_dataset:
    
    def __init__(self):
        print('Inicio módulo de carga de dataset')
        print('Las funciones son:')
        print('cargador_laboratorio')
        print('cargador_epivigila'  )            
        print('cargador_epivigilaV'  )            
        print('cargador_epivigilaN'  )            
        print('cargador_seguimiento'  )            


        self.LabN = pd.DataFrame()
        
        self.EpiN = pd.DataFrame()
        self.Epi = pd.DataFrame()
        self.EpiV = pd.DataFrame()
        
        self.Seguimiento =  pd.DataFrame()
        
        self.bases_datos = list([
                self.LabN,
                self.Epi,
                self.EpiN,
                self.EpiV,
                self.Seguimiento
                ])
        
    def cargador_laboratorio(self, direccion= None):
        # Me aseguro que la dirección esté definida
        if direccion:
            ruta = direccion
        else:
            ruta = '../BD_source/LabNacional_diario.bd'
            
        self.LabN = pd.read_pickle(ruta)
        print('Cargado Labortorio nacional')
        
    def cargador_epivigila(self, direccion= None):
        # Me aseguro que la dirección esté definida
        if direccion:
            ruta = direccion
        else:
            ruta = '../BD_source/Epivigila.bd'
            
        self.Epi = pd.read_pickle(ruta)
        print('Cargado Epivigila')

    def cargador_epivigilaV(self, direccion= None):
        # Me aseguro que la dirección esté definida
        if direccion:
            ruta = direccion
        else:
            ruta = '../BD_source/Epivigila.bd'
            
        self.EpiV = pd.read_pickle(ruta)
        print('Cargado Epivigila V')
        
    def cargador_epivigilaN(self, direccion= None):
        # Me aseguro que la dirección esté definida
        if direccion:
            ruta = direccion
        else:
            ruta = '../BD_source/Epivigila.bd'
            
        self.EpiN = pd.read_pickle(ruta)
        print('Cargado Epivigila Nacional')
        
    def cargador_seguimiento(self, direccion= None):
        # Me aseguro que la dirección esté definida
        if direccion:
            ruta = direccion
        else:
            ruta = '../BD_source/Epivigila.bd'
            
        self.Seguimiento = pd.read_pickle(ruta)
        print('Cargado Seguimiento')

    def descriptor_cargas(self):
        print('EpiV:')
        print(self.EpiV.shape)
        print('̣\n')
    
        print('EpiN:')
        print(self.EpiN.shape)
        print('̣\n')

        print('Epi:')
        print(self.Epi.shape)
        print('̣\n')

        print('Seguimiento:')
        print(self.Seguimiento.shape)
        print('̣\n')

        print('LabN:')
        print(self.LabN.shape)
        print('̣\n')
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            