import sys
from antlr4 import *
from CSVLexer import CSVLexer
from CSVParser import CSVParser
from CSVListener import CSVListener
import json

class Loader(CSVListener):
    EMPTY = ""
    
    def __init__(self):
        self.rows = []
        self.header = []
        self.currentRowFieldValues = []
        self.emptyFieldCount = 0  # Initialize the empty field counter

    def enterRow(self, ctx:CSVParser.RowContext):
        self.currentRowFieldValues = []

    def exitText(self, ctx:CSVParser.TextContext):
        self.currentRowFieldValues.append(ctx.getText())

    def exitString(self, ctx:CSVParser.StringContext):
        self.currentRowFieldValues.append(ctx.getText())

    def exitEmpty(self, ctx:CSVParser.EmptyContext):
        self.currentRowFieldValues.append(self.EMPTY)
        self.emptyFieldCount += 1  # Increment the counter for empty fields

    def exitHeader(self, ctx:CSVParser.HeaderContext):
        self.header = list(self.currentRowFieldValues)

    def exitRow(self, ctx:CSVParser.RowContext):
        # Avoid processing the row if it's part of the header
        if ctx.parentCtx.getRuleIndex() == CSVParser.RULE_header:
            return
        
        # Check if row values match the header
        if len(self.currentRowFieldValues) != len(self.header):
            print(f"Fila inválida: {self.currentRowFieldValues}")
        
        m = {}
        for i, val in enumerate(self.currentRowFieldValues):
            key = self.header[i] if i < len(self.header) else f"col_{i}"
            m[key] = val
        self.rows.append(m)

    def limpiar_montos(self):
        for fila in self.rows:
         if "Cantidad" in fila:
            fila["Cantidad"] = fila["Cantidad"].replace('"', '').replace('$','').replace(',', '')   



    def exportar_a_json(self, filename="output.json"):
        with open(filename, "w", encoding="utf-8") as f:
             json.dump(self.rows, f, indent=2, ensure_ascii=False)        
    


def main(argv):
    input_stream = FileStream(argv[1], encoding='utf-8')
    lexer = CSVLexer(input_stream)
    stream = CommonTokenStream(lexer)
    parser = CSVParser(stream)
    tree = parser.csvFile()

    loader = Loader()
    walker = ParseTreeWalker()
    walker.walk(loader, tree)

    # Print the parsed rows
    for row in loader.rows:
        print(row)

    print(f"Total de campos vacíos: {loader.emptyFieldCount}")

if __name__ == '__main__':
    main(sys.argv)
