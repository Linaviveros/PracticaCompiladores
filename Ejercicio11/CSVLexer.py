# Generated from CSV.g4 by ANTLR 4.9.3
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
    from typing import TextIO
else:
    from typing.io import TextIO



def serializedATN():
    with StringIO() as buf:
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\2\b")
        buf.write(",\b\1\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t\7")
        buf.write("\3\2\3\2\3\3\3\3\3\4\3\4\3\5\6\5\27\n\5\r\5\16\5\30\3")
        buf.write("\6\3\6\3\6\3\6\7\6\37\n\6\f\6\16\6\"\13\6\3\6\3\6\3\7")
        buf.write("\6\7\'\n\7\r\7\16\7(\3\7\3\7\2\2\b\3\3\5\4\7\5\t\6\13")
        buf.write("\7\r\b\3\2\5\6\2\f\f\17\17$$..\3\2$$\4\2\13\13\"\"\2/")
        buf.write("\2\3\3\2\2\2\2\5\3\2\2\2\2\7\3\2\2\2\2\t\3\2\2\2\2\13")
        buf.write("\3\2\2\2\2\r\3\2\2\2\3\17\3\2\2\2\5\21\3\2\2\2\7\23\3")
        buf.write("\2\2\2\t\26\3\2\2\2\13\32\3\2\2\2\r&\3\2\2\2\17\20\7.")
        buf.write("\2\2\20\4\3\2\2\2\21\22\7\17\2\2\22\6\3\2\2\2\23\24\7")
        buf.write("\f\2\2\24\b\3\2\2\2\25\27\n\2\2\2\26\25\3\2\2\2\27\30")
        buf.write("\3\2\2\2\30\26\3\2\2\2\30\31\3\2\2\2\31\n\3\2\2\2\32 ")
        buf.write("\7$\2\2\33\34\7$\2\2\34\37\7$\2\2\35\37\n\3\2\2\36\33")
        buf.write("\3\2\2\2\36\35\3\2\2\2\37\"\3\2\2\2 \36\3\2\2\2 !\3\2")
        buf.write("\2\2!#\3\2\2\2\" \3\2\2\2#$\7$\2\2$\f\3\2\2\2%\'\t\4\2")
        buf.write("\2&%\3\2\2\2\'(\3\2\2\2(&\3\2\2\2()\3\2\2\2)*\3\2\2\2")
        buf.write("*+\b\7\2\2+\16\3\2\2\2\7\2\30\36 (\3\b\2\2")
        return buf.getvalue()


class CSVLexer(Lexer):

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    T__0 = 1
    T__1 = 2
    T__2 = 3
    TEXT = 4
    STRING = 5
    WS = 6

    channelNames = [ u"DEFAULT_TOKEN_CHANNEL", u"HIDDEN" ]

    modeNames = [ "DEFAULT_MODE" ]

    literalNames = [ "<INVALID>",
            "','", "'\r'", "'\n'" ]

    symbolicNames = [ "<INVALID>",
            "TEXT", "STRING", "WS" ]

    ruleNames = [ "T__0", "T__1", "T__2", "TEXT", "STRING", "WS" ]

    grammarFileName = "CSV.g4"

    def __init__(self, input=None, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.9.3")
        self._interp = LexerATNSimulator(self, self.atn, self.decisionsToDFA, PredictionContextCache())
        self._actions = None
        self._predicates = None


