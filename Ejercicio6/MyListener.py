from ExprListener import ExprListener

class MyListener(ExprListener):
    def exitExpr(self, ctx):
        print("Nodo expr:", ctx.getText())