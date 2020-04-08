import sys
import antlr4

from .antlr_build.SystemVerilogSymbolLexer import SystemVerilogSymbolLexer as WorkspaceSymbolLexer
from .antlr_build.SystemVerilogSymbolParser import SystemVerilogSymbolParser as WorkspaceSymbolParser
# from .antlr_build.SystemVerilogSymbolListener import SystemVerilogSymbolListener as
# from .antlr_build.SystemVerilogSymbolVisitor import SystemVerilogSymbolVisitor

from .fast_visitor import FastVisitor

# =================================
# The parser splits


# =================================


class Parser:

    def __init__(self):
        self.workspace = "."

    def parse_full(self, filename):
        input_stream = antlr4.FileStream(filename)
        lexer = WorkspaceSymbolLexer(input_stream)
        stream = antlr4.CommonTokenStream(lexer)
        parser = WorkspaceSymbolParser(stream)
        tree = parser.source()

        # walker = antlr4.ParseTreeWalker()
        return tree

    def parse_fast(self, fname: str):
        input_stream = antlr4.FileStream(fname)
        lexer = WorkspaceSymbolLexer(input_stream)
        stream = antlr4.CommonTokenStream(lexer)
        parser = WorkspaceSymbolParser(stream)
        tree = parser.source()

        visitor = FastVisitor(fname)
        result = visitor.visit(tree)

        return visitor.items
