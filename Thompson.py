
"""
Basado en lo presentado por el
catedrático Bidkar Pojoy
en archivo subido a Canvas.

Adaptado a este proyecto por:
Alejandro Gomez 20347


Definición:

La clase TransicionesConstruccion define métodos para construir un NFA a partir de una entrada de expresión regular utilizando el algoritmo de Thompson. 
Por último, la clase InfixPostfix define métodos para convertir una expresión regular de notación infija a notación postfija.
"""
from InfixPostfix import *
from AFN_Abstract import ConstruccionAbstract

from AFN import *

class TransicionesConstruccion(ConstruccionAbstract):

    """
    Esta clase define métodos para construir un AFN a partir de una entrada de expresion regular
    utilizando el algoritmo de Thompson.
    """

    def __init__(self, rE):
        self.rE = rE
        self.EN = 0
        self.estados = set()
        self.groupAFN = []
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

    def ThompsonAlgorithm(self):
        # Se recorre la expresion regular
        [self.Thompson(i) for i in self.postfix]
        # Se agrega la transicion final
        self.groupAFN[0].EN = self.EN
        return self.groupAFN[0]

    def Thompson(self, i):
        # Si es un simbolo
        if i in self.alfabeto:
            self.groupAFN.append(self.Simbolo(i))
        else:
            # concatenacion
            if i == ".":
                afn1, afn2 = self.groupAFN.pop(), self.groupAFN.pop()
                self.groupAFN.append(self.Concatenacion(afn2, afn1))
            # union
            elif i == "|":
                afn1, afn2 = self.groupAFN.pop(), self.groupAFN.pop()
                self.groupAFN.append(self.Union(afn2, afn1))
            # cerradura de kleene
            elif i == "*":
                afn = self.groupAFN.pop() 
                self.groupAFN.append(self.CerraduraKleene(afn))
            # cerradura positiva
            elif i == "+":
                afn = self.groupAFN.pop()
                self.groupAFN.append(self.CerraduraKleene2(afn))
            # cerradura ?
            elif i == "?":
                afn = self.groupAFN.pop()
                self.groupAFN.append(self.Interrogacion(afn))

    def Simbolo(self, S):
        # Se crea el estado inicial y final
        EI, EF = Estado(self.EN), Estado(self.EN + 1)
        self.EN += 2
        # Se crea la transicion
        transiciones = self.Transiciones(Transicion(EI, S, EF))
        # Se agregan los estados
        Estados = [EI, EF]
        # Se agregan los estados y transiciones
        self.estados.update(Estados)

        # Se retorna el AFN
        return AFN(EI, EF, self.EN, transiciones, Estados)

    def Union(self, AFN, AFN2):
        # Se crea el estado inicial y final
        EI, EF = Estado(self.EN), Estado(self.EN + 1)
        self.EN += 2
        # Se agregan las transiciones
        transiciones = (
            AFN.transiciones
            + AFN2.transiciones
            + [
                Transicion(self.epsilon, AFN.EI, EF),
                Transicion(self.epsilon, AFN2.EI, EF),
                Transicion(self.epsilon, EI, AFN.EI),
                Transicion(self.epsilon, EI, AFN2.EI),
            ]
        )
        # Se eliminan las transiciones repetidas
        trans_dict = {t: None for t in transiciones}
        transiciones = list(trans_dict.keys())
        # Se agregan los estados y transiciones
        estados = AFN.estados + AFN2.estados + [EI, EF]
        self.estados.update(estados)
        # Se retorna el AFN
        return AFN(EI, EF, self.EN, self.Transiciones(transiciones), estados)

    def Concatenacion(self, AFN, AFN2):
        # Se eliminan las transiciones repetidas
        AFN.estados.remove(AFN.EF)
        # Se agregan las transiciones
        for estado in AFN2.estados:
            estado.id += AFN.EN - 1
            estado.eI += AFN.EN - 1
            estado.eF += AFN.EN - 1
        AFN2.EI += AFN.EN - 1
        AFN2.EF += AFN.EN - 1
        # Se agregan los estados y transiciones
        estados = AFN.estados + AFN2.estados
        transiciones = (
            AFN.transiciones
            + AFN2.transiciones
            + [Transicion(self.epsilon, AFN.EF, AFN2.EI)]
        )
        # Se retorna el AFN
        return AFN(AFN.EI, AFN2.EF, self.EN, self.Transiciones(transiciones), estados)

    def CerraduraKleene(self, AFN):
        # Se crea el estado inicial y final
        EI, EF = Estado(self.EN), Estado(self.EN + 1)
        self.EN += 2
        # Se agregan las transiciones
        transiciones = AFN.transiciones + [
            Transicion(self.epsilon, AFN.EF, AFN.EI),
            Transicion(self.epsilon, EI, AFN.EI),
            Transicion(self.epsilon, AFN.EF, EF),
            Transicion(self.epsilon, EI, EF),
        ]
        # Se eliminan las transiciones repetidas
        trans_dict = {t: None for t in transiciones}
        transiciones = list(trans_dict.keys())
        # Se agregan los estados y transiciones
        estados = AFN.estados + [EI, EF]
        self.estados.update(estados)
        # Se retorna el AFN
        return AFN(EI, EF, self.EN, self.Transiciones(transiciones), estados)

    def CerraduraKleene2(self, AFN):
        # Se crea el estado inicial y final
        EI, EF = Estado(self.EN), Estado(self.EN + 1)
        self.EN += 2
        # Se agregan las transiciones
        transiciones = AFN.transiciones + [
            Transicion(self.epsilon, AFN.EF, AFN.EI),
            Transicion(self.epsilon, EI, AFN.EI),
            Transicion(self.epsilon, AFN.EF, EF),
        ]
        # Se eliminan las transiciones repetidas
        trans_dict = {t: None for t in transiciones}
        transiciones = list(trans_dict.keys())

        # Se agregan los estados y transiciones
        estados = AFN.estados + [EI, EF]
        self.estados.update(estados)

        # Se retorna el AFN
        return AFN(EI, EF, self.EN, self.Transiciones(transiciones), estados)

    def Interrogacion(self, AFN):
        # Se crea el estado inicial y final
        EI, EF = Estado(self.EN), Estado(self.EN + 1)
        self.EN += 2
        # Se agregan las transiciones
        transiciones = AFN.transiciones + [
            Transicion(self.epsilon, EI, AFN.EI),
            Transicion(self.epsilon, AFN.EF, EF),
            Transicion(self.epsilon, EI, EF),
        ]
        # Se eliminan las transiciones repetidas
        trans_dict = {t: None for t in transiciones}
        transiciones = list(trans_dict.keys())
        # Se agregan los estados y transiciones
        estados = AFN.estados + [EI, EF]
        self.estados.update(estados)
        # Se retorna el AFN
        return AFN(EI, EF, self.EN, self.Transiciones(transiciones), estados)