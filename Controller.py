"""


"""
import sys

from InfixPostfix import *

from AFN import *

from AFN_Abstract import ConstruccionAbstract

from outputImage import ExportAFN

from Thompson import *


def main(argument):

    regex = InfixPostfix(argument).Infix_Postfix()
    print(regex)
    AFNTest = TransicionesConstruccion(regex).ThompsonAlgorithm()

    ExportAFN.Export(AFNTest, regex)
    print("HOLA: ", argument)
