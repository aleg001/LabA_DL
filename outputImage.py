"""
Definición:
Permite exportar/abrir un autómata finito no determinístico (AFN) a una imagen en formato PNG usando la biblioteca Graphviz.


La clase ExportAFN tiene un método llamado Export que toma un objeto AFN1 como entrada. 

El método Export primero crea un objeto Digraph de Graphviz y configura la dirección de la jerarquía y el tamaño del gráfico.

Luego, se procesan los estados del AFN y se agregan al gráfico. 
Si el estado es el estado inicial, se agrega un nodo adicional llamado "start" que se conecta al estado inicial. 
Si el estado es el estado final, se agrega un nodo doblemente circular. 
Si no es ni el estado inicial ni el estado final, se agrega un nodo circular.

A continuación, se procesan las transiciones del AFN y se agregan al gráfico. 
Cada transición se representa como una arista con una etiqueta que indica el símbolo que desencadena la transición.

Finalmente, el gráfico se convierte en una imagen PNG y se muestra en una ventana temporal utilizando la biblioteca Pillow.
"""
import graphviz  # pip install graphviz
from PIL import Image  # pip install pillow
import io


class GraphAFN:
    def Show(AFN1):
        grapvizDigraph = graphviz.Digraph()
        grapvizDigraph.attr(rankdir="LR")

        estados = [(i) for i in AFN1.estados]
        for i in estados:
            if i == AFN1.EI:
                grapvizDigraph.node(
                    str(i), shape="circle", style="filled", fillcolor="green"
                )
            if i == AFN1.EF:
                grapvizDigraph.node(str(i), shape="doublecircle", style="filled")
            else:
                grapvizDigraph.node(str(i), shape="circle")

        transiciones = [i for i in AFN1.transiciones]
        for i in transiciones:
            Inicial, Simbolo, Final = str(i.eI), str(i.s), str(i.eF)
            grapvizDigraph.edge(Inicial, Final, label=str(Simbolo))
        # Conversion imagen
        pngBytes = grapvizDigraph.pipe(format="png")
        with io.BytesIO(pngBytes) as f:
            img = Image.open(f)
            img.show()
