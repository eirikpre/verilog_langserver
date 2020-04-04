# Generated from VerilogParser.g4 by ANTLR 4.8
from antlr4 import *
if __name__ is not None and "." in __name__:
    from .VerilogParser import VerilogParser
else:
    from VerilogParser import VerilogParser

# This class defines a complete generic visitor for a parse tree produced by VerilogParser.

class VerilogParserVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by VerilogParser#source.
    def visitSource(self, ctx:VerilogParser.SourceContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by VerilogParser#declaration.
    def visitDeclaration(self, ctx:VerilogParser.DeclarationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by VerilogParser#module_declaration.
    def visitModule_declaration(self, ctx:VerilogParser.Module_declarationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by VerilogParser#interface_declaration.
    def visitInterface_declaration(self, ctx:VerilogParser.Interface_declarationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by VerilogParser#program_declaration.
    def visitProgram_declaration(self, ctx:VerilogParser.Program_declarationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by VerilogParser#package_declaration.
    def visitPackage_declaration(self, ctx:VerilogParser.Package_declarationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by VerilogParser#config_declaration.
    def visitConfig_declaration(self, ctx:VerilogParser.Config_declarationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by VerilogParser#package_item.
    def visitPackage_item(self, ctx:VerilogParser.Package_itemContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by VerilogParser#task_declaration.
    def visitTask_declaration(self, ctx:VerilogParser.Task_declarationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by VerilogParser#function_declaration.
    def visitFunction_declaration(self, ctx:VerilogParser.Function_declarationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by VerilogParser#class_declaration.
    def visitClass_declaration(self, ctx:VerilogParser.Class_declarationContext):
        return self.visitChildren(ctx)



del VerilogParser