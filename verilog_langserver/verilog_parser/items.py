from antlr4 import ParserRuleContext
from .antlr_build.WorkspaceSymbolParser import WorkspaceSymbolParser as Parser
from pygls.types import Location, SymbolInformation, Range, Position, SymbolKind


class Symbol(SymbolInformation):
    def __init__(self, filename, ctx: ParserRuleContext, kind=None):
        super().__init__(
            name=ctx.getChild(0, Parser.IdentifierContext).start.text,
            kind=kind,
            location=Location(filename,
                Range(
                    start=Position(ctx.start.line, ctx.start.column),
                    end=Position(ctx.stop.line, ctx.stop.column)
                ))
            )


class Module(Symbol):
    def __init__(self, fn, ctx: ParserRuleContext):
        super().__init__(fn, ctx, SymbolKind.Module)

class Interface(Symbol):
    def __init__(self, fn, ctx: ParserRuleContext):
        super().__init__(fn, ctx, SymbolKind.Interface)

class Class(Symbol):
    def __init__(self, fn, ctx: ParserRuleContext):
        super().__init__(fn, ctx, SymbolKind.Class)

class Package(Symbol):
    def __init__(self, fn, ctx: ParserRuleContext):
        super().__init__(fn, ctx, SymbolKind.Package)

class Function(Symbol):
    def __init__(self, fn, ctx: ParserRuleContext):
        super().__init__(fn, ctx, SymbolKind.Function)

class Task(Symbol):
    def __init__(self, fn, ctx: ParserRuleContext):
        super().__init__(fn, ctx, SymbolKind.Function)

class Typedef(Symbol):
    def __init__(self, fn, ctx: ParserRuleContext):
        super().__init__(fn, ctx, 25)
        # 25 is TypeParameter in VSCode
        # TODO: Pull-request in new SymbolKinds to pygls

class Defines(Symbol):
    pass

