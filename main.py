"""
Simbolo epsilon = E

Caracteristicas:

Convertir regex de infix a postfix para
devolver r'

r' se ingresa para construir un AFN con
McNaughton-Yamada-Thompson

Validar regex, correcto balance, manejar errores
"""

from InfixPostfix import *

import sys


if __name__ == "__main__":
    if len(sys.argv) == 2:
        argument = sys.argv[1]
        main(argument)
    else:
        print("Error: Ingresa un argumento")
