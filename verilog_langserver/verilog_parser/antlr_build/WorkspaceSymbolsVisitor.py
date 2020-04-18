# Generated from C:\Users\eirik\Desktop\verilog-langserver\verilog_langserver\verilog_parser/grammar/WorkspaceSymbols.g4 by ANTLR 4.8
from antlr4 import *
if __name__ is not None and "." in __name__:
    from .WorkspaceSymbolsParser import WorkspaceSymbolsParser
else:
    from WorkspaceSymbolsParser import WorkspaceSymbolsParser

# This class defines a complete generic visitor for a parse tree produced by WorkspaceSymbolsParser.

class WorkspaceSymbolsVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by WorkspaceSymbolsParser#source.
    def visitSource(self, ctx:WorkspaceSymbolsParser.SourceContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by WorkspaceSymbolsParser#declaration.
    def visitDeclaration(self, ctx:WorkspaceSymbolsParser.DeclarationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by WorkspaceSymbolsParser#module_declaration.
    def visitModule_declaration(self, ctx:WorkspaceSymbolsParser.Module_declarationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by WorkspaceSymbolsParser#interface_declaration.
    def visitInterface_declaration(self, ctx:WorkspaceSymbolsParser.Interface_declarationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by WorkspaceSymbolsParser#program_declaration.
    def visitProgram_declaration(self, ctx:WorkspaceSymbolsParser.Program_declarationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by WorkspaceSymbolsParser#package_declaration.
    def visitPackage_declaration(self, ctx:WorkspaceSymbolsParser.Package_declarationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by WorkspaceSymbolsParser#config_declaration.
    def visitConfig_declaration(self, ctx:WorkspaceSymbolsParser.Config_declarationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by WorkspaceSymbolsParser#class_declaration.
    def visitClass_declaration(self, ctx:WorkspaceSymbolsParser.Class_declarationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by WorkspaceSymbolsParser#udp_declaration.
    def visitUdp_declaration(self, ctx:WorkspaceSymbolsParser.Udp_declarationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by WorkspaceSymbolsParser#package_item.
    def visitPackage_item(self, ctx:WorkspaceSymbolsParser.Package_itemContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by WorkspaceSymbolsParser#task_declaration.
    def visitTask_declaration(self, ctx:WorkspaceSymbolsParser.Task_declarationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by WorkspaceSymbolsParser#function_declaration.
    def visitFunction_declaration(self, ctx:WorkspaceSymbolsParser.Function_declarationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by WorkspaceSymbolsParser#type_declaration.
    def visitType_declaration(self, ctx:WorkspaceSymbolsParser.Type_declarationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by WorkspaceSymbolsParser#parameter_port_list.
    def visitParameter_port_list(self, ctx:WorkspaceSymbolsParser.Parameter_port_listContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by WorkspaceSymbolsParser#port_list.
    def visitPort_list(self, ctx:WorkspaceSymbolsParser.Port_listContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by WorkspaceSymbolsParser#return_val.
    def visitReturn_val(self, ctx:WorkspaceSymbolsParser.Return_valContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by WorkspaceSymbolsParser#life_time.
    def visitLife_time(self, ctx:WorkspaceSymbolsParser.Life_timeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by WorkspaceSymbolsParser#identifier.
    def visitIdentifier(self, ctx:WorkspaceSymbolsParser.IdentifierContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by WorkspaceSymbolsParser#label.
    def visitLabel(self, ctx:WorkspaceSymbolsParser.LabelContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by WorkspaceSymbolsParser#hierarchical_identifier.
    def visitHierarchical_identifier(self, ctx:WorkspaceSymbolsParser.Hierarchical_identifierContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by WorkspaceSymbolsParser#constant_bit_select.
    def visitConstant_bit_select(self, ctx:WorkspaceSymbolsParser.Constant_bit_selectContext):
        return self.visitChildren(ctx)



del WorkspaceSymbolsParser