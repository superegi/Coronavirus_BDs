
ruta   = './Informe v1/textos/'
nombre = '02Duplicados' + '.txt'
ruta+nombre
texto  = open(str(ruta+nombre),'w')

# genero un objeto que mide casos duplicados
duplicados = BD['ID_personal'].duplicated()
# aquellos que son valores únicos
(~duplicados).values.sum()
# los que son la copia de algún caso
(duplicados).values.sum()

A_ESCRIBIR = 'En la base de datos hay {casos_totales} casos, pero \
hay personas que tienen más de un registro dado que más de un \
profesional notificó el caso. \
Existen {personas} personas en los registros y   \
{multi_casos} casos que son un segundo, tercer o cuarto registro de \
un mismo paciente. \n'.format(
    casos_totales = len(duplicados),
    personas      = (~duplicados).values.sum(),
    multi_casos   = (duplicados).values.sum()
)

# genero un objeto que mide casos duplicados pero activos
duplicados = BD.loc[BD['ESTADO CASO'] == 'Caso activo']['ID_personal'].duplicated()

A_ESCRIBIR = A_ESCRIBIR + 'En los registros hay {casos_activos} casos activos, \
de ellos hay {personas_activas} personas y \
{multi_casos_activos} casos duplicados de estas personas.'.format(
    casos_activos         = len(duplicados),
    personas_activas      = (~duplicados).values.sum(),
    multi_casos_activos   = (duplicados).values.sum()
)

print(A_ESCRIBIR,file = texto)
texto.close()
print(A_ESCRIBIR)