BD = pd.DataFrame()

for key, df in Laboratorios_dict.items():
    if key== 'Minsal':
        print('listo!!')
    else:
        print(key, 'entradas:', df.shape[0])
        BD = BD.append(df, sort=False,)

BD.shape

print(BD.head())



normalizacion_vals = dict({
    'NEGATIVO'			: 'Negativo',
    'Negativo '			: 'Negativo',
    'INDETERMINADO '	: 'Indeterminado',
    'INDETERMINADO'		: 'Indeterminado',
    'No Concluyente '	: 'Indeterminado',
    'No Concluyente'	: 'Indeterminado',
    'POSITIVO '			: 'Positivo',
    'POSITIVO'			: 'Positivo'})

# Resigno nombres
BD.Resultado = BD.Resultado.replace(normalizacion_vals)
print(BD.Resultado.value_counts())

