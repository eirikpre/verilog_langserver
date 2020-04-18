import antlr4
from pygls.types import Location, SymbolInformation, Range, Position, SymbolKind

from .antlr_build.WorkspaceSymbolsLexer import WorkspaceSymbolsLexer as Lexer
from .antlr_build.WorkspaceSymbolsParser import WorkspaceSymbolsParser as Parser
from .antlr_build.WorkspaceSymbolsVisitor import WorkspaceSymbolsVisitor as Visitor

def parse(uri):
    input_stream = antlr4.FileStream(uri)
    lexer = Lexer(input_stream)
    stream = antlr4.CommonTokenStream(lexer)
    parser = Parser(stream)
    tree = parser.source()
    visitor = WSVisitor(uri)
    result = visitor.visit(tree)
    if result is not None:
        raise 'Something is up'
    return visitor.items


class WorkspaceSymbol(SymbolInformation):
    def __init__(self, filename, ctx, kind=None):
        super().__init__(
            name=ctx.getChild(0, Parser.IdentifierContext).start.text,
            kind=kind,
            location=Location(filename,
                Range(
                    start=Position(ctx.start.line, ctx.start.column),
                    end=Position(ctx.stop.line, ctx.stop.column)
        )))


class WSVisitor(Visitor):

    def __init__(self, fname):
        self.fname = fname
        self.items = []

    def visitModule_declaration(self, ctx:Parser.Module_declarationContext):
        obj = WorkspaceSymbol(self.fname, ctx, SymbolKind.Module)
        self.items.append(obj)
        return None # Do not support recursive items

    def visitInterface_declaration(self, ctx:Parser.Interface_declarationContext):
        obj = WorkspaceSymbol(self.fname, ctx, SymbolKind.Interface)
        self.items.append(obj)
        return None # Do not support recursive items

    def visitProgram_declaration(self, ctx:Parser.Program_declarationContext):
        obj = WorkspaceSymbol(self.fname, ctx, SymbolKind.Module)
        self.items.append(obj)
        return None # Do not support recursive items

    def visitPackage_declaration(self, ctx:Parser.Package_declarationContext):
        obj = WorkspaceSymbol(self.fname, ctx, SymbolKind.Package)
        self.items.append(obj)
        return self.visitChildren(ctx)

    def visitTask_declaration(self, ctx:Parser.Task_declarationContext):
        obj = WorkspaceSymbol(self.fname, ctx, SymbolKind.Method)
        self.items.append(obj)
        return None # Do not support recursive items

    def visitFunction_declaration(self, ctx:Parser.Function_declarationContext):
        obj = WorkspaceSymbol(self.fname, ctx, SymbolKind.Function)
        self.items.append(obj)
        return None # Do not support recursive items

    def visitClass_declaration(self, ctx:Parser.Class_declarationContext):
        obj = WorkspaceSymbol(self.fname, ctx, SymbolKind.Class)
        self.items.append(obj)
        return None # Do not support recursive items

    def visitType_declaration(self, ctx: Parser.Type_declarationContext):
        obj = WorkspaceSymbol(self.fname, ctx, 25)
        self.items.append(obj)
        return None # Do not support recursive items

    # ========================
    #      Future
    # ========================
    # macro?
    # property?
    # config?
