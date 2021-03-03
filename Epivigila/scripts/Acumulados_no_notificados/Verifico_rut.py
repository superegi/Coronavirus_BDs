

MINSAL_POSITIVOS_acumulados_noNOTIFICADOS.columns
MINSAL_POSITIVOS_acumulados_noNOTIFICADOS['Verificador_RUT'] = MINSAL_POSITIVOS_acumulados_noNOTIFICADOS.RUT.apply(lambda x: verifico_RUT(x))
MINSAL_POSITIVOS_acumulados_noNOTIFICADOS['Verificador_RUT'].value_counts(dropna=False)


# Me enfoco en la V región y calculo los que tengan mal RUT en laboratorios

MinsalV = MINSAL_POSITIVOS_acumulados_noNOTIFICADOS.loc[
    (MINSAL_POSITIVOS_acumulados_noNOTIFICADOS.region_toma_muestra == 'Región de Valparaíso') |
    (MINSAL_POSITIVOS_acumulados_noNOTIFICADOS.region_toma_muestra == 'Valparaíso')].copy()

print(MinsalV.shape)
MinsalV.head(2)
print(MinsalV['Verificador_RUT'].value_counts(dropna=False))


