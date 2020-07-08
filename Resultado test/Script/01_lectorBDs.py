

# listo los archivos disponibles que he bajado
lista_archivos = []
for dirname, dirnames, filenames in os.walk('./BDs'):
    for filename in filenames:
        lista_archivos.append(os.path.join(dirname, filename))
archivos = lista_archivos

# asigno una variable por cada archivo diponible
laboratorios = {}

laboratorios['Integramedica']	= [s for s in archivos if "integramedica" in s]
laboratorios['Barnafi']	 		= [s for s in archivos if "Barnafi" in s]
laboratorios['PUCVmolecular']	= [s for s in archivos if "PUCV molecular" in s]
laboratorios['PUCVacuicula']	= [s for s in archivos if "PUCV acuicula" in s]
laboratorios['ETCHEVERRY']		= [s for s in archivos if "ETCHEVERRY" in s]
laboratorios['Labocenter']		= [s for s in archivos if "Labocenter" in s]
laboratorios['UV']	 			= [s for s in archivos if "UV" in s]

laboratorios['HCVB']	 		= [s for s in archivos if 'HCVB' in s]
laboratorios['UPLA']	 		= [s for s in archivos if 'UPLA' in s]
laboratorios['UC']	 			= [s for s in archivos if ' UC' in s]
laboratorios['HOSCA']			= [s for s in archivos if 'HOSCA' in s]
laboratorios['Hquilpue']		= [s for s in archivos if 'Hquilpue' in s]
laboratorios['Hnaval']	 		= [s for s in archivos if 'Hnaval' in s]
laboratorios['HEP']	 			= [s for s in archivos if 'HEP' in s]
laboratorios['HSMQ']	 		= [s for s in archivos if 'HSMQ' in s]
laboratorios['TAAG']			= [s for s in archivos if 'TAAG' in s]

laboratorios['MINSAL']	 		= [s for s in archivos if "Minsal" in s]
laboratorios['SeremiV']	 		= [s for s in archivos if "SeremiV" in s]

