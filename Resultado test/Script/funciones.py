#!/usr/bin/python3

# Algunas funciones que usare a lo largo del programa

# verificador de RUTs


from itertools import cycle

# define el digito verificador
def digito_verificador(rut):
    reversed_digits = map(int, reversed(str(rut)))
    factors = cycle(range(2, 8))
    s = sum(d * f for d, f in zip(reversed_digits, factors))
    if (-s) % 11 == 10:
        return 'K'
    else:
        return (-s) % 11

# chequea que sea correcto
def verifico_RUT(valor):
    try:
        RUT_i  = str(valor)[:-1]
        RUT_DV =str(valor)[-1]
        if (str(digito_verificador(RUT_i)) == RUT_DV) == True:
            return 'RUT_OK'
        else:
            return 'RUT_error'
    except:
        print("ERROR! ERROR! ERROR!")
#         print(valor)
        return 'RUT_error'

def cambio_sexo(base_y_columna, dictado=None):
    # Defino la variable
    propuesta = dict()
    #creo propuesta de dict
    dict_sexual = dict({
    'HOMBRE'        : 'Hombre',
    'HOMBRE '       : 'Hombre',
    'Hombre '       : 'Hombre',
    'Masculino '    : 'Hombre',
    'Masculino'     : 'Hombre',
    'Femenino'      : 'Mujer',
    'Femenino '     : 'Mujer',
    'MUJER'         : 'Mujer',
    'Mujer '        : 'Mujer'}
    )

    if dictado == None:
        print('Usando propuesta INTERNA')
        propuesta = dict_sexual
    else:
        print('Usando propuesta ingresada')
        propuesta = dictado

    base_y_columna = base_y_columna.replace(propuesta, inplace=True)

def incluyo_laboratorio(Nombre_BD,archivo_script):
    print(
        str('x-0'*20), '\n',
        Nombre_BD,   ' Inicio ', '\n',
        str('x-0'*20), '\n',
        sep = '')
    print('Incio agregación de laboratorios...')
    print('leyendo en :', archivo_script) 
    if len(laboratorios[Nombre_BD]) == 0:
        return print (
            str('Sin bases de datos! en '+Nombre_BD + '\n')*5)    
    if len(laboratorios[Nombre_BD]) > 1:
        print (str('Más de una BD en '+Nombre_BD + '\n')*5)  
    
    print(laboratorios[Nombre_BD])


    exec(open(archivo_script).read())
    print( '\n',
        str('x-0'*20), '\n',
        Nombre_BD,   ' Fin ', '\n',
        str('x-0'*20), '\n',
        sep = '')
    print('\n')
    # return print(globals())
