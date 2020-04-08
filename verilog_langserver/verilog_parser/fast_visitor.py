from .items import *
from .antlr_build.SystemVerilogSymbolParser import SystemVerilogSymbolParser as Parser
from .antlr_build.SystemVerilogSymbolVisitor import SystemVerilogSymbolVisitor as Visitor

class FastVisitor(Visitor):

    def __init__(self, fname):
        self.fname = fname
        self.items = []

    def visitModule_declaration(self, ctx:Parser.Module_declarationContext):
        obj = Module(self.fname, ctx)
        self.items.append( obj )
        return None # Do not support recursive items

    def visitInterface_declaration(self, ctx:Parser.Interface_declarationContext):
        obj = Interface(self.fname, ctx)
        self.items.append( obj )
        return None # Do not support recursive items

    def visitProgram_declaration(self, ctx:Parser.Program_declarationContext):
        return self.visitChildren(ctx)

    def visitPackage_declaration(self, ctx:Parser.Package_declarationContext):
        obj = Package(self.fname, ctx)
        self.items.append( obj )
        return self.visitChildren(ctx)

    def visitTask_declaration(self, ctx:Parser.Task_declarationContext):
        obj = TaskOrFunction(self.fname, ctx)
        self.items.append( obj )
        return None # Do not support recursive items

    def visitFunction_declaration(self, ctx:Parser.Function_declarationContext):
        obj = TaskOrFunction(self.fname, ctx)
        self.items.append( obj )
        return None # Do not support recursive items

    def visitClass_declaration(self, ctx:Parser.Class_declarationContext):
        obj = Class(self.fname, ctx)
        self.items.append( obj )
        return None # Do not support recursive items
