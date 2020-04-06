# Generated from SystemVerilog.g4 by ANTLR 4.8
from antlr4 import *
if __name__ is not None and "." in __name__:
    from .SystemVerilogParser import SystemVerilogParser
else:
    from SystemVerilogParser import SystemVerilogParser

# This class defines a complete generic visitor for a parse tree produced by SystemVerilogParser.

class SystemVerilogVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by SystemVerilogParser#source.
    def visitSource(self, ctx:SystemVerilogParser.SourceContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SystemVerilogParser#declaration.
    def visitDeclaration(self, ctx:SystemVerilogParser.DeclarationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SystemVerilogParser#module_declaration.
    def visitModule_declaration(self, ctx:SystemVerilogParser.Module_declarationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SystemVerilogParser#interface_declaration.
    def visitInterface_declaration(self, ctx:SystemVerilogParser.Interface_declarationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SystemVerilogParser#program_declaration.
    def visitProgram_declaration(self, ctx:SystemVerilogParser.Program_declarationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SystemVerilogParser#package_declaration.
    def visitPackage_declaration(self, ctx:SystemVerilogParser.Package_declarationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SystemVerilogParser#config_declaration.
    def visitConfig_declaration(self, ctx:SystemVerilogParser.Config_declarationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SystemVerilogParser#class_declaration.
    def visitClass_declaration(self, ctx:SystemVerilogParser.Class_declarationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SystemVerilogParser#package_item.
    def visitPackage_item(self, ctx:SystemVerilogParser.Package_itemContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SystemVerilogParser#task_declaration.
    def visitTask_declaration(self, ctx:SystemVerilogParser.Task_declarationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SystemVerilogParser#function_declaration.
    def visitFunction_declaration(self, ctx:SystemVerilogParser.Function_declarationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SystemVerilogParser#parameter_port_list.
    def visitParameter_port_list(self, ctx:SystemVerilogParser.Parameter_port_listContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SystemVerilogParser#port_list.
    def visitPort_list(self, ctx:SystemVerilogParser.Port_listContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SystemVerilogParser#return_val.
    def visitReturn_val(self, ctx:SystemVerilogParser.Return_valContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SystemVerilogParser#identifier.
    def visitIdentifier(self, ctx:SystemVerilogParser.IdentifierContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SystemVerilogParser#label.
    def visitLabel(self, ctx:SystemVerilogParser.LabelContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SystemVerilogParser#hierarchical_identifier.
    def visitHierarchical_identifier(self, ctx:SystemVerilogParser.Hierarchical_identifierContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SystemVerilogParser#constant_bit_select.
    def visitConstant_bit_select(self, ctx:SystemVerilogParser.Constant_bit_selectContext):
        return self.visitChildren(ctx)



del SystemVerilogParser