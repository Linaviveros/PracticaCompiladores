from antlr4 import *
from ExprLexer import ExprLexer
from ExprParser import ExprParser
from EvalVisitor import EvalVisitor

input_stream = InputStream(input('? '))
lexer = ExprLexer(input_stream)
tokens = CommonTokenStream(lexer)
parser = ExprParser(tokens)
tree = parser.root()

visitor = EvalVisitor()
result = visitor.visit(tree)
print("Resultado:", result)