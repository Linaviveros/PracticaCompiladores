from MiGramaticaListener import MiGramaticaListener

class MyListener(MiGramaticaListener):
    def exitIfElse(self, ctx):
        print("🔍 Se detectó un bloque IF-ELSE")

    def exitAssign(self, ctx):
        print("✍️ Asignación detectada:", ctx.getText())

    def exitCondicionSimple(self, ctx):
        print("⚠️ Condición con variable:", ctx.ID().getText(), ctx.op.text, ctx.INT().getText())