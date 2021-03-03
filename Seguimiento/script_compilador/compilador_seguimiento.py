#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Feb 21 11:59:07 2021

@author: egidio
"""
import pandas as pd
import numpy as np
from pandas_ods_reader import read_ods
import os
import datetime as dt

class Compilador_seguimiento:
    
    
    def __init__(self):
        print('Inicio módulo de compilación y limpieza')
        print('Las funciones son:')
        print('cargadorBD')
        print('limpieza1')
        print('limpieza2')
        print('guardo')        
        
        self.BD = pd.DataFrame()
    
    def cargadorBD(self, database):
        self.BD = database
        
    def limpieza1(self):
        
        a = (self.BD.identificacion_paciente == 'RUN')
        
        RUT = self.BD[a].cont_n_identificacion.str.strip().str[:-1] \
        + '-'                                                       \
        + self.BD[a].cont_n_identificacion.str.strip().str[-1]
        
        self.BD.loc[a==True, 'RUT'] = RUT

        self.BD['Nombre_full'] = self.BD.nombre_paciente                    \
        + ' '                                                               \
        + self.BD.primer_apellido_paciente

    def limpieza2(self):
        ####
        ####  Convierto a fecha
        ####
        cols = self.BD.columns
        cols_fechas = [ string for string in cols if  "fecha" in string]
        cols_fechas.append('dia_contacto')
        print(cols)
        print(cols_fechas)
        
        for dates in cols_fechas:
            	self.BD[dates] = pd.to_datetime(self.BD[dates],
            										format = '%Y-%m-%d',
            										errors='coerce')

    
    def arreglo_folios(self):
        self.BD['FOLIO'] = self.BD.n_folio.str.rsplit('-').str[-1]
        self.BD['FOLIO_CONTACTO'] = self.BD.n_folio.str.rsplit('SC').str[1].str.split('-').str[0]

    def arreglo_BOOL(self):
        self.BD.loc[self.BD.contacto_localizado == 't', 'contacto_localizado'] = 'Si'
        self.BD.loc[self.BD.contacto_localizado == 'f', 'contacto_localizado'] = 'No'
        
    def guardo(self, direccion):
        
        print(self.BD.info())
        
        if direccion:
            ruta = direccion
        else:
            ruta = '../Producto/Seguimiento_BRUTO.pkl'          
        
        self.BD.to_pickle(ruta)
        print('guardado:', ruta)

