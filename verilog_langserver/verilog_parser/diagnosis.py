from antlr4 import Token, DiagnosticErrorListener, FileStream, CommonTokenStream
from antlr4.error.ErrorListener import ErrorListener
from pygls.types import Diagnostic, Range, DiagnosticSeverity, Position, Location

from .antlr_build.diagnosis.SystemVerilogLexer import SystemVerilogLexer as DiagnosisLexer
from .antlr_build.diagnosis.SystemVerilogParser import SystemVerilogParser as DiagnosisParser

# Diagnosis is extremly slow at the moment,
# should use the antlr, diagnostic tool to figure
# out why.
def parse(self, fname: str):
    input_stream = FileStream(fname)
    lexer = DiagnosisLexer(input_stream)
    stream = CommonTokenStream(lexer)
    parser = DiagnosisParser(stream)
    listener = DiagnosisListener()
    parser.addErrorListener(listener)
    tree = parser.system_verilog_text()

    return listener.errors

class DiagnosisListener(DiagnosticErrorListener):

    def __init__(self):
        self.errors: [Diagnostic] = []
        super().__init__()

    def syntaxError(self, recognizer, offendingSymbol: Token, line, column, msg, e):
        err = Diagnostic(
            range=Range(Position(line, column), Position(line, column+len(offendingSymbol.text))),
            message=msg
        )
        self.errors.append(err)



