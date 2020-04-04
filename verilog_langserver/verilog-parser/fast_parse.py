from .items import *
from .grammar.VerilogParser import VerilogParser
from .grammar.VerilogParserVisitor import VerilogParserVisitor

class FastParse(VerilogParserVisitor):

    def __init__(self):
        self.items = {}

    def visitModule_declaration(self, ctx:VerilogParser.Module_declarationContext):
        obj = Module(ctx)
        self.items.update( { obj.name, obj } )
        return None # Do not support recursive modules

    def visitInterface_declaration(self, ctx:VerilogParser.Interface_declarationContext):
        return self.visitChildren(ctx)
    def visitProgram_declaration(self, ctx:VerilogParser.Program_declarationContext):
        return self.visitChildren(ctx)
    def visitPackage_declaration(self, ctx:VerilogParser.Package_declarationContext):
        return self.visitChildren(ctx)
    def visitConfig_declaration(self, ctx:VerilogParser.Config_declarationContext):
        return self.visitChildren(ctx)
    def visitPackage_item(self, ctx:VerilogParser.Package_itemContext):
        return self.visitChildren(ctx)
    def visitTask_declaration(self, ctx:VerilogParser.Task_declarationContext):
        return self.visitChildren(ctx)
    def visitFunction_declaration(self, ctx:VerilogParser.Function_declarationContext):
        return self.visitChildren(ctx)
    def visitClass_declaration(self, ctx:VerilogParser.Class_declarationContext):
        return self.visitChildren(ctx)





    pass