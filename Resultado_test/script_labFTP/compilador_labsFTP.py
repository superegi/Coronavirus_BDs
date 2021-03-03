# -*- coding: utf-8 -*-
"""
Editor de Spyder

Este es un archivo temporal.
"""

import pandas as pd
import os

from itertools import cycle
#from funciones_auxilares import pcolor
     
class Compilador_laboratorios:
    
    def __init__(self):
        print('Inicio módulo de compilación y limpieza')
        print('Las funciones son:')
        print('cargadorBD')
        print('corrijo_rut')
        print('guardo')


        # Archivos a leer
        self.BD = pd.DataFrame()
    
    def cargadorBD(self, database):
        self.BD = database
        
    def digito_verificador(self, rut):
        reversed_digits = map(int, reversed(str(rut)))
        factors = cycle(range(2, 8))
        s = sum(d * f for d, f in zip(reversed_digits, factors))
        if (-s) % 11 == 10:
            return 'K'
        else:
            return (-s) % 11

    # chequea que sea correcto
    def verifico_RUT(self, valor):
        try:
            RUT_i  = str(valor)[:-1]
            RUT_DV =str(valor)[-1]
            if (str(self.digito_verificador(RUT_i)) == RUT_DV) == True:
                return 'RUT_OK'
            else:
                return 'RUT_error'
        except:
            print("ERROR! ERROR! ERROR!")
            print(valor)
            return 'RUT_error'
    
    def agrego_palitoRUT(self):
        a = (self.BD.Verificador_RUT == 'RUT_OK')
        RUUUUTT = self.BD[a].RUT.str.strip().str[:-1] + '-' + self.BD[a].RUT.str.strip().str[-1]
        self.BD.loc[a==True, 'RUT'] = RUUUUTT

    def corrijo_rut(self):
        self.BD['Verificador_RUT'] = self.BD.RUT.apply(lambda x: self.verifico_RUT(x))
        self.agrego_palitoRUT()

    def corrijo_resultadotest(self):
    	# los negativos
        self.BD.loc[self.BD.Resultado.str.contains('nega', case=False), 'RESULT' ] = 'Negativo'

        # los positivos
        self.BD.loc[self.BD.Resultado.str.contains('posi', case=False), 'RESULT' ] = 'Positivo'

        # Los descartados
        dum = ['MUESTRA NO APTA']
        for x in dum:
            self.BD.loc[self.BD.Resultado.str.contains(x, case=False), 'RESULT' ] = 'Descartada'
        # Los indeterminados

        dum = ['indeter']
        for x in dum:
            self.BD.loc[self.BD.Resultado.str.contains(x, case=False), 'RESULT' ] = 'Indeterminado'

        # Los nueva muestra
        dum = ['nueva muestra']
        for x in dum:
            self.BD.loc[self.BD.Resultado.str.contains(x, case=False), 'RESULT' ] = 'Requiere nueva muestra'


    def agrego_nombreBD(self, nombre_BD):
        self.BD['nombre_BD'] = str(nombre_BD)

    def set_index(self):
        self.BD.set_index('IDLaboratorio', drop=True, inplace=True)

    
    def guardo(self, direccion=None):
        if direccion:
            self.BD.to_pickle(direccion)
        else:
            print(self.BD.info())
            self.BD.to_pickle('../Producto/LabFTP.pkl')
            print('guardado: ../Producto/LabFTP.pkl')
            
            self.BD.head(1000).to_excel('../Producto/LabFTP_sample.xlsx')
            print('guardado parcial: ../Producto/LabFTP_sample.xlsx')

    
