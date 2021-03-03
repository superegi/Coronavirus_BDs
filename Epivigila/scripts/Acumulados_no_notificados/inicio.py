


exec(open('./funciones.py').read())
pcolor('Importadas: funciones')

fecha_lectura = '20201018'

exec(open('./Lector.py').read())
pcolor('Importadas: Lector BD')

exec(open('./Verifico_rut.py').read())
pcolor('Importadas: Verificador RUT')

exec(open('./buscador_probable.py').read())

MinsalV.to_excel('./RUT encontrados.xlsx')

# exec(open('./Lector.py').read())



