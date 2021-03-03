
import pandas as pd
import os
import script_importador as importa


wd = os.getcwd()
print(wd)

#
###############################################
# Laboratorios
###############################################
#

import compilador_labsFTP as clab

lee = importa.Importador_BASEDATOS()
lee.archivo_busca(direccion='../../BDs_FTP/')

lee.archivo_selecciona(fecha='20210213', area= 'Laboratorio_regiones')
lee.archivo_carga()
compila = clab.Compilador_laboratorios()
compila.cargadorBD(lee.BD)
compila.corrijo_rut()
compila.corrijo_resultadotest()
compila.agrego_nombreBD('20210213')
compila.set_index()
BDlabsN13 = compila.BD

print('Inicio carga 20210214')
lee.archivo_selecciona(fecha='20210214', area= 'Laboratorio_regiones')
lee.archivo_carga()
compila = clab.Compilador_laboratorios()
compila.cargadorBD(lee.BD)
compila.corrijo_rut()
compila.corrijo_resultadotest()
compila.agrego_nombreBD('20210214')
compila.set_index()
BDlabsN14 = compila.BD

print('Inicio carga 20210215')
lee.archivo_selecciona(fecha='20210215',   area= 'Laboratorio_regiones')
lee.archivo_carga()
compila = clab.Compilador_laboratorios()
compila.cargadorBD(lee.BD)
compila.corrijo_rut()
compila.corrijo_resultadotest()
compila.agrego_nombreBD('20210215')
compila.set_index()
BDlabsN15 = compila.BD


print(BDlabsN13.shape)
print(BDlabsN14.shape)
print(BDlabsN15.shape)

BDlabs = pd.concat([BDlabsN13, BDlabsN14, BDlabsN15])

print('Exportando')
BDlabs.to_pickle('./labs.pkl')
print('exportado')

#
###############################################
# EPIVIGILA
###############################################
#


import compilador_epivigila as ce

lee = importa.Importador_BASEDATOS()
lee.archivo_busca(direccion='../../BDs_FTP/')
lee.archivo_selecciona(fecha='20210215', area='notificaciones')
lee.archivo_carga()

compila = ce.Compilador_epivigila()
compila.cargadorBD(lee.BD)
compila.limpieza1()
compila.limpieza2()
compila.limpieza3()
print('Exportando')
compila.guardo('./EpiV.pkl')
print('exportado')


#
###############################################
# Seguimiento
###############################################
#

import compilador_seguimiento as cs

lee = importa.Importador_BASEDATOS()
lee.archivo_busca('../../BDs_FTP/Valparaíso')
lee.archivo_selecciona('20210215', 'Seguimiento')
lee.archivo_carga()

compila = cs.Compilador_seguimiento()
compila.cargadorBD(lee.BD)
compila.limpieza1()
compila.limpieza2()
compila.arreglo_folios()
compila.arreglo_BOOL()
compila.guardo('./Seguimiento.pkl')








print('end')


