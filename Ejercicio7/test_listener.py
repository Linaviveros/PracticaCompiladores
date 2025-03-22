from antlr4 import *
from MiGramaticaLexer import MiGramaticaLexer
from MiGramaticaParser import MiGramaticaParser
from MyListener import MyListener
from antlr4.tree.Tree import ParseTreeWalker

input_stream = InputStream(input('? '))
lexer = MiGramaticaLexer(input_stream)
tokens = CommonTokenStream(lexer)
parser = MiGramaticaParser(tokens)
tree = parser.programa()

walker = ParseTreeWalker()
walker.walk(MyListener(), tree)