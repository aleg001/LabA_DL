"""
Simbolo epsilon = E

Caracteristicas:

Convertir regex de infix a postfix para
devolver r'

r' se ingresa para construir un AFN con
McNaughton-Yamada-Thompson

Validar regex, correcto balance, manejar errores
"""

import sys
import Controller as c

arg = sys.argv[1]

c.main(arg)
