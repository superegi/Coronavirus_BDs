from script_importador import *
from compilador_seguimiento import *

lee = Importador_BASEDATOS()
lee.archivo_busca('../../BDs_FTP/Valparaíso/')
lee.archivo_selecciona('01032021', 'Seguimiento')
lee.archivo_carga()

compila = Compilador_seguimiento()
compila.cargadorBD(lee.BD)
compila.limpieza1()
compila.limpieza2()
compila.arreglo_folios()


compila.guardo('../Producto/Seguimiento.pkl')
compila.BD.head(1000).to_excel('../Producto/Seguimiento_sample.xlsx')


BD = compila.BD

print('end')