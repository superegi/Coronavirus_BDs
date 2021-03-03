from script_importador import *
from compilador_labsFTP import *
import pandas as pd


lee = Importador_BASEDATOS()
lee.archivo_busca(direccion='../../BDs_FTP/')

lee.archivo_selecciona(fecha='20210213')
lee.archivo_carga()

compila = Compilador_laboratorios()
compila.cargadorBD(lee.BD)
compila.corrijo_rut()
compila.corrijo_resultadotest()
compila.agrego_nombreBD('20210213')
compila.set_index()
compila.guardo()

print('compilado')


