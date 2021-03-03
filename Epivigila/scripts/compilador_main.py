from script_importador import *
from compilador_epivigila import *

lee = Importador_BASEDATOS()
lee.archivo_busca()
lee.archivo_selecciona(fecha='20210221', area='EpiV')
lee.archivo_carga()

compila = Compilador_epivigila()
compila.cargadorBD(lee.BD)
compila.limpieza1()
compila.limpieza2()
compila.limpieza3()
compila.guardo()

print('end')