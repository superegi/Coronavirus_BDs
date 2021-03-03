
from termcolor import colored
from colorama import Fore, Style

class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'

    def disable(self):
        self.HEADER = ''
        self.OKBLUE = ''
        self.OKGREEN = ''
        self.WARNING = ''
        self.FAIL = ''
        self.ENDC = ''

print(bcolors.WARNING + "Warning" + bcolors.ENDC)

def pcolor(string):
    TS = pd.Timestamp.now().strftime('%H:%M:%S')
    TS = '[' + TS + ']'

	return print(bcolors.WARNING +TS + string + bcolors.ENDC)


# define el digito verificador
from itertools import cycle

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




print(Fore.BLUE + "Funciones importadas")