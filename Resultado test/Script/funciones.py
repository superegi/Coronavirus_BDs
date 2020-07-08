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


def cambio_sexo(base_y_columna):
	normalizacion_sex = dict({
	    'MUJER'				: 'Mujer',
	    'Mujer '			: 'Mujer',
	    'HOMBRE'			: 'Hombre',
	    'HOMBRE '			: 'Hombre',
	    'Hombre '			: 'Hombre'})
	base_y_columna = base_y_columna.replace(normalizacion_sex, inplace=True)