# Generated from C:\Users\eirik\Desktop\verilog-langserver\verilog_langserver\verilog_parser/grammar/WorkspaceSymbol.g4 by ANTLR 4.8
from antlr4 import *
if __name__ is not None and "." in __name__:
    from .WorkspaceSymbolParser import WorkspaceSymbolParser
else:
    from WorkspaceSymbolParser import WorkspaceSymbolParser

# This class defines a complete generic visitor for a parse tree produced by WorkspaceSymbolParser.

class WorkspaceSymbolVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by WorkspaceSymbolParser#source.
    def visitSource(self, ctx:WorkspaceSymbolParser.SourceContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by WorkspaceSymbolParser#declaration.
    def visitDeclaration(self, ctx:WorkspaceSymbolParser.DeclarationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by WorkspaceSymbolParser#module_declaration.
    def visitModule_declaration(self, ctx:WorkspaceSymbolParser.Module_declarationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by WorkspaceSymbolParser#interface_declaration.
    def visitInterface_declaration(self, ctx:WorkspaceSymbolParser.Interface_declarationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by WorkspaceSymbolParser#program_declaration.
    def visitProgram_declaration(self, ctx:WorkspaceSymbolParser.Program_declarationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by WorkspaceSymbolParser#package_declaration.
    def visitPackage_declaration(self, ctx:WorkspaceSymbolParser.Package_declarationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by WorkspaceSymbolParser#config_declaration.
    def visitConfig_declaration(self, ctx:WorkspaceSymbolParser.Config_declarationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by WorkspaceSymbolParser#class_declaration.
    def visitClass_declaration(self, ctx:WorkspaceSymbolParser.Class_declarationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by WorkspaceSymbolParser#package_item.
    def visitPackage_item(self, ctx:WorkspaceSymbolParser.Package_itemContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by WorkspaceSymbolParser#task_declaration.
    def visitTask_declaration(self, ctx:WorkspaceSymbolParser.Task_declarationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by WorkspaceSymbolParser#function_declaration.
    def visitFunction_declaration(self, ctx:WorkspaceSymbolParser.Function_declarationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by WorkspaceSymbolParser#type_declaration.
    def visitType_declaration(self, ctx:WorkspaceSymbolParser.Type_declarationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by WorkspaceSymbolParser#parameter_port_list.
    def visitParameter_port_list(self, ctx:WorkspaceSymbolParser.Parameter_port_listContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by WorkspaceSymbolParser#port_list.
    def visitPort_list(self, ctx:WorkspaceSymbolParser.Port_listContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by WorkspaceSymbolParser#return_val.
    def visitReturn_val(self, ctx:WorkspaceSymbolParser.Return_valContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by WorkspaceSymbolParser#life_time.
    def visitLife_time(self, ctx:WorkspaceSymbolParser.Life_timeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by WorkspaceSymbolParser#identifier.
    def visitIdentifier(self, ctx:WorkspaceSymbolParser.IdentifierContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by WorkspaceSymbolParser#label.
    def visitLabel(self, ctx:WorkspaceSymbolParser.LabelContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by WorkspaceSymbolParser#hierarchical_identifier.
    def visitHierarchical_identifier(self, ctx:WorkspaceSymbolParser.Hierarchical_identifierContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by WorkspaceSymbolParser#constant_bit_select.
    def visitConstant_bit_select(self, ctx:WorkspaceSymbolParser.Constant_bit_selectContext):
        return self.visitChildren(ctx)



del WorkspaceSymbolParser