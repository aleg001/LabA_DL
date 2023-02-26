"""
Definición:
Permite exportar/abrir un autómata finito no determinístico (AFN) a una imagen en formato PNG usando la biblioteca Graphviz.
"""
import graphviz  # pip install graphviz
import PIL as pil  # pip install pillow


class ExportAFN:
    def Export(AFN, Regex):
        grapvizDigraph = graphviz.Digraph(comment=Regex)
        grapvizDigraph.attr(rankdir="LR", size="8,5")
        for i in AFN.estados:
            if i in AFN.EF:
                grapvizDigraph.node(str(i), shape="doublecircle")
            if i == AFN.EI:
                grapvizDigraph.edge("ini", str(i))
            else:
                grapvizDigraph.node(str(i), shape="circle")

        pil.Image.open("AFN.png")
