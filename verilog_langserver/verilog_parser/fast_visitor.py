from .items import *
from .grammar.SystemVerilogParser import SystemVerilogParser as Parser
from .grammar.SystemVerilogVisitor import SystemVerilogVisitor as Visitor

class FastVisitor(Visitor):

    def __init__(self, fname):
        self.fname = fname
        self.items = {}

    def visitModule_declaration(self, ctx:Parser.Module_declarationContext):
        obj = Module(self.fname, ctx)
        self.items.update( { obj.name, obj } )
        return None # Do not support recursive items

    def visitInterface_declaration(self, ctx:Parser.Interface_declarationContext):
        obj = Interface(self.fname, ctx)
        self.items.update( { obj.name : obj } )
        return None # Do not support recursive items

    def visitProgram_declaration(self, ctx:Parser.Program_declarationContext):
        return self.visitChildren(ctx)
    def visitPackage_declaration(self, ctx:Parser.Package_declarationContext):
        return self.visitChildren(ctx)
    def visitConfig_declaration(self, ctx:Parser.Config_declarationContext):
        return self.visitChildren(ctx)
    def visitPackage_item(self, ctx:Parser.Package_itemContext):
        return self.visitChildren(ctx)
    def visitTask_declaration(self, ctx:Parser.Task_declarationContext):
        return self.visitChildren(ctx)
    def visitFunction_declaration(self, ctx:Parser.Function_declarationContext):
        return self.visitChildren(ctx)
    def visitClass_declaration(self, ctx:Parser.Class_declarationContext):
        return self.visitChildren(ctx)





    pass