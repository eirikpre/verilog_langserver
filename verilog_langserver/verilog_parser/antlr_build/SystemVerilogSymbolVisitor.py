# Generated from C:\Users\eirik\Desktop\verilog-langserver\verilog_langserver\verilog_parser/grammar/SystemVerilogSymbol.g4 by ANTLR 4.8
from antlr4 import *
if __name__ is not None and "." in __name__:
    from .SystemVerilogSymbolParser import SystemVerilogSymbolParser
else:
    from SystemVerilogSymbolParser import SystemVerilogSymbolParser

# This class defines a complete generic visitor for a parse tree produced by SystemVerilogSymbolParser.

class SystemVerilogSymbolVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by SystemVerilogSymbolParser#source.
    def visitSource(self, ctx:SystemVerilogSymbolParser.SourceContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SystemVerilogSymbolParser#declaration.
    def visitDeclaration(self, ctx:SystemVerilogSymbolParser.DeclarationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SystemVerilogSymbolParser#module_declaration.
    def visitModule_declaration(self, ctx:SystemVerilogSymbolParser.Module_declarationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SystemVerilogSymbolParser#interface_declaration.
    def visitInterface_declaration(self, ctx:SystemVerilogSymbolParser.Interface_declarationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SystemVerilogSymbolParser#program_declaration.
    def visitProgram_declaration(self, ctx:SystemVerilogSymbolParser.Program_declarationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SystemVerilogSymbolParser#package_declaration.
    def visitPackage_declaration(self, ctx:SystemVerilogSymbolParser.Package_declarationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SystemVerilogSymbolParser#config_declaration.
    def visitConfig_declaration(self, ctx:SystemVerilogSymbolParser.Config_declarationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SystemVerilogSymbolParser#class_declaration.
    def visitClass_declaration(self, ctx:SystemVerilogSymbolParser.Class_declarationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SystemVerilogSymbolParser#package_item.
    def visitPackage_item(self, ctx:SystemVerilogSymbolParser.Package_itemContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SystemVerilogSymbolParser#task_declaration.
    def visitTask_declaration(self, ctx:SystemVerilogSymbolParser.Task_declarationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SystemVerilogSymbolParser#function_declaration.
    def visitFunction_declaration(self, ctx:SystemVerilogSymbolParser.Function_declarationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SystemVerilogSymbolParser#type_declaration.
    def visitType_declaration(self, ctx:SystemVerilogSymbolParser.Type_declarationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SystemVerilogSymbolParser#parameter_port_list.
    def visitParameter_port_list(self, ctx:SystemVerilogSymbolParser.Parameter_port_listContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SystemVerilogSymbolParser#port_list.
    def visitPort_list(self, ctx:SystemVerilogSymbolParser.Port_listContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SystemVerilogSymbolParser#return_val.
    def visitReturn_val(self, ctx:SystemVerilogSymbolParser.Return_valContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SystemVerilogSymbolParser#life_time.
    def visitLife_time(self, ctx:SystemVerilogSymbolParser.Life_timeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SystemVerilogSymbolParser#identifier.
    def visitIdentifier(self, ctx:SystemVerilogSymbolParser.IdentifierContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SystemVerilogSymbolParser#label.
    def visitLabel(self, ctx:SystemVerilogSymbolParser.LabelContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SystemVerilogSymbolParser#hierarchical_identifier.
    def visitHierarchical_identifier(self, ctx:SystemVerilogSymbolParser.Hierarchical_identifierContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SystemVerilogSymbolParser#constant_bit_select.
    def visitConstant_bit_select(self, ctx:SystemVerilogSymbolParser.Constant_bit_selectContext):
        return self.visitChildren(ctx)



del SystemVerilogSymbolParser