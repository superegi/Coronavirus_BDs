import wget
from datetime import datetime
import os

hoy 		= datetime.today()
hoy_web	= hoy.strftime('%Y/%m/%Y%m%d')

hoy_web = '2020/10/20201029'

from tqdm import *
import requests

def bajar_archivo(ruta, nombre_archivo):
	try:
		url		= ruta
		name 	= nombre_archivo
		with requests.get(url, stream=True) as r:
		    r.raise_for_status()
		    with open(name, 'wb') as f:
		        pbar = tqdm(total=int(r.headers['Content-Length']))
		        for chunk in r.iter_content(chunk_size=8192):
		            if chunk:  # filter out keep-alive new chunks
		                f.write(chunk)
		                pbar.update(len(chunk))
	except:
		print('error, no se pudo bajar.....')


# # Archivos AM
BD_AM		= 'http://epi.minsal.cl/wp-content/uploads/{fecha}_bases_por_region_AM.rar'.format(fecha = hoy_web)
nombre_file	= '../BDs/' + hoy.strftime('%Y%m%d') + '_AM.rar'
print('Web a bajar:    ', BD_AM)
print('Nombre archivo: ' , nombre_file)
bajar_archivo(BD_AM, nombre_file)
print('\n')

# url desde donde se baja la BD de PM
BD_PM		= 'http://epi.minsal.cl/wp-content/uploads/{fecha}_bases_por_region_PM.rar'.format(fecha = hoy_web)
nombre_file	= '../BDs/' + hoy.strftime('%Y%m%d') + '_PM.rar'
print('Web a bajar:    ', BD_PM)
print('Nombre archivo: ' , nombre_file)
bajar_archivo(BD_PM, nombre_file)
print('\n')

print('La fecha de hoy es:', hoy)

print('Los archivos bajados fueron: \n')
print(os.listdir('../BDs/'))
