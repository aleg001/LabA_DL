"""
Descripción:
Este código es el punto de entrada del programa, que tiene como objetivo construir un autómata finito no determinista a partir de una expresión regular y exportar su representación gráfica.
El programa importa módulos que implementan las funciones necesarias para realizar estas tareas.

El código importa varias clases y funciones definidas en otros archivos y define una función main que toma un argumento de entrada. 
El argumento se convierte de notación infix a postfix y se utiliza para construir un autómata finito no determinista (AFN) mediante el algoritmo de Thompson. 
Luego, se visualiza el AFN construido mediante la clase Show que genera una imagen usando Graphviz y la muestra en pantalla.
"""

from InfixPostfix import *

from AFN import *

from AFN_Abstract import ConstruccionAbstract

from outputImage import GraphAFN

from Thompson import *


def main(argument):
    regex = InfixPostfix(argument).Infix_Postfix()
    AutomataFN = TransicionesConstruccion(regex).ThompsonAlgorithm()
    GraphAFN.Show(AutomataFN)
