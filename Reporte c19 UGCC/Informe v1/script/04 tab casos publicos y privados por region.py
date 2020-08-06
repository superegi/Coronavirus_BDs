ruta   = './Informe v1/textos/'
nombre = '04TAB_publicosprivadosxregion' + '.tab'
ruta+nombre
tabla  = open(str(ruta+nombre),'w')

BD.groupby(['REGION PACIENTE', 'TIPO ESTABLECIMIENTO', 'ESTADO CASO']).ID_personal.count().agg('sum')
A_ESCRIBIR = pd.crosstab(
    BD['REGION PRESTADOR'],
    [BD['ESTADO CASO'], BD['TIPO ESTABLECIMIENTO']])
print(A_ESCRIBIR.to_latex(bold_rows= True,
                    float_format="%.1f",
                    column_format = 'rcccccc',
                    multicolumn_format = 'c',
                    col_space=0.01),
      file=tabla)
tabla.close()
print(A_ESCRIBIR)
