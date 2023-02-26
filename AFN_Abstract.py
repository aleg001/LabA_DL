from abc import ABC, abstractmethod

"""
Se define la clase abstracta para la construccion de AFN.

Esto se hizo para implementar patrones de diseño
como buenas practicas de programacion.

"""


class ConstruccionAbstract(ABC):
    @abstractmethod
    def Transiciones(self, t):
        # Se define el metodo abstracto para las transiciones
        pass

    @abstractmethod
    def ThompsonAlgorithm(self):
        # Se define el metodo abstracto para el algoritmo de Thompson
        pass

    @abstractmethod
    def Thompson(self, i):
        # Se define el metodo abstracto para el algoritmo de Thompson
        pass

    @abstractmethod
    def Simbolo(self, S):
        # Se define el método abstracto para el simbolo
        pass

    @abstractmethod
    def Union(self, AFN, AFN2):
        # Se define el método abstracto para la union
        pass

    @abstractmethod
    def Concatenacion(self, AFN, AFN2):
        # Se define el método abstracto para la concatenacion
        pass

    @abstractmethod
    def CerraduraKleene(self, AFN):
        # Se define el método abstracto para la cerradura de Kleene
        pass

    @abstractmethod
    def CerraduraKleene2(self, AFN):
        # Se define el método abstracto para la cerradura de Kleene
        pass

    @abstractmethod
    def Interrogacion(self, AFN):
        # Se define el método abstracto para usar el signo de interrogacion
        pass
