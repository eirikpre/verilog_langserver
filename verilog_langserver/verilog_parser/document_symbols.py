import antlr4
from pygls.types import Location, DocumentSymbol, Range, Position, SymbolKind

from .antlr_build.DocumentSymbolsLexer import DocumentSymbolsLexer as Lexer
from .antlr_build.DocumentSymbolsParser import DocumentSymbolsParser as Parser
from .antlr_build.DocumentSymbolsVisitor import DocumentSymbolsVisitor as Visitor

def parse(text: str):
    input_stream = antlr4.InputStream(text)
    lexer = Lexer(input_stream)
    stream = antlr4.CommonTokenStream(lexer)
    parser = Parser(stream)
    tree = parser.source()
    visitor = VerilogVisitor()
    result = visitor.visit(tree)
    if result is not None:
        raise 'Something is up'
    return visitor.items


class HdlDocumentSymbol(DocumentSymbol):
    # self,
    # name: str,
    # kind: int,
    # range: 'Range',
    # selection_range: 'Range',
    # detail: str = None,
    # children: List['DocumentSymbol'] = None,
    # deprecated: bool = False):
    def __init__(self, ctx, kind=None):
        identifier = ctx.getChild(0, Parser.IdentifierContext).start.text
        ra = Range( start=Position(ctx.start.line, ctx.start.column),
                    end=Position(ctx.stop.line, ctx.stop.column))
        super().__init__(
            name=identifier,
            kind=kind,
            range=ra,
            selection_range=ra,
            children=[]
        )

def get_symbol_kind(ctx):
    if isinstance(ctx, Parser.Interface_declarationContext):
        return
    # elif expression:
    #     pass
    return SymbolKind.Variable

class VerilogVisitor(Visitor):

    def __init__(self):
        self.items = []
        self.scope = self.items

    def visit_symbol(self, ctx: antlr4.ParserRuleContext, kind:int=SymbolKind.Variable, visit_children:bool=True):
        id_ctx = ctx.getChild(0, Parser.IdentifierContext)

        symbol =  DocumentSymbol(
            name=id_ctx.start.text,
            kind=kind,
            range=Range(
                start=Position(ctx.start.line, ctx.start.column),
                end=Position(ctx.stop.line, ctx.stop.column)
            ),
            selection_range=Range(
                start=Position(id_ctx.start.line, id_ctx.start.column),
                end=Position(id_ctx.stop.line, id_ctx.stop.column)
            ),
            detail=None,
            children=[],
            deprecated=False
        )

        self.scope.append(symbol)

        if visit_children:
            prev_scope = self.scope
            self.scope = symbol.children
            res = self.visitChildren(ctx)
            self.scope = prev_scope
            return res


    def visitModule_declaration(self, ctx:Parser.Module_declarationContext):
        return self.visit_symbol(ctx, SymbolKind.Module, True)

    def visitInterface_declaration(self, ctx:Parser.Interface_declarationContext):
        return self.visit_symbol(ctx, SymbolKind.Interface, True)

    def visitProgram_declaration(self, ctx:Parser.Program_declarationContext):
        return self.visit_symbol(ctx, SymbolKind.Module, True)

    def visitPackage_declaration(self, ctx:Parser.Package_declarationContext):
        return self.visit_symbol(ctx, SymbolKind.Package, True)

    def visitConfig_declaration(self, ctx:Parser.Config_declarationContext):
        return self.visit_symbol(ctx, SymbolKind.Property, True)

    def visitClass_declaration(self, ctx:Parser.Class_declarationContext):
        return self.visit_symbol(ctx, SymbolKind.Class, True)

    def visitUdp_declaration(self, ctx:Parser.Udp_declarationContext):
        return self.visit_symbol(ctx, SymbolKind.Property, True)

    def visitTask_declaration(self, ctx:Parser.Task_declarationContext):
        return self.visit_symbol(ctx, SymbolKind.Method, True)

    def visitFunction_declaration(self, ctx:Parser.Function_declarationContext):
        return self.visit_symbol(ctx, SymbolKind.Function, True)

    def visitType_declaration(self, ctx:Parser.Type_declarationContext):
        return self.visit_symbol(ctx, 25, True)
