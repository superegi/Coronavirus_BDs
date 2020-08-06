ruta   = './Informe v1/textos/'
nombre = '01Descripcion_dataset' + '.txt'
ruta+nombre
texto  = open(str(ruta+nombre),'w')


A_ESCRIBIR = 'El set de datos tiene {dataset_entradas} entradas. El ingreso de datos se comienza el {dataset_inicio} \
    y tiene su último registro el {dataset_fin}. \
    A la fecha de este reporte se encuentran {estadocaso_activo} casos activos y {estadocaso_hist} \
    casos historicos. \n'.format(
        dataset_entradas = BD['ID CASO'].count(),
        dataset_inicio   = BD['FECHA DE INGRESO'].describe()['first'].strftime('%Y-%m-%d'),
        dataset_fin   = BD['FECHA DE INGRESO'].describe()['last'].strftime('%Y-%m-%d'),
        estadocaso_activo = len(BD.groupby(['ESTADO CASO']).groups['Caso activo']),
        estadocaso_hist = len(BD.groupby(['ESTADO CASO']).groups['Caso histórico']),
)
A_ESCRIBIR = A_ESCRIBIR + ' \
De todos los casos en el set de datos, hay {casos_fonasa}, ({casos_fonasaP} \%) casos que son FONASA,  \
{casos_isapre}, ({casos_isapreP} \%) casos que son ISAPRE. \
'.format(
    casos_fonasa   = BD['PREVISION'].value_counts()['FONASA'],
    casos_fonasaP  = round(
        BD['PREVISION'].value_counts()['FONASA'] /BD['PREVISION'].value_counts().sum()*100, 
        3),
    casos_isapre   = BD['PREVISION'].value_counts()['ISAPRE'],
    casos_isapreP  = round(
        BD['PREVISION'].value_counts()['ISAPRE'] /BD['PREVISION'].value_counts().sum()*100, 
        3)
)
print(A_ESCRIBIR,file = texto)
texto.close()
print(A_ESCRIBIR)