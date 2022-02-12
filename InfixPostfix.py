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


def Infix_Postfix(self):
    # Input vacio
    if not self.expression:
        raise ValueError("ERROR: Input vacio")

    # Declaración de variables
    stack = []
    postfix = ""

    # Recorrido de la expresión
    for i in self.expression:
        # Verificar si es un operador
        if i in self.operators:

            while (
                stack
                and stack[-1] != "("
                and self.priority[i] <= self.priority[stack[-1]]
            ):
                # Se agrega el operador a la expresión
                postfix += stack.pop()
            # Se agrega el operador al stack
            stack.append(i)
        elif i == "(":
            # Se agrega el paréntesis al stack
            stack.append(i)

        elif i == ")":
            if "(" not in stack:
                # Se verifica que el paréntesis tenga cierre
                raise ValueError("Error: No se cerraron los parentesis chavo!")

            while stack and stack[-1] != "(":
                # Se agrega el operador a la expresión
                postfix += stack.pop()
            # Se elimina el paréntesis del stack
            stack.pop()
        else:
            # Se verifica que el caracter se encuentre en el alfabeto
            if i not in set(
                "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789"
            ):
                raise ValueError(
                    f"Chavo... Has ingresado este caracter que no pertenece!: {i}"
                )
            # Se agrega el caracter a la expresión
            postfix += i

    # Verificacion de parentesis
    if "(" in stack:
        raise ValueError("Error de parentesis amigo XD")

    # Se agrega el stack a la expresión
    while stack:
        # Se agrega el operador a la expresión
        postfix += stack.pop()

    # Se devuelve la expresión en postfix
    return postfix
