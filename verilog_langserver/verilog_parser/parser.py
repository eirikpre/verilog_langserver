import sys
import antlr4

from .antlr_build.SystemVerilogLexer import SystemVerilogLexer
from .antlr_build.SystemVerilogParser import SystemVerilogParser
from .antlr_build.SystemVerilogListener import SystemVerilogListener
from .antlr_build.SystemVerilogVisitor import SystemVerilogVisitor

from .fast_visitor import FastVisitor

# =================================
# The parser splits


# =================================


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
