"""
Definicion de clases abstractas para automata.
Usado para definir las clases de AFN y AFD

"""
from abc import ABC, abstractmethod


class Automata(ABC):
    """
    Clase abstracta para automata
    """

    @abstractmethod
    def __init__(self, estadoI, estadoF, estadosN, transiciones, estados):
        pass


class Transicion(ABC):
    """
    Clase abstracta para transicion
    """

    @abstractmethod
    def __init__(self, s, eI, eF):
        pass


class Estado(ABC):
    """
    Clase abstracta para estado
    """

    @abstractmethod
    def __init__(self, id):
        pass
