import numpy as np
import pandas as pd

import colorama
from colorama import Fore, Style



Epi_chile = pd.read_pickle('../BDs/BD_regiones.pkl')

print(Epi_chile.head())

Resumen_regional = pd.ExcelFile('../BDs/20200812/Resumen Regional/20200812_Resumen regional.xlsx')
print(Resumen_regional.sheet_names)

MINSAL_POSITIVOS_nuevos                      = Resumen_regional.parse('NUEVOS NOTIFICADOS PCR +')
MINSAL_POSITIVOS_acumulados_noNOTIFICADOS    = Resumen_regional.parse('ACUM NO NOTIFICADOS')
MINSAL_POSITIVOS_acumulados_siNOTIFICADOS    = Resumen_regional.parse('ACUM NOTIFICADOS')
MINSAL_PROBABLES_acumulados                  = Resumen_regional.parse('PROBABLES ACUMULADOS')
MINSAL_rutcorregido                          = Resumen_regional.parse('RUT CORREGIDOS')

print(MINSAL_POSITIVOS_acumulados_noNOTIFICADOS.head())
print(Fore.BLUE + 'Importado BD de test!')
