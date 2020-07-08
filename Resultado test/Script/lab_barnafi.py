

# Leo la BD
Nombre_BD    = 'Barnafi'
ruta         = laboratorios[Nombre_BD][0]

Laboratorios_dict[Nombre_BD] = pd.read_excel(ruta, dayfirst=True,
                                             sheet_name='BARNAFI_KRAUSE',
                                             skiprows=3
                                            )
# creo la variable 'LabBD'
Laboratorios_dict[Nombre_BD]['LabBD'] = str('Lab_' + Nombre_BD)


# creo el TS de ingreso
Laboratorios_dict[Nombre_BD]['TS_recepcion'] = pd.to_datetime(
    arg = (Laboratorios_dict[Nombre_BD]['Fecha Ingreso'].astype(str) + ' '+  Laboratorios_dict[Nombre_BD]['Hora ingreso'].astype(str)),
    format=('%Y-%m-%d %H:%M:%S'))

# Elimino algunas columnas redundates
Laboratorios_dict[Nombre_BD].drop(
    columns= ['Fecha Ingreso', 'Hora ingreso', 'Código BK', 'Examen',
              'Fecha Resultado', 'Hora Resultado', 'Unnamed: 16'],
    index=1,
    inplace=True)

# Chequeo la integridad de los rut
Laboratorios_dict[Nombre_BD]['Verificador_RUT'] = Laboratorios_dict[Nombre_BD].Rut.apply(lambda x: verifico_RUT(x))
Laboratorios_dict[Nombre_BD]['Verificador_RUT'].value_counts(dropna=False)

# Normalizo las columnas
normalizacion_cols = dict({
    'correlativo SEREMI'													: 'ID_SEREMI',
    'Paciente' 																: 'Nombre',
    'Rut'																	: 'RUT',
    'Edad'																	: 'Edad',
    'Sexo'																	: 'Sexo',
    'Tipo muestra'															: 'Tipo_muestra',
    'Toma Mues.'															: 'TS_toma',
    'Fecha de recepción de la muestra'										: 'TS_recepcion',
    'fecha hora resulados'													: 'TS_resultado',
    'Hospital o establecimiento de origen (lugar donde se toma la muestra)'	: 'origen',
    'Región de establecimiento de origen'									: 'origenRegion',
    'Laboratorio de referencia (lugar donde se procesa la muestra)'			: 'Laboratorio',
    'Región de laboratorio donde se procesa la muestra'						: 'LaboratorioRegion',
    'Teléfono de contacto de paciente'										: 'PAC_telefono',
    'Correo de contacto de paciente'										: 'PAC_mail',
    'Dirección de contacto de paciente'										: 'PAC_direccion',
    'fecha validacioon'														: 'TS_validacion'})

# Resigno nombres
Laboratorios_dict[Nombre_BD] = Laboratorios_dict[Nombre_BD].rename(columns=normalizacion_cols)

# Arreglo sexo
Laboratorios_dict[Nombre_BD].Sexo = Laboratorios_dict[Nombre_BD].Sexo.apply(str)
Laboratorios_dict[Nombre_BD].Sexo.value_counts().index
norm_sexo = dict({
    'M' 					: 'Hombre',
    '0' 					: np.nan,
    'F' 					: 'Mujer'})

# Resigno nombres
Laboratorios_dict[Nombre_BD].Sexo = Laboratorios_dict[Nombre_BD].Sexo.replace(norm_sexo)
Laboratorios_dict[Nombre_BD].Sexo.value_counts()

print(
	Laboratorios_dict[Nombre_BD].head(3).loc[:, (Laboratorios_dict[Nombre_BD].columns != 'Nombre') & (Laboratorios_dict[Nombre_BD].columns != 'RUT')]
	)
