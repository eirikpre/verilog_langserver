from antlr4 import ParserRuleContext
from .antlr_build.WorkspaceSymbolParser import WorkspaceSymbolParser as Parser
from pygls.types import Location, SymbolInformation, Range, Position, SymbolKind

class Symbol(SymbolInformation):
    def __init__(self, filename, ctx: ParserRuleContext):
        self.name = ctx.getChild(0, Parser.IdentifierContext).start.text
        self.kind = None
        self.containerName = None
        self.location = Location(filename,
            Range(
            start=Position(ctx.start.line, ctx.start.column),
            end=Position(ctx.stop.line, ctx.stop.column)
        ))

class Module(Symbol):
    def __init__(self, fname, ctx: ParserRuleContext):
        super().__init__(fname, ctx)
        self.kind = SymbolKind.Module


class Interface(Symbol):
    def __init__(self, fname, ctx: ParserRuleContext):
        super().__init__(fname, ctx)
        self.kind = SymbolKind.Interface

class Class(Symbol):
    def __init__(self, fname, ctx: ParserRuleContext):
        super().__init__(fname, ctx)
        self.kind = SymbolKind.Class

class Package(Symbol):
    def __init__(self, fname, ctx: ParserRuleContext):
        super().__init__(fname, ctx)
        self.kind = SymbolKind.Package

class TaskOrFunction(Symbol):
    def __init__(self, fname, ctx: ParserRuleContext):
        super().__init__(fname, ctx)
        self.kind = SymbolKind.Function

class Defines(Symbol):
    pass

