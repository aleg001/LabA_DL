"""
Basado en lo presentado por el
catedrático Bidkar Pojoy
en archivo subido a Canvas.

Adaptado a este proyecto por:
Alejandro Gomez 20347

"""

from InfixPostfix import *

# Clase AFN


# Clase Estado
class Estado:
    def __init__(self, id):
        # Se define el id del estado
        self.id = id
        self.transiciones = {}


# Clase Transicion
class Transicion:
    def __init__(self, s, eI, eF):
        # Se define el simbolo, estado inicial y estado final
        self.s = s
        self.eI = eI
        self.eF = eF


# Clase AFN
class AFN:
    def __init__(self, estadoI, estadoF, estadosN, transiciones, estados):
        # Se define estados, transiciones, estado inicial y estados finales
        self.estados = estados
        self.transiciones = transiciones
        self.EI = estadoI
        self.EF = estadoF
        self.EN = estadosN


class TransicionesConstruccion:
    def __init__(self, rE):
        self.rE = rE
        self.EN = 0
        self.estados = []
        self.AFNS = []
        self.epsilon = "E"

        self.postfix = InfixPostfix(rE).Infix_Postfix()
        self.alfabeto = InfixPostfix(rE).Alfabeto()

    def Transiciones(self, t):
        final = []
        stack = [t]

        while stack:
            t = stack.pop()
            if isinstance(t, list):
                stack.extend(t)
            else:
                final.append(t)
        return final

    def Simbolo(self, S):
        # Se crea el estado inicial y final
        EI = Estado(0)
        EF = Estado(1)

        # Se crea la transicion
        transicion = Transicion(S, EI, EF)

        # Se agregan los estados y transiciones
        self.estados = [EI, EF]
        self.transiciones = [transicion]

        # Se define el estado inicial y final
        self.EI = EI
        self.EF = [EF]

    def Union(self, AFN, AFN2):
        # Se crea el estado inicial y final
        eI = Estado(0)
        eF = Estado(1)
        # Se crea la lista de transiciones
        transiciones = AFN.transiciones + AFN2.transiciones
        # Se agregan las transiciones
        for i in AFN.estados:
            transicion = Transicion("E", eI, i)
            transiciones.append(transicion)

        # Se agregan las transiciones
        for i in AFN2.estados:
            transicion = Transicion("E", eI, i)
            transiciones.append(transicion)

        # Se agregan las transiciones
        for i in AFN.EF:
            transicion = Transicion("E", i, eF)
            transiciones.append(transicion)

        # Se agregan las transiciones
        for i in AFN2.EF:
            transicion = Transicion("E", i, eF)
            transiciones.append(transicion)

        # Se agregan los estados y transiciones
        self.estados = [eI] + AFN.estados + AFN2.estados + [eF]
        self.transiciones = transiciones

        # Se agrega el estado inicial y final
        self.EI = eI
        self.EF = [eF]

    def Concatenacion(self, AFN, AFN2):
        # Se crea la lista de transiciones
        transiciones = AFN.transiciones + AFN2.transiciones

        for i in AFN.EF:
            # Se agregan las transiciones
            transicion = Transicion("E", i, AFN2.EI)
            transiciones.append(transicion)

        # Se agregan los estados y transiciones
        self.estados = AFN.estados + AFN2.estados
        self.transiciones = transiciones

        # Se agrega el estado inicial y final
        self.EI = AFN.EI
        self.EF = AFN2.EF

    def CerraduraKleene(self, AFN):
        eI = Estado(0)
        eF = Estado(1)
        transiciones = AFN.transiciones
        for i in AFN.estados:
            # Se agregan las transiciones de estadoInicial
            transicion = Transicion("E", i, eI)
            transiciones.append(transicion)
            # Se agregan las transiciones de estadoFinal
            transicion = Transicion("E", i, eF)
            transiciones.append(transicion)

    def QuestionMark(self, AFN):
        eI = Estado(0)
        eF = Estado(1)
        transiciones = AFN.transiciones
        for i in AFN.estados:
            # Se agregan las transiciones de estadoInicial
            transicion = Transicion("E", i, eI)
            transiciones.append(transicion)
