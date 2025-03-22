# Generated from MiGramatica.g4 by ANTLR 4.13.0
from antlr4 import *
if "." in __name__:
    from .MiGramaticaParser import MiGramaticaParser
else:
    from MiGramaticaParser import MiGramaticaParser

# This class defines a complete generic visitor for a parse tree produced by MiGramaticaParser.

class MiGramaticaVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by MiGramaticaParser#programa.
    def visitPrograma(self, ctx:MiGramaticaParser.ProgramaContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiGramaticaParser#sentencia.
    def visitSentencia(self, ctx:MiGramaticaParser.SentenciaContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiGramaticaParser#IfElse.
    def visitIfElse(self, ctx:MiGramaticaParser.IfElseContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiGramaticaParser#CondicionSimple.
    def visitCondicionSimple(self, ctx:MiGramaticaParser.CondicionSimpleContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiGramaticaParser#Assign.
    def visitAssign(self, ctx:MiGramaticaParser.AssignContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiGramaticaParser#Variable.
    def visitVariable(self, ctx:MiGramaticaParser.VariableContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiGramaticaParser#MulDiv.
    def visitMulDiv(self, ctx:MiGramaticaParser.MulDivContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiGramaticaParser#AddSub.
    def visitAddSub(self, ctx:MiGramaticaParser.AddSubContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiGramaticaParser#Parens.
    def visitParens(self, ctx:MiGramaticaParser.ParensContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiGramaticaParser#Int.
    def visitInt(self, ctx:MiGramaticaParser.IntContext):
        return self.visitChildren(ctx)



del MiGramaticaParser