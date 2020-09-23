import difflib as difflib
from fuzzywuzzy import fuzz
import datetime


# Preparo epivigila para empezar a buscar similitudes

# nombre en uno solo
Epi_chile['Nombre'] = Epi_chile.nombres_paciente + ' ' + Epi_chile.primer_apellido_paciente+ ' ' +  Epi_chile.segundo_apellido_paciente

# dejo como RUT
Epi_chile['identificacion_paciente'] = Epi_chile['identificacion_paciente'].apply(lambda x: str(x))
Epi_chile['dv'] = Epi_chile['dv'].apply(lambda x: str(x))
Epi_chile['RUT'] = Epi_chile.identificacion_paciente + Epi_chile.dv
Epi_chile['Verificador_RUT'] = Epi_chile.RUT.apply(lambda x: verifico_RUT(x))
Epi_chile['Verificador_RUT'].value_counts(dropna=False)

# variables resultantes
MinsalV['RUT_pb'] = np.nan
MinsalV['Folio_pb'] = np.nan
MinsalV['Nombres_pb'] = np.nan
MinsalV['Region_pb'] = np.nan

n= 0

for index, row in MinsalV.iterrows():
    
    nombre_separado = row['NombreCompleto'].replace('(', '').replace(')', '').split()
    MinsalV[['NombreCompleto', 'RUT']].loc[index]

    maximo = max(sum([Epi_chile.Nombre.str.contains(word) for word in nombre_separado]))
    encontrados = Epi_chile.loc[sum([Epi_chile.Nombre.str.contains(word) for word in nombre_separado]) > maximo-1]

    close_match = difflib.get_close_matches(row.RUT, encontrados.RUT)
    close_match
    if len(close_match)>0:
        print(
        	Epi_chile.loc[Epi_chile.RUT.isin(close_match)][['numero_folio', 	'fecha_notificacion',
                                                                    'etapa_clinica', 'region',
                                                                    'tipo_identificacion', 	'identificacion_paciente',
                                                                    'dv', 'Nombre' ]]
                                                                    )
        
        folios = Epi_chile.loc[Epi_chile.RUT.isin(close_match)]['numero_folio']
        Ruts = Epi_chile.loc[Epi_chile.RUT.isin(close_match)]['RUT']
        nombres = Epi_chile.loc[Epi_chile.RUT.isin(close_match)]['Nombre']
        region = Epi_chile.loc[Epi_chile.RUT.isin(close_match)]['region']

        
        MinsalV.loc[index, 'RUT_pb'] = str(Ruts.to_list())
        MinsalV.loc[index, 'Folio_pb'] = str(folios.to_list())
        MinsalV.loc[index, 'Nombres_pb'] = str(nombres.to_list())
        MinsalV.loc[index, 'Region_pb'] = str(region.to_list())

    
    n = n+1
    now = datetime.datetime.now()
    print('-------------------------', n, 'de', MinsalV.shape[0], now)

