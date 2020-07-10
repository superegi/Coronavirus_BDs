

BD = pd.DataFrame()

for key, df in Laboratorios_dict.items():
    if key== 'Minsal':
        print('listo!!')
    else:
        print(key, 'entradas:', df.shape[0])
        BD = BD.append(df, sort=False,)


# seteo el orden de las columnas

columnas = BD.columns.values
cols_1rias = ['LabBD', 'RUT', 'Nombre', 'Sexo', 'Edad', 'Tipo_muestra', 'Resultado',
              'TS_toma', 'TS_recepcion', 'TS_resultado', 'origen',
              'origenRegion', 'Laboratorio', 'LaboratorioRegion',
              'PAC_telefono', 'PAC_mail', 'PAC_direccion',  'Verificador_RUT']

c = {element for element in columnas if element not in cols_1rias}
BD = BD[cols_1rias + list(c) ]




# Dejo algunas variables en su formato
BD.Edad = pd.to_numeric(BD.Edad, errors='coerce')





normalizacion_vals = dict({
    'NEGATIVO'                  : 'Negativo',
    'NEGATIVO '                 : 'Negativo',
    'Negativo '                 : 'Negativo',
    'NEG '                      : 'Negativo',
    'NEG'                       : 'Negativo',

    'INDETERMINADO '            : 'Indeterminado',
    'INDETERMINADO'             : 'Indeterminado',
    'No Concluyente '           : 'Indeterminado',
    'No Concluyente'            : 'Indeterminado',

    'REQUIERE NUEVA MUESTRA'    : 'Requiere nueva muestra',
    'MUESTRA NO APTA'           : 'Requiere nueva muestra',

    'POSITIVO '                 : 'Positivo',
    'POSITIV '                  : 'Positivo',
    'POSITIV'                  : 'Positivo',
    'POSITIVO'                  : 'Positivo'
    })

# Resigno nombres
BD.Resultado = BD.Resultado.replace(normalizacion_vals)

print(BD.Resultado.value_counts())


# Reseteo index
BD = BD.reset_index()
BD = BD.rename(columns={'Index': 'Indice BD'})


print(BD.head())
print(BD.info())

print(BD.LabBD.value_counts())

print(BD.shape)
