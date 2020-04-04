# Generated from VerilogParser.g4 by ANTLR 4.8
from antlr4 import *
if __name__ is not None and "." in __name__:
    from .VerilogParser import VerilogParser
else:
    from VerilogParser import VerilogParser

# This class defines a complete listener for a parse tree produced by VerilogParser.
class VerilogParserListener(ParseTreeListener):

    # Enter a parse tree produced by VerilogParser#source.
    def enterSource(self, ctx:VerilogParser.SourceContext):
        pass

    # Exit a parse tree produced by VerilogParser#source.
    def exitSource(self, ctx:VerilogParser.SourceContext):
        pass


    # Enter a parse tree produced by VerilogParser#declaration.
    def enterDeclaration(self, ctx:VerilogParser.DeclarationContext):
        pass

    # Exit a parse tree produced by VerilogParser#declaration.
    def exitDeclaration(self, ctx:VerilogParser.DeclarationContext):
        pass


    # Enter a parse tree produced by VerilogParser#module_declaration.
    def enterModule_declaration(self, ctx:VerilogParser.Module_declarationContext):
        pass

    # Exit a parse tree produced by VerilogParser#module_declaration.
    def exitModule_declaration(self, ctx:VerilogParser.Module_declarationContext):
        pass


    # Enter a parse tree produced by VerilogParser#interface_declaration.
    def enterInterface_declaration(self, ctx:VerilogParser.Interface_declarationContext):
        pass

    # Exit a parse tree produced by VerilogParser#interface_declaration.
    def exitInterface_declaration(self, ctx:VerilogParser.Interface_declarationContext):
        pass


    # Enter a parse tree produced by VerilogParser#program_declaration.
    def enterProgram_declaration(self, ctx:VerilogParser.Program_declarationContext):
        pass

    # Exit a parse tree produced by VerilogParser#program_declaration.
    def exitProgram_declaration(self, ctx:VerilogParser.Program_declarationContext):
        pass


    # Enter a parse tree produced by VerilogParser#package_declaration.
    def enterPackage_declaration(self, ctx:VerilogParser.Package_declarationContext):
        pass

    # Exit a parse tree produced by VerilogParser#package_declaration.
    def exitPackage_declaration(self, ctx:VerilogParser.Package_declarationContext):
        pass


    # Enter a parse tree produced by VerilogParser#config_declaration.
    def enterConfig_declaration(self, ctx:VerilogParser.Config_declarationContext):
        pass

    # Exit a parse tree produced by VerilogParser#config_declaration.
    def exitConfig_declaration(self, ctx:VerilogParser.Config_declarationContext):
        pass


    # Enter a parse tree produced by VerilogParser#package_item.
    def enterPackage_item(self, ctx:VerilogParser.Package_itemContext):
        pass

    # Exit a parse tree produced by VerilogParser#package_item.
    def exitPackage_item(self, ctx:VerilogParser.Package_itemContext):
        pass


    # Enter a parse tree produced by VerilogParser#task_declaration.
    def enterTask_declaration(self, ctx:VerilogParser.Task_declarationContext):
        pass

    # Exit a parse tree produced by VerilogParser#task_declaration.
    def exitTask_declaration(self, ctx:VerilogParser.Task_declarationContext):
        pass


    # Enter a parse tree produced by VerilogParser#function_declaration.
    def enterFunction_declaration(self, ctx:VerilogParser.Function_declarationContext):
        pass

    # Exit a parse tree produced by VerilogParser#function_declaration.
    def exitFunction_declaration(self, ctx:VerilogParser.Function_declarationContext):
        pass


    # Enter a parse tree produced by VerilogParser#class_declaration.
    def enterClass_declaration(self, ctx:VerilogParser.Class_declarationContext):
        pass

    # Exit a parse tree produced by VerilogParser#class_declaration.
    def exitClass_declaration(self, ctx:VerilogParser.Class_declarationContext):
        pass



del VerilogParser