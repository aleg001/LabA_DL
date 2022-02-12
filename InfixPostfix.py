"""
Clase que convierte una expresión infix a postfix

"""


class InfixPostfix:

    # Constructor
    def __init__(self, expression):

        # Variable de instancia
        self.expression = expression

        # Prioridad de operadores
        self.priority = {
            "(": 0,
            ")": 0,
            "": 0,
            "|": 1,
            ".": 2,
            "*": 3,
            "+": 3,
            "?": 3,
            "E": 3,
        }

        # Operadores
        self.operators = ["|", ".", "*", "+", "?", "E"]

    # Alfabeto de expresiones
    def Alfabeto(self):
        # Set con todos los caracteres de la expresión
        all_chars = set(self.expression)

        # Se eliminan operadores y paréntesis
        alphabet_chars = all_chars.difference(set("().*+|$?"))

        # Se retorna el alfabeto
        return sorted(list(alphabet_chars))
