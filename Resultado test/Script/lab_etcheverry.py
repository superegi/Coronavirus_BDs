

# Leo la BD
ruta         = laboratorios[Nombre_BD][0]

Laboratorios_dict[Nombre_BD] = pd.read_excel(ruta, dayfirst=True,
                                            )

# creo la variable 'LabBD'
Laboratorios_dict[Nombre_BD]['LabBD'] = str('Lab_' + Nombre_BD)

# Normalizo las columnas
normalizacion_cols = dict({
    'correlativo SEREMI'                                                    : 'ID_SEREMI',
    'RUN'                                                                   : 'RUT',
    'Nombre '                                                               : 'Nombre',
    'Sexo'                                                                  : 'Sexo',
    'Edad'                                                                  : 'Edad',
    'Tipo Muestra'                                                          : 'Tipo_muestra',
    'Fecha de toma de\nmuestra'                                             : 'TS_toma',
    'Fecha de\nrecepcion de la\nmuestra'                                    : 'TS_recepcion',
    'Fecha de\nresultado'                                                   : 'TS_resultado',
    'Hospital o establecimiento de origen\n(lugar donde se toma la muestra)': 'origen',
    'Región de\nestablecimiento de origen'                                  : 'origenRegion',
    'Laboratorio de referencia (lugar\ndonde se procesa la muestra)'        : 'Laboratorio',
    'Región de laboratorio\ndonde se procesa la\nmuestra'                   : 'LaboratorioRegion',
    'Teléfono\nde contacto de\npaciente'                                    : 'PAC_telefono',
    'Correo de\ncontacto de\npaciente'                                      : 'PAC_mail',
    'Dirección\nde contacto de\npaciente'                                   : 'PAC_direccion',
    'fecha validacioon'                                                     : 'TS_validacion',
    'RUN del médico'                                                        : 'Medico_rut',
    'Nombre del médico'                                                     : 'Medico_nombre',
})

# Resigno nombres
Laboratorios_dict[Nombre_BD] = Laboratorios_dict[Nombre_BD].rename(columns=normalizacion_cols)

# Chequeo la integridad de los rut
Laboratorios_dict[Nombre_BD]['Verificador_RUT'] = Laboratorios_dict[Nombre_BD].RUT.apply(lambda x: verifico_RUT(x))
print(Laboratorios_dict[Nombre_BD]['Verificador_RUT'].value_counts(dropna=False))

# Arreglo sexo
Laboratorios_dict[Nombre_BD].Sexo = Laboratorios_dict[Nombre_BD].Sexo.apply(str)
cambio_sexo(
    Laboratorios_dict[Nombre_BD].Sexo,
    dict({
    'H'                     : 'Hombre',
    'M'                     : 'Mujer'})
    )
print(Laboratorios_dict[Nombre_BD].Sexo.value_counts())

# imprimo BD final
print(
	Laboratorios_dict[Nombre_BD].head(3).loc[:, (Laboratorios_dict[Nombre_BD].columns != 'Nombre') & (Laboratorios_dict[Nombre_BD].columns != 'RUT')]
	)
