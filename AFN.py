class AFN:
    def __init__(self):
        self.estados = []
        self.transiciones = []
        self.EI = None
        self.EF = []


class Estado:
    def __init__(self, id):
        self.id = id
        self.transiciones = {}


class Transicion:
    def __init__(self, s, eI, eF):
        self.s = s
        self.eI = eI
        self.eF = eF


class Construccion:
    def __init__(self):
        pass

    def Simbolo(self):
        pass

    def Union(self):
        pass

    def Concatenacion(self):
        pass

    def CerraduraKleene(self):
        pass

    def PosicionKleene(self):
        pass

    def Interrogacion(self):
        pass
