guardar = True
nombre_archivo = 'casosnuevosUGCC' + '.png'
ruta = './Informe v1/figuras/' +  nombre_archivo

BD.groupby([
    pd.Grouper(key='FECHA DE INGRESO', freq='d'), 'TIPO ESTABLECIMIENTO']
)['ID CASO'].count().unstack().plot()

plt.legend(bbox_to_anchor=(1, 1), title= 'Notificación')

plt.xlabel('Fecha')
plt.ylabel('Cantidad de reportes nuevos')
plt.title('Registro de casos Coronavirus19 en plataforma UGCC')

# plt.xlim([inicio, fin])

if guardar == True:      
    print('Guardado:' + ruta)
    plt.savefig(ruta, bbox_inches='tight', dpi = 150)