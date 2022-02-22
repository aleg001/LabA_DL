import graphviz  # pip install graphviz
import PIL as pil  # pip install pillow


class ExportAFN:
    def __init__(self, path):
        self.graph = graphviz.Digraph(format="png", name=("AFN"))
        self.graph.node("ini", style="invis")

    def Export(self, AFN):
        grapvizDigraph = self.graph
        for i in AFN.estados:
            if i in AFN.EF:
                grapvizDigraph.node(str(i), shape="doublecircle")
            if i == AFN.EI:
                grapvizDigraph.edge("ini", str(i))
            else:
                grapvizDigraph.node(str(i), shape="circle")

        pil.Image.open("AFN.png")
