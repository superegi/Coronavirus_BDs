import numpy as np
import pandas as pd

import colorama
from colorama import Fore, Style



Epi_chile = pd.read_pickle('../../Producto/BD_regionesSUCIO.pkl')

print(Epi_chile.head())

archivo = '../../BDs/' + fecha_lectura + \
 '_bases_por_region_PM/Resumen Regional/' \
 + fecha_lectura + '_Resumen regional.xlsx'

20201008

Resumen_regional = pd.ExcelFile(archivo)
print(Resumen_regional.sheet_names)

MINSAL_POSITIVOS_nuevos                      = Resumen_regional.parse('NUEVOS NOTIFICADOS PCR +')
MINSAL_POSITIVOS_acumulados_noNOTIFICADOS    = Resumen_regional.parse('ACUM NO NOTIFICADOS')
MINSAL_POSITIVOS_acumulados_siNOTIFICADOS    = Resumen_regional.parse('ACUM NOTIFICADOS')
MINSAL_PROBABLES_acumulados                  = Resumen_regional.parse('PROBABLES ACUMULADOS')
MINSAL_rutcorregido                          = Resumen_regional.parse('RUT CORREGIDOS')

print(MINSAL_POSITIVOS_acumulados_noNOTIFICADOS.head())
print(Fore.BLUE + 'Importado BD de test!')
