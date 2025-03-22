from MiGramaticaVisitor import MiGramaticaVisitor

class EvalVisitor(MiGramaticaVisitor):
    def __init__(self):
        self.variables = {}

    def visitPrograma(self, ctx):
        for sentencia in ctx.sentencia():
            self.visit(sentencia)
        return self.variables

    def visitAssign(self, ctx):
        var = ctx.ID().getText()
        value = self.visit(ctx.expresion())
        self.variables[var] = value
        print(f"📝 {var} = {value}")
        return value

    def visitInt(self, ctx):
        return int(ctx.getText())

    def visitVariable(self, ctx):
        var = ctx.getText()
        if var not in self.variables:
            print(f"⚠️ Variable '{var}' no está inicializada. Se asume 0.")
        return self.variables.get(var, 0)

    def visitAddSub(self, ctx):
        left = self.visit(ctx.expresion(0))
        right = self.visit(ctx.expresion(1))
        if ctx.op.text == '+':
            return left + right
        else:
            return left - right

    def visitMulDiv(self, ctx):
        left = self.visit(ctx.expresion(0))
        right = self.visit(ctx.expresion(1))
        if ctx.op.text == '*':
            return left * right
        else:
            return left / right

    def visitParens(self, ctx):
        return self.visit(ctx.expresion())

    def visitIfElse(self, ctx):
        cond = self.visit(ctx.condicion())
        if cond:
            for stmt in ctx.sentencia(0).getChildren():
                self.visit(stmt)
        elif ctx.sentencia(1):
            for stmt in ctx.sentencia(1).getChildren():
                self.visit(stmt)

    def visitCondicionSimple(self, ctx):
        var = ctx.ID().getText()
        value = self.variables.get(var, 0)
        cmp_value = int(ctx.INT().getText())
        op = ctx.op.text

        if op == '>':
            return value > cmp_value
        elif op == '<':
            return value < cmp_value
        elif op == '==':
            return value == cmp_value
        elif op == '!=':
            return value != cmp_value
        return False