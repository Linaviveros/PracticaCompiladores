import sys
from antlr4 import *
from antlr4.error.ErrorListener import ErrorListener

from SimpleLexer import SimpleLexer
from SimpleParser import SimpleParser
from Listener import ClaseMetodoAsignacionListener
from antlr4.tree.Tree import ParseTreeWalker

# Listener personalizado para mostrar errores de sintaxis
class VerboseErrorListener(ErrorListener):
    def syntaxError(self, recognizer, offendingSymbol, line, column, msg, e):
        print(f"❌ Error de sintaxis en línea {line}, columna {column}: {msg}")

# Función principal de análisis
def parse_input(input_text):
    input_stream = InputStream(input_text)
    lexer = SimpleLexer(input_stream)
    tokens = CommonTokenStream(lexer)
    parser = SimpleParser(tokens)

    # Manejo personalizado de errores
    parser.removeErrorListeners()
    parser.addErrorListener(VerboseErrorListener())

    tree = parser.prog()
    walker = ParseTreeWalker()
    walker.walk(ClaseMetodoAsignacionListener(), tree)

if __name__ == "__main__":
    # Detectar si hay entrada por redirección (stdin) o por consola
    if not sys.stdin.isatty():
        entrada = sys.stdin.read()
    else:
        entrada = input("📝 Ingrese el código a analizar:\n")

    parse_input(entrada)
