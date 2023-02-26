"""
Basado en lo presentado por el
catedrático Bidkar Pojoy
en archivo subido a Canvas.

Adaptado a este proyecto por:
Alejandro Gomez 20347



Definición:

Este es un código en Python que define varias clases y métodos para construir y manipular un autómata finito no determinista (NFA) utilizando el algoritmo de Thompson. 
El NFA se construye a partir de una entrada de expresión regular utilizando una serie de operaciones que incluyen concatenación, unión, cierre de Kleene e interrogación. 
El NFA se define utilizando cinco clases: AFN, Transicion, Estado. 
La clase AFN define el NFA utilizando sus estados inicial y final, un conjunto de todos los estados y un conjunto de transiciones entre estados.
La clase Transicion define una transición entre dos estados utilizando un símbolo. 
La clase Estado define un estado por su identificador. 
"""


# Clase AFN
class AFN:
    """
    Esta clase define un AFN utilizando sus estados inicial y final, un conjunto de todos los estados y un conjunto de transiciones entre estados.
    """

    def __init__(self, estadoI, estadoF, estadosN, transiciones, estados):
        # Se define estados, transiciones, estado inicial y estados finales
        self.estados = estados
        self.transiciones = transiciones
        self.EI = estadoI
        self.EF = estadoF
        self.EN = estadosN 
        


# Clase Transicion
class Transicion:
    """
    Esta clase define una transicion entre dos estados utilizando un simbolo.
    """

    def __init__(self, s, eI, eF):
        # Se define el simbolo, estado inicial y estado final
        self.s, self.eI, self.eF = s, eI, eF


# Clase Estado
class Estado:
    """
    Esta clase define un estado por su identificador.
    """

    def __init__(self, id):
        # Se define el id del estado
        self.id = id


