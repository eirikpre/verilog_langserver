# Generated from C:\Users\eirik\Desktop\verilog-langserver\verilog_langserver\verilog_parser/grammar/DocumentSymbols.g4 by ANTLR 4.8
from antlr4 import *
if __name__ is not None and "." in __name__:
    from .DocumentSymbolsParser import DocumentSymbolsParser
else:
    from DocumentSymbolsParser import DocumentSymbolsParser

# This class defines a complete generic visitor for a parse tree produced by DocumentSymbolsParser.

class DocumentSymbolsVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by DocumentSymbolsParser#source.
    def visitSource(self, ctx:DocumentSymbolsParser.SourceContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by DocumentSymbolsParser#declaration.
    def visitDeclaration(self, ctx:DocumentSymbolsParser.DeclarationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by DocumentSymbolsParser#module_declaration.
    def visitModule_declaration(self, ctx:DocumentSymbolsParser.Module_declarationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by DocumentSymbolsParser#interface_declaration.
    def visitInterface_declaration(self, ctx:DocumentSymbolsParser.Interface_declarationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by DocumentSymbolsParser#program_declaration.
    def visitProgram_declaration(self, ctx:DocumentSymbolsParser.Program_declarationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by DocumentSymbolsParser#package_declaration.
    def visitPackage_declaration(self, ctx:DocumentSymbolsParser.Package_declarationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by DocumentSymbolsParser#config_declaration.
    def visitConfig_declaration(self, ctx:DocumentSymbolsParser.Config_declarationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by DocumentSymbolsParser#class_declaration.
    def visitClass_declaration(self, ctx:DocumentSymbolsParser.Class_declarationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by DocumentSymbolsParser#udp_declaration.
    def visitUdp_declaration(self, ctx:DocumentSymbolsParser.Udp_declarationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by DocumentSymbolsParser#package_item.
    def visitPackage_item(self, ctx:DocumentSymbolsParser.Package_itemContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by DocumentSymbolsParser#task_declaration.
    def visitTask_declaration(self, ctx:DocumentSymbolsParser.Task_declarationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by DocumentSymbolsParser#function_declaration.
    def visitFunction_declaration(self, ctx:DocumentSymbolsParser.Function_declarationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by DocumentSymbolsParser#type_declaration.
    def visitType_declaration(self, ctx:DocumentSymbolsParser.Type_declarationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by DocumentSymbolsParser#parameter_port_list.
    def visitParameter_port_list(self, ctx:DocumentSymbolsParser.Parameter_port_listContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by DocumentSymbolsParser#port_list.
    def visitPort_list(self, ctx:DocumentSymbolsParser.Port_listContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by DocumentSymbolsParser#return_val.
    def visitReturn_val(self, ctx:DocumentSymbolsParser.Return_valContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by DocumentSymbolsParser#life_time.
    def visitLife_time(self, ctx:DocumentSymbolsParser.Life_timeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by DocumentSymbolsParser#identifier.
    def visitIdentifier(self, ctx:DocumentSymbolsParser.IdentifierContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by DocumentSymbolsParser#label.
    def visitLabel(self, ctx:DocumentSymbolsParser.LabelContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by DocumentSymbolsParser#hierarchical_identifier.
    def visitHierarchical_identifier(self, ctx:DocumentSymbolsParser.Hierarchical_identifierContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by DocumentSymbolsParser#constant_bit_select.
    def visitConstant_bit_select(self, ctx:DocumentSymbolsParser.Constant_bit_selectContext):
        return self.visitChildren(ctx)



del DocumentSymbolsParser