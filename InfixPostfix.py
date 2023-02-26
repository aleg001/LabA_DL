"""
Clase que convierte una expresión infix a postfix

La clase InfixPostfix convierte una expresión en notación infix a notación postfix. 
Para ello, se utiliza el algoritmo shunting yard.

"""


class InfixPostfix:

    """
    Constructor
    El constructor de la clase recibe como parámetro una expresión en notación infix y crea una variable de instancia con dicho valor.
    Además, inicializa los diccionarios de prioridad y los operadores que se utilizarán durante la conversión.
    """

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

    """
    El método Alfabeto retorna una lista ordenada de todos los caracteres 
    que conforman el alfabeto de la expresión, eliminando los operadores y paréntesis.
    """

    def Alfabeto(self):
        # Set con todos los caracteres de la expresión
        all_chars = set(self.expression)

        # Se eliminan operadores y paréntesis
        alphabet_chars = all_chars.difference(set("().*+|$?"))

        # Se retorna el alfabeto
        return sorted(list(alphabet_chars))

    """
    El método Infix_Postfix realiza la conversión de la expresión de notación infix a postfix. 
    Primero, se verifica si la expresión es vacía, en caso contrario se declara un stack y una cadena de caracteres (postfix) que contendrá la expresión en notación postfix.

    Luego, se recorre la expresión de izquierda a derecha y se realiza lo siguiente:

    Si el caracter es un operador, se verifica si hay operadores en el stack que tengan mayor o igual prioridad y se van sacando de la pila y agregando a la cadena postfix. Finalmente, se agrega el operador actual al stack.
    Si el caracter es un paréntesis izquierdo, se agrega al stack.
    Si el caracter es un paréntesis derecho, se sacan los operadores del stack y se agregan a postfix hasta encontrar el paréntesis izquierdo correspondiente. Se elimina el paréntesis izquierdo del stack.
    Si el caracter es un caracter del alfabeto, se agrega directamente a la cadena postfix.
    Si el caracter no pertenece al alfabeto, se lanza una excepción informando que se ha ingresado un caracter no válido.
    Al finalizar el recorrido, se verifica si hay paréntesis sin cerrar en el stack. En caso afirmativo, se lanza una excepción informando el error. Luego, se van sacando los operadores restantes del stack y se agregan a la cadena postfix.

    Finalmente, se retorna la expresión en notación postfix.
    
    """

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

                """
                Excepciones
                Si la expresión es vacía, se lanza una excepción informando que se ha ingresado un input vacío.
                Si un paréntesis derecho no tiene un paréntesis izquierdo correspondiente, se lanza una excepción informando que no se cerraron los paréntesis.
                Si un caracter no pertenece al alfabeto de la expresión, se lanza una excepción informando que se ha ingresado un caracter inválido.
                Si hay paréntesis sin cerrar al finalizar el recorrido, se lanza una excepción informando que hay un error de paréntesis.
                
                """

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
