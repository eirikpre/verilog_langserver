
from antlr4 import Token, DiagnosticErrorListener
from antlr4.error.ErrorListener import ErrorListener
from pygls.types import Diagnostic, Range, DiagnosticSeverity, Position, Location

from .antlr_build.diagnosis.SystemVerilogListener import SystemVerilogListener


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



