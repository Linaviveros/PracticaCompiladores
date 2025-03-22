from antlr4 import *
from ExprLexer import ExprLexer
from ExprParser import ExprParser
from MyListener import MyListener
from antlr4.tree.Tree import ParseTreeWalker

input_stream = InputStream(input('? '))
lexer = ExprLexer(input_stream)
tokens = CommonTokenStream(lexer)
parser = ExprParser(tokens)
tree = parser.root()

walker = ParseTreeWalker()
walker.walk(MyListener(), tree)