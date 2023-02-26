from abc import ABC, abstractmethod

"""
Se define la clase abstracta para la construccion de AFN.

Esto se hizo para implementar patrones de diseño
como buenas practicas de programacion.

"""


class ConstruccionAbstract(ABC):
    @abstractmethod
    def Transiciones(self, t):
        pass

    @abstractmethod
    def ThompsonAlgorithm(self):
        pass

    @abstractmethod
    def Thompson(self, i):
        pass

    @abstractmethod
    def Simbolo(self, S):
        pass

    @abstractmethod
    def Union(self, AFN, AFN2):
        pass

    @abstractmethod
    def Concatenacion(self, AFN, AFN2):
        pass

    @abstractmethod
    def CerraduraKleene(self, AFN):
        pass

    @abstractmethod
    def CerraduraKleene2(self, AFN):
        pass

    @abstractmethod
    def Interrogacion(self, AFN):
        pass
