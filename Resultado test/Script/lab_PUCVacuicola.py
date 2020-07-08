

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
    'NOMBRE '                                                               : 'Nombre',
    'SEXO'                                                                  : 'Sexo',
    'EDAD'                                                                  : 'Edad',
    'RESULTADO'                                                             : 'Resultado',
    'TIPO DE MUESTRA'                                                       : 'Tipo_muestra',
    'FECHA TOMA DE MUESTRA'                                                 : 'TS_toma',
    'FECHA DE RECEPCION DE MUESTRA'                                         : 'TS_recepcion',
    'FECHA DE RESULTADO'                                                    : 'TS_resultado',
    'HOSPITAL O ESTABLECIMIENTO DE REFERENCIA'                              : 'origen',
    'Región de establecimiento de origen'                                   : 'origenRegion',
    'LABORATORIO DE REFERENCIA'                                             : 'Laboratorio',
    'Región de laboratorio donde se procesa la muestra'                     : 'LaboratorioRegion',
    'TELEFONO PACIENTE'                                                     : 'PAC_telefono',
    'CORREO PACIENTE'                                                       : 'PAC_mail',
    'DIRECCION PACIENTE'                                                    : 'PAC_direccion',
    'fecha validacioon'                                                     : 'TS_validacion'})

# Resigno nombres
Laboratorios_dict[Nombre_BD] = Laboratorios_dict[Nombre_BD].rename(columns=normalizacion_cols)

# Chequeo la integridad de los rut
Laboratorios_dict[Nombre_BD]['Verificador_RUT'] = Laboratorios_dict[Nombre_BD].RUT.apply(lambda x: verifico_RUT(x))
print(Laboratorios_dict[Nombre_BD]['Verificador_RUT'].value_counts(dropna=False))

# Arreglo sexo
Laboratorios_dict[Nombre_BD].Sexo = Laboratorios_dict[Nombre_BD].Sexo.apply(str)
Laboratorios_dict[Nombre_BD].Sexo.value_counts().index
norm_sexo = dict({
    'M'                     : 'Hombre',
    'F'                     : 'Mujer'})

# Resigno nombres
Laboratorios_dict[Nombre_BD].Sexo = Laboratorios_dict[Nombre_BD].Sexo.replace(norm_sexo)
print(Laboratorios_dict[Nombre_BD].Sexo.value_counts())

# imprimo BD final
print(
	Laboratorios_dict[Nombre_BD].head(3).loc[:, (Laboratorios_dict[Nombre_BD].columns != 'Nombre') & (Laboratorios_dict[Nombre_BD].columns != 'RUT')]
	)
