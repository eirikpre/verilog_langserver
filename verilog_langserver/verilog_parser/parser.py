import sys
import antlr4

# from .antlr_build.diagnosis.SystemVerilogLexer import SystemVerilogLexer as DiagnosisLexer
# from .antlr_build.diagnosis.SystemVerilogParser import SystemVerilogParser as DiagnosisParser

from .antlr_build.WorkspaceSymbolLexer import WorkspaceSymbolLexer
from .antlr_build.WorkspaceSymbolParser import WorkspaceSymbolParser
from .fast_visitor import FastVisitor


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
        if result is not None:
            raise 'Something is up'

        return visitor.items
