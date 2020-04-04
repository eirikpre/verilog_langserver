import sys
import antlr4

from .grammar.SystemVerilogLexer import SystemVerilogLexer
from .grammar.SystemVerilogParser import SystemVerilogParser
from .grammar.SystemVerilogListener import SystemVerilogListener
from .grammar.SystemVerilogVisitor import SystemVerilogVisitor

from .fast_visitor import FastVisitor


class Parser:

    def __init__(self):
        self.workspace = "."

    def parse_full(self, filename):
        input_stream = antlr4.FileStream(filename)
        lexer = SystemVerilogLexer(input_stream)
        stream = antlr4.CommonTokenStream(lexer)
        parser = SystemVerilogParser(stream)
        tree = parser.source()

        # walker = antlr4.ParseTreeWalker()
        return tree

    def parse_fast(self, fname):
        input_stream = antlr4.FileStream(fname)
        lexer = SystemVerilogLexer(input_stream)
        stream = antlr4.CommonTokenStream(lexer)
        parser = SystemVerilogParser(stream)
        tree = parser.source()

        visitor = FastVisitor(fname)
        result = visitor.visit(tree)

        return visitor.items
