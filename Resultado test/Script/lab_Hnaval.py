

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
    'Paciente'                                                              : 'Nombre',
    'Edad'                                                                  : 'Edad',
    'Sexo'                                                                  : 'Sexo',
    'Tipo muestra'                                                          : 'Tipo_muestra',
    'Fecha de toma de muestra'                                              : 'TS_toma',
    'Fecha de recepción de la muestra'                                      : 'TS_recepcion',
    'Fecha de resultado'                                                    : 'TS_resultado',
    'Hospital o establecimiento de origen (lugar donde se toma la muestra)' : 'origen',
    'Región de establecimiento de origen'                                   : 'origenRegion',
    'Laboratorio de referencia (lugar donde se procesa la muestra)'         : 'Laboratorio',
    'Región de laboratorio donde se procesa la muestra'                     : 'LaboratorioRegion',
    'Teléfono de contacto de paciente'                                      : 'PAC_telefono',
    'Correo de contacto de paciente'                                        : 'PAC_mail',
    'Dirección de contacto de paciente'                                     : 'PAC_direccion',
    'fecha validacioon'                                                     : 'TS_validacion'})

# Resigno nombres
Laboratorios_dict[Nombre_BD] = Laboratorios_dict[Nombre_BD].rename(columns=normalizacion_cols)

# Chequeo la integridad de los rut

Laboratorios_dict[Nombre_BD].RUT = Laboratorios_dict[Nombre_BD].RUT.str.replace('-', '', )
Laboratorios_dict[Nombre_BD]['Verificador_RUT'] = Laboratorios_dict[Nombre_BD].RUT.apply(lambda x: verifico_RUT(x))
print(Laboratorios_dict[Nombre_BD]['Verificador_RUT'].value_counts(dropna=False))

# Arreglo sexo
Laboratorios_dict[Nombre_BD].Sexo = Laboratorios_dict[Nombre_BD].Sexo.apply(str)
cambio_sexo(
    Laboratorios_dict[Nombre_BD].Sexo
    )
print(Laboratorios_dict[Nombre_BD].Sexo.value_counts())

# imprimo BD final
print(
	Laboratorios_dict[Nombre_BD].head(3).loc[:, (Laboratorios_dict[Nombre_BD].columns != 'Nombre') & (Laboratorios_dict[Nombre_BD].columns != 'RUT')]
	)
