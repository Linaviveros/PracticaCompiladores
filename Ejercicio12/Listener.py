from antlr4 import ParseTreeListener
from SimpleParser import SimpleParser

class ClaseMetodoAsignacionListener(ParseTreeListener):

    def enterClassDef(self, ctx:SimpleParser.ClassDefContext):
        # Detectamos el nombre de la clase
        print(f"Clase encontrada: {ctx.ID().getText()}")

    def enterMember(self, ctx:SimpleParser.MemberContext):
        # Si encontramos un miembro que es un método, detectamos su nombre
        if ctx.ID(1):  # El segundo ID es el nombre del método
            print(f"  Método encontrado: {ctx.ID(1).getText()}")

    def enterStat(self, ctx:SimpleParser.StatContext):
        # Detectamos asignaciones
        if ctx.ID():  # Si encontramos un identificador (una variable)
            print(f"  Asignación encontrada: {ctx.ID().getText()} = {ctx.expr().getText()}")
