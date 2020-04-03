import sys
import antlr4
from .grammar.VerilogLexer import VerilogLexer
# from grammar.VerilogParser import VerilogParser

def main(argv):
    input_stream = antlr4.FileStream(argv[1])
    lexer = VerilogLexer(input_stream)
    stream = antlr4.CommonTokenStream(lexer)
    print('Hey')
    # parser = VerilogParser(stream)
    # tree = parser.startRule()

