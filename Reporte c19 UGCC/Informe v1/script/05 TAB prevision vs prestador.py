###### Tablas
ruta   = './Informe v1/textos/'
nombre = '01TAB_previsionvscentro_total' + '.tab'
ruta+nombre
tabla  = open(str(ruta+nombre),'w')

dum = BD.copy()
A_ESCRIBIR = pd.crosstab(dum['ES FONASA'], dum['TIPO ESTABLECIMIENTO'],
            margins=True,
            margins_name='Total')
print(A_ESCRIBIR.to_latex(bold_rows= True,
                    float_format="%.1f",
                    column_format = 'rcccccc',
                    col_space=0.01),
      file=tabla)
tabla.close()
print(A_ESCRIBIR)

###### Tablas
ruta   = './Informe v1/textos/'
nombre = '01TAB_previsionvscentro_activos' + '.tab'
ruta+nombre
tabla  = open(str(ruta+nombre),'w')

dum = BD.loc[BD['ESTADO CASO'] == 'Caso activo'].copy()
A_ESCRIBIR = pd.crosstab(dum['ES FONASA'], dum['TIPO ESTABLECIMIENTO'],
            margins=True,
            margins_name='Total'
           )
print(A_ESCRIBIR.to_latex(bold_rows= True,
                    float_format="%.1f",
                    column_format = 'rcccccc',
                    col_space=0.01),
      file=tabla)
tabla.close()
print(A_ESCRIBIR)

##### Tablas
ruta   = './Informe v1/textos/'
nombre = '01TAB_previsionvscentro_activosV' + '.tab'
ruta+nombre
tabla  = open(str(ruta+nombre),'w')

dum = BD.loc[(BD['ESTADO CASO'] == 'Caso activo') &
            (BD['REGION PRESTADOR'] == 'Valparaíso')].copy()
A_ESCRIBIR = pd.crosstab(dum['ES FONASA'], dum['TIPO ESTABLECIMIENTO'],
            margins=True,
            margins_name='Total'
           )
print(A_ESCRIBIR.to_latex(bold_rows= True,
                    float_format="%.1f",
                    column_format = 'rcccccc',
                    col_space=0.01),
      file=tabla)
tabla.close()
print(A_ESCRIBIR)

##### Tablas
ruta   = './Informe v1/textos/'
nombre = '01TAB_previsionvscentro_activosRM' + '.tab'
ruta+nombre
tabla  = open(str(ruta+nombre),'w')

dum = BD.loc[(BD['ESTADO CASO'] == 'Caso activo') &
            (BD['REGION PRESTADOR'] == 'Metropolitana')].copy()
A_ESCRIBIR = pd.crosstab(dum['ES FONASA'], dum['TIPO ESTABLECIMIENTO'],
            margins=True,
            margins_name='Total'
           )
print(A_ESCRIBIR.to_latex(bold_rows= True,
                    float_format="%.1f",
                    column_format = 'rcccccc',
                    col_space=0.01),
      file=tabla)
tabla.close()
print(A_ESCRIBIR)