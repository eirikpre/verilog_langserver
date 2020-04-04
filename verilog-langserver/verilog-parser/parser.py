import sys
import antlr4

from .grammar.VerilogLexer import VerilogLexer
from .grammar.VerilogParser import VerilogParser
from .grammar.VerilogParserListener import VerilogParserListener
from .grammar.VerilogParserVisitor import VerilogParserVisitor

class Parser:

    def __init__(self):
        self.workspace = "."

    def parse_full(self, filename):
        input_stream = antlr4.FileStream(filename)
        lexer = VerilogLexer(input_stream)
        stream = antlr4.CommonTokenStream(lexer)
        parser = VerilogParser(stream)
        tree = parser.source()

        walker = antlr4.ParseTreeWalker()


        return tree

    def parse_fast(self, filename):
        pass