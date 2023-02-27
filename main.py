"""
Simbolo epsilon = E

Caracteristicas:

Convertir regex de infix a postfix para
devolver r'

r' se ingresa para construir un AFN con
McNaughton-Yamada-Thompson

Validar regex, correcto balance, manejar errores


Descripción:

Este código permite ejecutar el script Controller.py con un argumento pasado como parámetro desde la línea de comandos.

Primero, importa los módulos sys y Controller.py. Luego, toma el primer argumento pasado a través de la línea de comandos y lo almacena en la variable 'arg'.

Finalmente, llama a la función main del módulo Controller.py, pasándole como argumento el valor de 'arg'.
"""

# Imports
import sys
import Controller as c

# Argumento de terminal
arg = sys.argv[1]

# Se llama a main
c.main(arg)
