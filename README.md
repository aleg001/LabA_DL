
# Lab A

### Uso de programa:

```python
python3 main.py "regex"
```

El usuario ingresa la regex entre comillas y la imagen se abre.

### Dependencias:

```python
pip install graphviz
pip install PIL
```

### Generales
- Implementación de algoritmos básicos de autómatas finitos no deterministas y expresiones regulares.
- Desarrollo de una sección para la base de la implementación del generador de analizadores léxicos.

### Específicos
- Conversión de una expresión regular en notación infix a notación postfix. Puede utilizar el algoritmo Shunting Yard.
- Implementación del algoritmo de Construcción de Thompson.
- Generación visual de los AF.

## Especificación del funcionamiento del programa

### Entrada
- Una expresión regular (r).

### Salida
- Por cada AFN (NFA) generado a partir de r:
    - Una imagen con el grafo correspondiente para el AF generado, mostrando el estado inicial, los estados adicionales, el estado de aceptación y las transiciones con sus símbolos correspondientes.

