# Generated from C:\Users\eirik\Desktop\verilog-langserver\verilog_langserver\verilog_parser/grammar/WorkspaceSymbol.g4 by ANTLR 4.8
# encoding: utf-8
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
	from typing import TextIO
else:
	from typing.io import TextIO


def serializedATN():
    with StringIO() as buf:
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\3;")
        buf.write("\u0106\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t\7")
        buf.write("\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\4\r\t\r\4\16")
        buf.write("\t\16\4\17\t\17\4\20\t\20\4\21\t\21\4\22\t\22\4\23\t\23")
        buf.write("\4\24\t\24\4\25\t\25\4\26\t\26\3\2\7\2.\n\2\f\2\16\2\61")
        buf.write("\13\2\3\2\3\2\3\3\3\3\3\3\3\3\3\3\3\3\3\3\5\3<\n\3\3\4")
        buf.write("\3\4\3\4\5\4A\n\4\3\4\7\4D\n\4\f\4\16\4G\13\4\3\4\3\4")
        buf.write("\5\4K\n\4\3\5\3\5\3\5\5\5P\n\5\3\5\7\5S\n\5\f\5\16\5V")
        buf.write("\13\5\3\5\3\5\5\5Z\n\5\3\6\3\6\5\6^\n\6\3\6\3\6\7\6b\n")
        buf.write("\6\f\6\16\6e\13\6\3\6\3\6\5\6i\n\6\3\7\3\7\3\7\7\7n\n")
        buf.write("\7\f\7\16\7q\13\7\5\7s\n\7\3\7\3\7\5\7w\n\7\3\b\3\b\3")
        buf.write("\b\7\b|\n\b\f\b\16\b\177\13\b\3\b\3\b\5\b\u0083\n\b\3")
        buf.write("\t\5\t\u0086\n\t\3\t\3\t\5\t\u008a\n\t\3\t\3\t\7\t\u008e")
        buf.write("\n\t\f\t\16\t\u0091\13\t\3\t\3\t\5\t\u0095\n\t\3\n\3\n")
        buf.write("\3\n\7\n\u009a\n\n\f\n\16\n\u009d\13\n\3\n\3\n\5\n\u00a1")
        buf.write("\n\n\3\13\3\13\3\13\3\13\5\13\u00a7\n\13\3\f\3\f\3\f\7")
        buf.write("\f\u00ac\n\f\f\f\16\f\u00af\13\f\3\f\3\f\5\f\u00b3\n\f")
        buf.write("\3\r\3\r\3\r\3\r\3\r\7\r\u00ba\n\r\f\r\16\r\u00bd\13\r")
        buf.write("\3\r\3\r\5\r\u00c1\n\r\3\16\3\16\7\16\u00c5\n\16\f\16")
        buf.write("\16\16\u00c8\13\16\3\16\3\16\3\16\3\17\3\17\7\17\u00cf")
        buf.write("\n\17\f\17\16\17\u00d2\13\17\3\17\3\17\3\20\3\20\7\20")
        buf.write("\u00d8\n\20\f\20\16\20\u00db\13\20\3\20\3\20\3\21\3\21")
        buf.write("\7\21\u00e1\n\21\f\21\16\21\u00e4\13\21\5\21\u00e6\n\21")
        buf.write("\3\22\3\22\3\23\3\23\3\24\3\24\3\24\3\25\3\25\5\25\u00f1")
        buf.write("\n\25\3\25\3\25\3\25\3\25\7\25\u00f7\n\25\f\25\16\25\u00fa")
        buf.write("\13\25\3\25\3\25\3\26\3\26\3\26\7\26\u0101\n\26\f\26\16")
        buf.write("\26\u0104\13\26\3\26\17ETco}\u008f\u009b\u00ad\u00bb\u00c6")
        buf.write("\u00d0\u00d9\u00e2\2\27\2\4\6\b\n\f\16\20\22\24\26\30")
        buf.write("\32\34\36 \"$&(*\2\3\3\2\7\b\2\u011a\2/\3\2\2\2\4;\3\2")
        buf.write("\2\2\6=\3\2\2\2\bL\3\2\2\2\n[\3\2\2\2\fj\3\2\2\2\16x\3")
        buf.write("\2\2\2\20\u0085\3\2\2\2\22\u0096\3\2\2\2\24\u00a6\3\2")
        buf.write("\2\2\26\u00a8\3\2\2\2\30\u00b4\3\2\2\2\32\u00c2\3\2\2")
        buf.write("\2\34\u00cc\3\2\2\2\36\u00d5\3\2\2\2 \u00e5\3\2\2\2\"")
        buf.write("\u00e7\3\2\2\2$\u00e9\3\2\2\2&\u00eb\3\2\2\2(\u00f0\3")
        buf.write("\2\2\2*\u0102\3\2\2\2,.\5\4\3\2-,\3\2\2\2.\61\3\2\2\2")
        buf.write("/-\3\2\2\2/\60\3\2\2\2\60\62\3\2\2\2\61/\3\2\2\2\62\63")
        buf.write("\7\2\2\3\63\3\3\2\2\2\64<\5\6\4\2\65<\5\b\5\2\66<\5\n")
        buf.write("\6\2\67<\5\f\7\28<\5\24\13\29<\5\16\b\2:<\5\22\n\2;\64")
        buf.write("\3\2\2\2;\65\3\2\2\2;\66\3\2\2\2;\67\3\2\2\2;8\3\2\2\2")
        buf.write(";9\3\2\2\2;:\3\2\2\2<\5\3\2\2\2=>\7\37\2\2>@\5$\23\2?")
        buf.write("A\5\34\17\2@?\3\2\2\2@A\3\2\2\2AE\3\2\2\2BD\13\2\2\2C")
        buf.write("B\3\2\2\2DG\3\2\2\2EF\3\2\2\2EC\3\2\2\2FH\3\2\2\2GE\3")
        buf.write("\2\2\2HJ\7 \2\2IK\5&\24\2JI\3\2\2\2JK\3\2\2\2K\7\3\2\2")
        buf.write("\2LM\7!\2\2MO\5$\23\2NP\5\34\17\2ON\3\2\2\2OP\3\2\2\2")
        buf.write("PT\3\2\2\2QS\13\2\2\2RQ\3\2\2\2SV\3\2\2\2TU\3\2\2\2TR")
        buf.write("\3\2\2\2UW\3\2\2\2VT\3\2\2\2WY\7\"\2\2XZ\5&\24\2YX\3\2")
        buf.write("\2\2YZ\3\2\2\2Z\t\3\2\2\2[]\7)\2\2\\^\5\"\22\2]\\\3\2")
        buf.write("\2\2]^\3\2\2\2^_\3\2\2\2_c\5$\23\2`b\13\2\2\2a`\3\2\2")
        buf.write("\2be\3\2\2\2cd\3\2\2\2ca\3\2\2\2df\3\2\2\2ec\3\2\2\2f")
        buf.write("h\7*\2\2gi\5&\24\2hg\3\2\2\2hi\3\2\2\2i\13\3\2\2\2jr\7")
        buf.write("/\2\2ks\5\24\13\2ln\13\2\2\2ml\3\2\2\2nq\3\2\2\2op\3\2")
        buf.write("\2\2om\3\2\2\2ps\3\2\2\2qo\3\2\2\2rk\3\2\2\2ro\3\2\2\2")
        buf.write("st\3\2\2\2tv\7\60\2\2uw\5&\24\2vu\3\2\2\2vw\3\2\2\2w\r")
        buf.write("\3\2\2\2xy\7%\2\2y}\5$\23\2z|\13\2\2\2{z\3\2\2\2|\177")
        buf.write("\3\2\2\2}~\3\2\2\2}{\3\2\2\2~\u0080\3\2\2\2\177}\3\2\2")
        buf.write("\2\u0080\u0082\7&\2\2\u0081\u0083\5&\24\2\u0082\u0081")
        buf.write("\3\2\2\2\u0082\u0083\3\2\2\2\u0083\17\3\2\2\2\u0084\u0086")
        buf.write("\7\3\2\2\u0085\u0084\3\2\2\2\u0085\u0086\3\2\2\2\u0086")
        buf.write("\u0087\3\2\2\2\u0087\u0089\7#\2\2\u0088\u008a\5\"\22\2")
        buf.write("\u0089\u0088\3\2\2\2\u0089\u008a\3\2\2\2\u008a\u008b\3")
        buf.write("\2\2\2\u008b\u008f\5$\23\2\u008c\u008e\13\2\2\2\u008d")
        buf.write("\u008c\3\2\2\2\u008e\u0091\3\2\2\2\u008f\u0090\3\2\2\2")
        buf.write("\u008f\u008d\3\2\2\2\u0090\u0092\3\2\2\2\u0091\u008f\3")
        buf.write("\2\2\2\u0092\u0094\7$\2\2\u0093\u0095\5&\24\2\u0094\u0093")
        buf.write("\3\2\2\2\u0094\u0095\3\2\2\2\u0095\21\3\2\2\2\u0096\u0097")
        buf.write("\7\'\2\2\u0097\u009b\5$\23\2\u0098\u009a\13\2\2\2\u0099")
        buf.write("\u0098\3\2\2\2\u009a\u009d\3\2\2\2\u009b\u009c\3\2\2\2")
        buf.write("\u009b\u0099\3\2\2\2\u009c\u009e\3\2\2\2\u009d\u009b\3")
        buf.write("\2\2\2\u009e\u00a0\7(\2\2\u009f\u00a1\5&\24\2\u00a0\u009f")
        buf.write("\3\2\2\2\u00a0\u00a1\3\2\2\2\u00a1\23\3\2\2\2\u00a2\u00a7")
        buf.write("\5\26\f\2\u00a3\u00a7\5\30\r\2\u00a4\u00a7\5\20\t\2\u00a5")
        buf.write("\u00a7\5\32\16\2\u00a6\u00a2\3\2\2\2\u00a6\u00a3\3\2\2")
        buf.write("\2\u00a6\u00a4\3\2\2\2\u00a6\u00a5\3\2\2\2\u00a7\25\3")
        buf.write("\2\2\2\u00a8\u00a9\7+\2\2\u00a9\u00ad\5$\23\2\u00aa\u00ac")
        buf.write("\13\2\2\2\u00ab\u00aa\3\2\2\2\u00ac\u00af\3\2\2\2\u00ad")
        buf.write("\u00ae\3\2\2\2\u00ad\u00ab\3\2\2\2\u00ae\u00b0\3\2\2\2")
        buf.write("\u00af\u00ad\3\2\2\2\u00b0\u00b2\7,\2\2\u00b1\u00b3\5")
        buf.write("&\24\2\u00b2\u00b1\3\2\2\2\u00b2\u00b3\3\2\2\2\u00b3\27")
        buf.write("\3\2\2\2\u00b4\u00b5\7-\2\2\u00b5\u00b6\5 \21\2\u00b6")
        buf.write("\u00b7\5$\23\2\u00b7\u00bb\7\23\2\2\u00b8\u00ba\13\2\2")
        buf.write("\2\u00b9\u00b8\3\2\2\2\u00ba\u00bd\3\2\2\2\u00bb\u00bc")
        buf.write("\3\2\2\2\u00bb\u00b9\3\2\2\2\u00bc\u00be\3\2\2\2\u00bd")
        buf.write("\u00bb\3\2\2\2\u00be\u00c0\7.\2\2\u00bf\u00c1\5&\24\2")
        buf.write("\u00c0\u00bf\3\2\2\2\u00c0\u00c1\3\2\2\2\u00c1\31\3\2")
        buf.write("\2\2\u00c2\u00c6\7\4\2\2\u00c3\u00c5\13\2\2\2\u00c4\u00c3")
        buf.write("\3\2\2\2\u00c5\u00c8\3\2\2\2\u00c6\u00c7\3\2\2\2\u00c6")
        buf.write("\u00c4\3\2\2\2\u00c7\u00c9\3\2\2\2\u00c8\u00c6\3\2\2\2")
        buf.write("\u00c9\u00ca\5$\23\2\u00ca\u00cb\7\27\2\2\u00cb\33\3\2")
        buf.write("\2\2\u00cc\u00d0\7\5\2\2\u00cd\u00cf\13\2\2\2\u00ce\u00cd")
        buf.write("\3\2\2\2\u00cf\u00d2\3\2\2\2\u00d0\u00d1\3\2\2\2\u00d0")
        buf.write("\u00ce\3\2\2\2\u00d1\u00d3\3\2\2\2\u00d2\u00d0\3\2\2\2")
        buf.write("\u00d3\u00d4\7\24\2\2\u00d4\35\3\2\2\2\u00d5\u00d9\7\23")
        buf.write("\2\2\u00d6\u00d8\13\2\2\2\u00d7\u00d6\3\2\2\2\u00d8\u00db")
        buf.write("\3\2\2\2\u00d9\u00da\3\2\2\2\u00d9\u00d7\3\2\2\2\u00da")
        buf.write("\u00dc\3\2\2\2\u00db\u00d9\3\2\2\2\u00dc\u00dd\7\24\2")
        buf.write("\2\u00dd\37\3\2\2\2\u00de\u00e6\7\6\2\2\u00df\u00e1\13")
        buf.write("\2\2\2\u00e0\u00df\3\2\2\2\u00e1\u00e4\3\2\2\2\u00e2\u00e3")
        buf.write("\3\2\2\2\u00e2\u00e0\3\2\2\2\u00e3\u00e6\3\2\2\2\u00e4")
        buf.write("\u00e2\3\2\2\2\u00e5\u00de\3\2\2\2\u00e5\u00e2\3\2\2\2")
        buf.write("\u00e6!\3\2\2\2\u00e7\u00e8\t\2\2\2\u00e8#\3\2\2\2\u00e9")
        buf.write("\u00ea\7;\2\2\u00ea%\3\2\2\2\u00eb\u00ec\7\30\2\2\u00ec")
        buf.write("\u00ed\5$\23\2\u00ed\'\3\2\2\2\u00ee\u00ef\7\t\2\2\u00ef")
        buf.write("\u00f1\7\34\2\2\u00f0\u00ee\3\2\2\2\u00f0\u00f1\3\2\2")
        buf.write("\2\u00f1\u00f8\3\2\2\2\u00f2\u00f3\7;\2\2\u00f3\u00f4")
        buf.write("\5*\26\2\u00f4\u00f5\7\34\2\2\u00f5\u00f7\3\2\2\2\u00f6")
        buf.write("\u00f2\3\2\2\2\u00f7\u00fa\3\2\2\2\u00f8\u00f6\3\2\2\2")
        buf.write("\u00f8\u00f9\3\2\2\2\u00f9\u00fb\3\2\2\2\u00fa\u00f8\3")
        buf.write("\2\2\2\u00fb\u00fc\5$\23\2\u00fc)\3\2\2\2\u00fd\u00fe")
        buf.write("\7\21\2\2\u00fe\u00ff\7;\2\2\u00ff\u0101\7\22\2\2\u0100")
        buf.write("\u00fd\3\2\2\2\u0101\u0104\3\2\2\2\u0102\u0100\3\2\2\2")
        buf.write("\u0102\u0103\3\2\2\2\u0103+\3\2\2\2\u0104\u0102\3\2\2")
        buf.write("\2%/;@EJOTY]chorv}\u0082\u0085\u0089\u008f\u0094\u009b")
        buf.write("\u00a0\u00a6\u00ad\u00b2\u00bb\u00c0\u00c6\u00d0\u00d9")
        buf.write("\u00e2\u00e5\u00f0\u00f8\u0102")
        return buf.getvalue()


class WorkspaceSymbolParser ( Parser ):

    grammarFileName = "WorkspaceSymbol.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'virtual'", "'typedef'", "'#('", "'void'", 
                     "'static'", "'automatic'", "'$root'", "<INVALID>", 
                     "<INVALID>", "' '", "'\t'", "<INVALID>", "<INVALID>", 
                     "<INVALID>", "'['", "']'", "'('", "')'", "'{'", "'}'", 
                     "';'", "':'", "','", "'='", "'?'", "'.'", "<INVALID>", 
                     "<INVALID>", "'module'", "'endmodule'", "'interface'", 
                     "'endinterface'", "'class'", "'endclass'", "'config'", 
                     "'endconfig'", "'primitive'", "'endprimitive'", "'program'", 
                     "'endprogram'", "'task'", "'endtask'", "'function'", 
                     "'endfunction'", "'package'", "'endpackage'" ]

    symbolicNames = [ "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "SINGLELINE_COMMENT", "MULTILINE_COMMENT", "SPACE", 
                      "TAB", "NEWLINE", "String", "COMPILER_DIRECTIVE", 
                      "OpenBracket", "CloseBracket", "OpenParen", "CloseParen", 
                      "OpenBrace", "CloseBrace", "SemiColon", "Colon", "Comma", 
                      "Assign", "QuestionMark", "Dot", "Apostrophe", "Operators", 
                      "Module", "Endmodule", "Interface", "Endinterface", 
                      "Class", "Endclass", "Config", "Endconfig", "Primitive", 
                      "Endprimitive", "Program", "Endprogram", "Task", "Endtask", 
                      "Function", "Endfunction", "Package", "Endpackage", 
                      "Number", "IntegralNumber", "RealNumber", "UnsignedNumber", 
                      "DecimalNumber", "BinaryNumber", "OctalNumber", "HexNumber", 
                      "UnbasedUnsizedLiteral", "Time", "Word" ]

    RULE_source = 0
    RULE_declaration = 1
    RULE_module_declaration = 2
    RULE_interface_declaration = 3
    RULE_program_declaration = 4
    RULE_package_declaration = 5
    RULE_config_declaration = 6
    RULE_class_declaration = 7
    RULE_udp_declaration = 8
    RULE_package_item = 9
    RULE_task_declaration = 10
    RULE_function_declaration = 11
    RULE_type_declaration = 12
    RULE_parameter_port_list = 13
    RULE_port_list = 14
    RULE_return_val = 15
    RULE_life_time = 16
    RULE_identifier = 17
    RULE_label = 18
    RULE_hierarchical_identifier = 19
    RULE_constant_bit_select = 20

    ruleNames =  [ "source", "declaration", "module_declaration", "interface_declaration", 
                   "program_declaration", "package_declaration", "config_declaration", 
                   "class_declaration", "udp_declaration", "package_item", 
                   "task_declaration", "function_declaration", "type_declaration", 
                   "parameter_port_list", "port_list", "return_val", "life_time", 
                   "identifier", "label", "hierarchical_identifier", "constant_bit_select" ]

    EOF = Token.EOF
    T__0=1
    T__1=2
    T__2=3
    T__3=4
    T__4=5
    T__5=6
    T__6=7
    SINGLELINE_COMMENT=8
    MULTILINE_COMMENT=9
    SPACE=10
    TAB=11
    NEWLINE=12
    String=13
    COMPILER_DIRECTIVE=14
    OpenBracket=15
    CloseBracket=16
    OpenParen=17
    CloseParen=18
    OpenBrace=19
    CloseBrace=20
    SemiColon=21
    Colon=22
    Comma=23
    Assign=24
    QuestionMark=25
    Dot=26
    Apostrophe=27
    Operators=28
    Module=29
    Endmodule=30
    Interface=31
    Endinterface=32
    Class=33
    Endclass=34
    Config=35
    Endconfig=36
    Primitive=37
    Endprimitive=38
    Program=39
    Endprogram=40
    Task=41
    Endtask=42
    Function=43
    Endfunction=44
    Package=45
    Endpackage=46
    Number=47
    IntegralNumber=48
    RealNumber=49
    UnsignedNumber=50
    DecimalNumber=51
    BinaryNumber=52
    OctalNumber=53
    HexNumber=54
    UnbasedUnsizedLiteral=55
    Time=56
    Word=57

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.8")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None




    class SourceContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def EOF(self):
            return self.getToken(WorkspaceSymbolParser.EOF, 0)

        def declaration(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(WorkspaceSymbolParser.DeclarationContext)
            else:
                return self.getTypedRuleContext(WorkspaceSymbolParser.DeclarationContext,i)


        def getRuleIndex(self):
            return WorkspaceSymbolParser.RULE_source

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterSource" ):
                listener.enterSource(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitSource" ):
                listener.exitSource(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitSource" ):
                return visitor.visitSource(self)
            else:
                return visitor.visitChildren(self)




    def source(self):

        localctx = WorkspaceSymbolParser.SourceContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_source)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 45
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << WorkspaceSymbolParser.T__0) | (1 << WorkspaceSymbolParser.T__1) | (1 << WorkspaceSymbolParser.Module) | (1 << WorkspaceSymbolParser.Interface) | (1 << WorkspaceSymbolParser.Class) | (1 << WorkspaceSymbolParser.Config) | (1 << WorkspaceSymbolParser.Primitive) | (1 << WorkspaceSymbolParser.Program) | (1 << WorkspaceSymbolParser.Task) | (1 << WorkspaceSymbolParser.Function) | (1 << WorkspaceSymbolParser.Package))) != 0):
                self.state = 42
                self.declaration()
                self.state = 47
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 48
            self.match(WorkspaceSymbolParser.EOF)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class DeclarationContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def module_declaration(self):
            return self.getTypedRuleContext(WorkspaceSymbolParser.Module_declarationContext,0)


        def interface_declaration(self):
            return self.getTypedRuleContext(WorkspaceSymbolParser.Interface_declarationContext,0)


        def program_declaration(self):
            return self.getTypedRuleContext(WorkspaceSymbolParser.Program_declarationContext,0)


        def package_declaration(self):
            return self.getTypedRuleContext(WorkspaceSymbolParser.Package_declarationContext,0)


        def package_item(self):
            return self.getTypedRuleContext(WorkspaceSymbolParser.Package_itemContext,0)


        def config_declaration(self):
            return self.getTypedRuleContext(WorkspaceSymbolParser.Config_declarationContext,0)


        def udp_declaration(self):
            return self.getTypedRuleContext(WorkspaceSymbolParser.Udp_declarationContext,0)


        def getRuleIndex(self):
            return WorkspaceSymbolParser.RULE_declaration

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterDeclaration" ):
                listener.enterDeclaration(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitDeclaration" ):
                listener.exitDeclaration(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitDeclaration" ):
                return visitor.visitDeclaration(self)
            else:
                return visitor.visitChildren(self)




    def declaration(self):

        localctx = WorkspaceSymbolParser.DeclarationContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_declaration)
        try:
            self.state = 57
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [WorkspaceSymbolParser.Module]:
                self.enterOuterAlt(localctx, 1)
                self.state = 50
                self.module_declaration()
                pass
            elif token in [WorkspaceSymbolParser.Interface]:
                self.enterOuterAlt(localctx, 2)
                self.state = 51
                self.interface_declaration()
                pass
            elif token in [WorkspaceSymbolParser.Program]:
                self.enterOuterAlt(localctx, 3)
                self.state = 52
                self.program_declaration()
                pass
            elif token in [WorkspaceSymbolParser.Package]:
                self.enterOuterAlt(localctx, 4)
                self.state = 53
                self.package_declaration()
                pass
            elif token in [WorkspaceSymbolParser.T__0, WorkspaceSymbolParser.T__1, WorkspaceSymbolParser.Class, WorkspaceSymbolParser.Task, WorkspaceSymbolParser.Function]:
                self.enterOuterAlt(localctx, 5)
                self.state = 54
                self.package_item()
                pass
            elif token in [WorkspaceSymbolParser.Config]:
                self.enterOuterAlt(localctx, 6)
                self.state = 55
                self.config_declaration()
                pass
            elif token in [WorkspaceSymbolParser.Primitive]:
                self.enterOuterAlt(localctx, 7)
                self.state = 56
                self.udp_declaration()
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Module_declarationContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def Module(self):
            return self.getToken(WorkspaceSymbolParser.Module, 0)

        def identifier(self):
            return self.getTypedRuleContext(WorkspaceSymbolParser.IdentifierContext,0)


        def Endmodule(self):
            return self.getToken(WorkspaceSymbolParser.Endmodule, 0)

        def parameter_port_list(self):
            return self.getTypedRuleContext(WorkspaceSymbolParser.Parameter_port_listContext,0)


        def label(self):
            return self.getTypedRuleContext(WorkspaceSymbolParser.LabelContext,0)


        def getRuleIndex(self):
            return WorkspaceSymbolParser.RULE_module_declaration

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterModule_declaration" ):
                listener.enterModule_declaration(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitModule_declaration" ):
                listener.exitModule_declaration(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitModule_declaration" ):
                return visitor.visitModule_declaration(self)
            else:
                return visitor.visitChildren(self)




    def module_declaration(self):

        localctx = WorkspaceSymbolParser.Module_declarationContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_module_declaration)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 59
            self.match(WorkspaceSymbolParser.Module)
            self.state = 60
            self.identifier()
            self.state = 62
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,2,self._ctx)
            if la_ == 1:
                self.state = 61
                self.parameter_port_list()


            self.state = 67
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,3,self._ctx)
            while _alt!=1 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1+1:
                    self.state = 64
                    self.matchWildcard() 
                self.state = 69
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,3,self._ctx)

            self.state = 70
            self.match(WorkspaceSymbolParser.Endmodule)
            self.state = 72
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==WorkspaceSymbolParser.Colon:
                self.state = 71
                self.label()


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Interface_declarationContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def Interface(self):
            return self.getToken(WorkspaceSymbolParser.Interface, 0)

        def identifier(self):
            return self.getTypedRuleContext(WorkspaceSymbolParser.IdentifierContext,0)


        def Endinterface(self):
            return self.getToken(WorkspaceSymbolParser.Endinterface, 0)

        def parameter_port_list(self):
            return self.getTypedRuleContext(WorkspaceSymbolParser.Parameter_port_listContext,0)


        def label(self):
            return self.getTypedRuleContext(WorkspaceSymbolParser.LabelContext,0)


        def getRuleIndex(self):
            return WorkspaceSymbolParser.RULE_interface_declaration

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterInterface_declaration" ):
                listener.enterInterface_declaration(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitInterface_declaration" ):
                listener.exitInterface_declaration(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitInterface_declaration" ):
                return visitor.visitInterface_declaration(self)
            else:
                return visitor.visitChildren(self)




    def interface_declaration(self):

        localctx = WorkspaceSymbolParser.Interface_declarationContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_interface_declaration)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 74
            self.match(WorkspaceSymbolParser.Interface)
            self.state = 75
            self.identifier()
            self.state = 77
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,5,self._ctx)
            if la_ == 1:
                self.state = 76
                self.parameter_port_list()


            self.state = 82
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,6,self._ctx)
            while _alt!=1 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1+1:
                    self.state = 79
                    self.matchWildcard() 
                self.state = 84
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,6,self._ctx)

            self.state = 85
            self.match(WorkspaceSymbolParser.Endinterface)
            self.state = 87
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==WorkspaceSymbolParser.Colon:
                self.state = 86
                self.label()


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Program_declarationContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def Program(self):
            return self.getToken(WorkspaceSymbolParser.Program, 0)

        def identifier(self):
            return self.getTypedRuleContext(WorkspaceSymbolParser.IdentifierContext,0)


        def Endprogram(self):
            return self.getToken(WorkspaceSymbolParser.Endprogram, 0)

        def life_time(self):
            return self.getTypedRuleContext(WorkspaceSymbolParser.Life_timeContext,0)


        def label(self):
            return self.getTypedRuleContext(WorkspaceSymbolParser.LabelContext,0)


        def getRuleIndex(self):
            return WorkspaceSymbolParser.RULE_program_declaration

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterProgram_declaration" ):
                listener.enterProgram_declaration(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitProgram_declaration" ):
                listener.exitProgram_declaration(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitProgram_declaration" ):
                return visitor.visitProgram_declaration(self)
            else:
                return visitor.visitChildren(self)




    def program_declaration(self):

        localctx = WorkspaceSymbolParser.Program_declarationContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_program_declaration)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 89
            self.match(WorkspaceSymbolParser.Program)
            self.state = 91
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==WorkspaceSymbolParser.T__4 or _la==WorkspaceSymbolParser.T__5:
                self.state = 90
                self.life_time()


            self.state = 93
            self.identifier()
            self.state = 97
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,9,self._ctx)
            while _alt!=1 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1+1:
                    self.state = 94
                    self.matchWildcard() 
                self.state = 99
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,9,self._ctx)

            self.state = 100
            self.match(WorkspaceSymbolParser.Endprogram)
            self.state = 102
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==WorkspaceSymbolParser.Colon:
                self.state = 101
                self.label()


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Package_declarationContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def Package(self):
            return self.getToken(WorkspaceSymbolParser.Package, 0)

        def Endpackage(self):
            return self.getToken(WorkspaceSymbolParser.Endpackage, 0)

        def package_item(self):
            return self.getTypedRuleContext(WorkspaceSymbolParser.Package_itemContext,0)


        def label(self):
            return self.getTypedRuleContext(WorkspaceSymbolParser.LabelContext,0)


        def getRuleIndex(self):
            return WorkspaceSymbolParser.RULE_package_declaration

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterPackage_declaration" ):
                listener.enterPackage_declaration(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitPackage_declaration" ):
                listener.exitPackage_declaration(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitPackage_declaration" ):
                return visitor.visitPackage_declaration(self)
            else:
                return visitor.visitChildren(self)




    def package_declaration(self):

        localctx = WorkspaceSymbolParser.Package_declarationContext(self, self._ctx, self.state)
        self.enterRule(localctx, 10, self.RULE_package_declaration)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 104
            self.match(WorkspaceSymbolParser.Package)
            self.state = 112
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,12,self._ctx)
            if la_ == 1:
                self.state = 105
                self.package_item()
                pass

            elif la_ == 2:
                self.state = 109
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,11,self._ctx)
                while _alt!=1 and _alt!=ATN.INVALID_ALT_NUMBER:
                    if _alt==1+1:
                        self.state = 106
                        self.matchWildcard() 
                    self.state = 111
                    self._errHandler.sync(self)
                    _alt = self._interp.adaptivePredict(self._input,11,self._ctx)

                pass


            self.state = 114
            self.match(WorkspaceSymbolParser.Endpackage)
            self.state = 116
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==WorkspaceSymbolParser.Colon:
                self.state = 115
                self.label()


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Config_declarationContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def Config(self):
            return self.getToken(WorkspaceSymbolParser.Config, 0)

        def identifier(self):
            return self.getTypedRuleContext(WorkspaceSymbolParser.IdentifierContext,0)


        def Endconfig(self):
            return self.getToken(WorkspaceSymbolParser.Endconfig, 0)

        def label(self):
            return self.getTypedRuleContext(WorkspaceSymbolParser.LabelContext,0)


        def getRuleIndex(self):
            return WorkspaceSymbolParser.RULE_config_declaration

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterConfig_declaration" ):
                listener.enterConfig_declaration(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitConfig_declaration" ):
                listener.exitConfig_declaration(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitConfig_declaration" ):
                return visitor.visitConfig_declaration(self)
            else:
                return visitor.visitChildren(self)




    def config_declaration(self):

        localctx = WorkspaceSymbolParser.Config_declarationContext(self, self._ctx, self.state)
        self.enterRule(localctx, 12, self.RULE_config_declaration)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 118
            self.match(WorkspaceSymbolParser.Config)
            self.state = 119
            self.identifier()
            self.state = 123
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,14,self._ctx)
            while _alt!=1 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1+1:
                    self.state = 120
                    self.matchWildcard() 
                self.state = 125
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,14,self._ctx)

            self.state = 126
            self.match(WorkspaceSymbolParser.Endconfig)
            self.state = 128
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==WorkspaceSymbolParser.Colon:
                self.state = 127
                self.label()


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Class_declarationContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def Class(self):
            return self.getToken(WorkspaceSymbolParser.Class, 0)

        def identifier(self):
            return self.getTypedRuleContext(WorkspaceSymbolParser.IdentifierContext,0)


        def Endclass(self):
            return self.getToken(WorkspaceSymbolParser.Endclass, 0)

        def life_time(self):
            return self.getTypedRuleContext(WorkspaceSymbolParser.Life_timeContext,0)


        def label(self):
            return self.getTypedRuleContext(WorkspaceSymbolParser.LabelContext,0)


        def getRuleIndex(self):
            return WorkspaceSymbolParser.RULE_class_declaration

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterClass_declaration" ):
                listener.enterClass_declaration(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitClass_declaration" ):
                listener.exitClass_declaration(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitClass_declaration" ):
                return visitor.visitClass_declaration(self)
            else:
                return visitor.visitChildren(self)




    def class_declaration(self):

        localctx = WorkspaceSymbolParser.Class_declarationContext(self, self._ctx, self.state)
        self.enterRule(localctx, 14, self.RULE_class_declaration)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 131
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==WorkspaceSymbolParser.T__0:
                self.state = 130
                self.match(WorkspaceSymbolParser.T__0)


            self.state = 133
            self.match(WorkspaceSymbolParser.Class)
            self.state = 135
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==WorkspaceSymbolParser.T__4 or _la==WorkspaceSymbolParser.T__5:
                self.state = 134
                self.life_time()


            self.state = 137
            self.identifier()
            self.state = 141
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,18,self._ctx)
            while _alt!=1 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1+1:
                    self.state = 138
                    self.matchWildcard() 
                self.state = 143
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,18,self._ctx)

            self.state = 144
            self.match(WorkspaceSymbolParser.Endclass)
            self.state = 146
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==WorkspaceSymbolParser.Colon:
                self.state = 145
                self.label()


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Udp_declarationContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def Primitive(self):
            return self.getToken(WorkspaceSymbolParser.Primitive, 0)

        def identifier(self):
            return self.getTypedRuleContext(WorkspaceSymbolParser.IdentifierContext,0)


        def Endprimitive(self):
            return self.getToken(WorkspaceSymbolParser.Endprimitive, 0)

        def label(self):
            return self.getTypedRuleContext(WorkspaceSymbolParser.LabelContext,0)


        def getRuleIndex(self):
            return WorkspaceSymbolParser.RULE_udp_declaration

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterUdp_declaration" ):
                listener.enterUdp_declaration(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitUdp_declaration" ):
                listener.exitUdp_declaration(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitUdp_declaration" ):
                return visitor.visitUdp_declaration(self)
            else:
                return visitor.visitChildren(self)




    def udp_declaration(self):

        localctx = WorkspaceSymbolParser.Udp_declarationContext(self, self._ctx, self.state)
        self.enterRule(localctx, 16, self.RULE_udp_declaration)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 148
            self.match(WorkspaceSymbolParser.Primitive)
            self.state = 149
            self.identifier()
            self.state = 153
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,20,self._ctx)
            while _alt!=1 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1+1:
                    self.state = 150
                    self.matchWildcard() 
                self.state = 155
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,20,self._ctx)

            self.state = 156
            self.match(WorkspaceSymbolParser.Endprimitive)
            self.state = 158
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==WorkspaceSymbolParser.Colon:
                self.state = 157
                self.label()


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Package_itemContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def task_declaration(self):
            return self.getTypedRuleContext(WorkspaceSymbolParser.Task_declarationContext,0)


        def function_declaration(self):
            return self.getTypedRuleContext(WorkspaceSymbolParser.Function_declarationContext,0)


        def class_declaration(self):
            return self.getTypedRuleContext(WorkspaceSymbolParser.Class_declarationContext,0)


        def type_declaration(self):
            return self.getTypedRuleContext(WorkspaceSymbolParser.Type_declarationContext,0)


        def getRuleIndex(self):
            return WorkspaceSymbolParser.RULE_package_item

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterPackage_item" ):
                listener.enterPackage_item(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitPackage_item" ):
                listener.exitPackage_item(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitPackage_item" ):
                return visitor.visitPackage_item(self)
            else:
                return visitor.visitChildren(self)




    def package_item(self):

        localctx = WorkspaceSymbolParser.Package_itemContext(self, self._ctx, self.state)
        self.enterRule(localctx, 18, self.RULE_package_item)
        try:
            self.state = 164
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [WorkspaceSymbolParser.Task]:
                self.enterOuterAlt(localctx, 1)
                self.state = 160
                self.task_declaration()
                pass
            elif token in [WorkspaceSymbolParser.Function]:
                self.enterOuterAlt(localctx, 2)
                self.state = 161
                self.function_declaration()
                pass
            elif token in [WorkspaceSymbolParser.T__0, WorkspaceSymbolParser.Class]:
                self.enterOuterAlt(localctx, 3)
                self.state = 162
                self.class_declaration()
                pass
            elif token in [WorkspaceSymbolParser.T__1]:
                self.enterOuterAlt(localctx, 4)
                self.state = 163
                self.type_declaration()
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Task_declarationContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def Task(self):
            return self.getToken(WorkspaceSymbolParser.Task, 0)

        def identifier(self):
            return self.getTypedRuleContext(WorkspaceSymbolParser.IdentifierContext,0)


        def Endtask(self):
            return self.getToken(WorkspaceSymbolParser.Endtask, 0)

        def label(self):
            return self.getTypedRuleContext(WorkspaceSymbolParser.LabelContext,0)


        def getRuleIndex(self):
            return WorkspaceSymbolParser.RULE_task_declaration

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterTask_declaration" ):
                listener.enterTask_declaration(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitTask_declaration" ):
                listener.exitTask_declaration(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitTask_declaration" ):
                return visitor.visitTask_declaration(self)
            else:
                return visitor.visitChildren(self)




    def task_declaration(self):

        localctx = WorkspaceSymbolParser.Task_declarationContext(self, self._ctx, self.state)
        self.enterRule(localctx, 20, self.RULE_task_declaration)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 166
            self.match(WorkspaceSymbolParser.Task)
            self.state = 167
            self.identifier()
            self.state = 171
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,23,self._ctx)
            while _alt!=1 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1+1:
                    self.state = 168
                    self.matchWildcard() 
                self.state = 173
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,23,self._ctx)

            self.state = 174
            self.match(WorkspaceSymbolParser.Endtask)
            self.state = 176
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==WorkspaceSymbolParser.Colon:
                self.state = 175
                self.label()


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Function_declarationContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def Function(self):
            return self.getToken(WorkspaceSymbolParser.Function, 0)

        def return_val(self):
            return self.getTypedRuleContext(WorkspaceSymbolParser.Return_valContext,0)


        def identifier(self):
            return self.getTypedRuleContext(WorkspaceSymbolParser.IdentifierContext,0)


        def OpenParen(self):
            return self.getToken(WorkspaceSymbolParser.OpenParen, 0)

        def Endfunction(self):
            return self.getToken(WorkspaceSymbolParser.Endfunction, 0)

        def label(self):
            return self.getTypedRuleContext(WorkspaceSymbolParser.LabelContext,0)


        def getRuleIndex(self):
            return WorkspaceSymbolParser.RULE_function_declaration

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterFunction_declaration" ):
                listener.enterFunction_declaration(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitFunction_declaration" ):
                listener.exitFunction_declaration(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFunction_declaration" ):
                return visitor.visitFunction_declaration(self)
            else:
                return visitor.visitChildren(self)




    def function_declaration(self):

        localctx = WorkspaceSymbolParser.Function_declarationContext(self, self._ctx, self.state)
        self.enterRule(localctx, 22, self.RULE_function_declaration)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 178
            self.match(WorkspaceSymbolParser.Function)
            self.state = 179
            self.return_val()
            self.state = 180
            self.identifier()
            self.state = 181
            self.match(WorkspaceSymbolParser.OpenParen)
            self.state = 185
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,25,self._ctx)
            while _alt!=1 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1+1:
                    self.state = 182
                    self.matchWildcard() 
                self.state = 187
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,25,self._ctx)

            self.state = 188
            self.match(WorkspaceSymbolParser.Endfunction)
            self.state = 190
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==WorkspaceSymbolParser.Colon:
                self.state = 189
                self.label()


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Type_declarationContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def identifier(self):
            return self.getTypedRuleContext(WorkspaceSymbolParser.IdentifierContext,0)


        def SemiColon(self):
            return self.getToken(WorkspaceSymbolParser.SemiColon, 0)

        def getRuleIndex(self):
            return WorkspaceSymbolParser.RULE_type_declaration

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterType_declaration" ):
                listener.enterType_declaration(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitType_declaration" ):
                listener.exitType_declaration(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitType_declaration" ):
                return visitor.visitType_declaration(self)
            else:
                return visitor.visitChildren(self)




    def type_declaration(self):

        localctx = WorkspaceSymbolParser.Type_declarationContext(self, self._ctx, self.state)
        self.enterRule(localctx, 24, self.RULE_type_declaration)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 192
            self.match(WorkspaceSymbolParser.T__1)
            self.state = 196
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,27,self._ctx)
            while _alt!=1 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1+1:
                    self.state = 193
                    self.matchWildcard() 
                self.state = 198
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,27,self._ctx)

            self.state = 199
            self.identifier()
            self.state = 200
            self.match(WorkspaceSymbolParser.SemiColon)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Parameter_port_listContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def CloseParen(self):
            return self.getToken(WorkspaceSymbolParser.CloseParen, 0)

        def getRuleIndex(self):
            return WorkspaceSymbolParser.RULE_parameter_port_list

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterParameter_port_list" ):
                listener.enterParameter_port_list(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitParameter_port_list" ):
                listener.exitParameter_port_list(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitParameter_port_list" ):
                return visitor.visitParameter_port_list(self)
            else:
                return visitor.visitChildren(self)




    def parameter_port_list(self):

        localctx = WorkspaceSymbolParser.Parameter_port_listContext(self, self._ctx, self.state)
        self.enterRule(localctx, 26, self.RULE_parameter_port_list)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 202
            self.match(WorkspaceSymbolParser.T__2)
            self.state = 206
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,28,self._ctx)
            while _alt!=1 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1+1:
                    self.state = 203
                    self.matchWildcard() 
                self.state = 208
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,28,self._ctx)

            self.state = 209
            self.match(WorkspaceSymbolParser.CloseParen)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Port_listContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def OpenParen(self):
            return self.getToken(WorkspaceSymbolParser.OpenParen, 0)

        def CloseParen(self):
            return self.getToken(WorkspaceSymbolParser.CloseParen, 0)

        def getRuleIndex(self):
            return WorkspaceSymbolParser.RULE_port_list

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterPort_list" ):
                listener.enterPort_list(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitPort_list" ):
                listener.exitPort_list(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitPort_list" ):
                return visitor.visitPort_list(self)
            else:
                return visitor.visitChildren(self)




    def port_list(self):

        localctx = WorkspaceSymbolParser.Port_listContext(self, self._ctx, self.state)
        self.enterRule(localctx, 28, self.RULE_port_list)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 211
            self.match(WorkspaceSymbolParser.OpenParen)
            self.state = 215
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,29,self._ctx)
            while _alt!=1 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1+1:
                    self.state = 212
                    self.matchWildcard() 
                self.state = 217
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,29,self._ctx)

            self.state = 218
            self.match(WorkspaceSymbolParser.CloseParen)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Return_valContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return WorkspaceSymbolParser.RULE_return_val

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterReturn_val" ):
                listener.enterReturn_val(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitReturn_val" ):
                listener.exitReturn_val(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitReturn_val" ):
                return visitor.visitReturn_val(self)
            else:
                return visitor.visitChildren(self)




    def return_val(self):

        localctx = WorkspaceSymbolParser.Return_valContext(self, self._ctx, self.state)
        self.enterRule(localctx, 30, self.RULE_return_val)
        try:
            self.state = 227
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,31,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 220
                self.match(WorkspaceSymbolParser.T__3)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 224
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,30,self._ctx)
                while _alt!=1 and _alt!=ATN.INVALID_ALT_NUMBER:
                    if _alt==1+1:
                        self.state = 221
                        self.matchWildcard() 
                    self.state = 226
                    self._errHandler.sync(self)
                    _alt = self._interp.adaptivePredict(self._input,30,self._ctx)

                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Life_timeContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return WorkspaceSymbolParser.RULE_life_time

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterLife_time" ):
                listener.enterLife_time(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitLife_time" ):
                listener.exitLife_time(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitLife_time" ):
                return visitor.visitLife_time(self)
            else:
                return visitor.visitChildren(self)




    def life_time(self):

        localctx = WorkspaceSymbolParser.Life_timeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 32, self.RULE_life_time)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 229
            _la = self._input.LA(1)
            if not(_la==WorkspaceSymbolParser.T__4 or _la==WorkspaceSymbolParser.T__5):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class IdentifierContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def Word(self):
            return self.getToken(WorkspaceSymbolParser.Word, 0)

        def getRuleIndex(self):
            return WorkspaceSymbolParser.RULE_identifier

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterIdentifier" ):
                listener.enterIdentifier(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitIdentifier" ):
                listener.exitIdentifier(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitIdentifier" ):
                return visitor.visitIdentifier(self)
            else:
                return visitor.visitChildren(self)




    def identifier(self):

        localctx = WorkspaceSymbolParser.IdentifierContext(self, self._ctx, self.state)
        self.enterRule(localctx, 34, self.RULE_identifier)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 231
            self.match(WorkspaceSymbolParser.Word)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class LabelContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def Colon(self):
            return self.getToken(WorkspaceSymbolParser.Colon, 0)

        def identifier(self):
            return self.getTypedRuleContext(WorkspaceSymbolParser.IdentifierContext,0)


        def getRuleIndex(self):
            return WorkspaceSymbolParser.RULE_label

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterLabel" ):
                listener.enterLabel(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitLabel" ):
                listener.exitLabel(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitLabel" ):
                return visitor.visitLabel(self)
            else:
                return visitor.visitChildren(self)




    def label(self):

        localctx = WorkspaceSymbolParser.LabelContext(self, self._ctx, self.state)
        self.enterRule(localctx, 36, self.RULE_label)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 233
            self.match(WorkspaceSymbolParser.Colon)
            self.state = 234
            self.identifier()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Hierarchical_identifierContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def identifier(self):
            return self.getTypedRuleContext(WorkspaceSymbolParser.IdentifierContext,0)


        def Dot(self, i:int=None):
            if i is None:
                return self.getTokens(WorkspaceSymbolParser.Dot)
            else:
                return self.getToken(WorkspaceSymbolParser.Dot, i)

        def Word(self, i:int=None):
            if i is None:
                return self.getTokens(WorkspaceSymbolParser.Word)
            else:
                return self.getToken(WorkspaceSymbolParser.Word, i)

        def constant_bit_select(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(WorkspaceSymbolParser.Constant_bit_selectContext)
            else:
                return self.getTypedRuleContext(WorkspaceSymbolParser.Constant_bit_selectContext,i)


        def getRuleIndex(self):
            return WorkspaceSymbolParser.RULE_hierarchical_identifier

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterHierarchical_identifier" ):
                listener.enterHierarchical_identifier(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitHierarchical_identifier" ):
                listener.exitHierarchical_identifier(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitHierarchical_identifier" ):
                return visitor.visitHierarchical_identifier(self)
            else:
                return visitor.visitChildren(self)




    def hierarchical_identifier(self):

        localctx = WorkspaceSymbolParser.Hierarchical_identifierContext(self, self._ctx, self.state)
        self.enterRule(localctx, 38, self.RULE_hierarchical_identifier)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 238
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==WorkspaceSymbolParser.T__6:
                self.state = 236
                self.match(WorkspaceSymbolParser.T__6)
                self.state = 237
                self.match(WorkspaceSymbolParser.Dot)


            self.state = 246
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,33,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    self.state = 240
                    self.match(WorkspaceSymbolParser.Word)
                    self.state = 241
                    self.constant_bit_select()
                    self.state = 242
                    self.match(WorkspaceSymbolParser.Dot) 
                self.state = 248
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,33,self._ctx)

            self.state = 249
            self.identifier()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Constant_bit_selectContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def OpenBracket(self, i:int=None):
            if i is None:
                return self.getTokens(WorkspaceSymbolParser.OpenBracket)
            else:
                return self.getToken(WorkspaceSymbolParser.OpenBracket, i)

        def Word(self, i:int=None):
            if i is None:
                return self.getTokens(WorkspaceSymbolParser.Word)
            else:
                return self.getToken(WorkspaceSymbolParser.Word, i)

        def CloseBracket(self, i:int=None):
            if i is None:
                return self.getTokens(WorkspaceSymbolParser.CloseBracket)
            else:
                return self.getToken(WorkspaceSymbolParser.CloseBracket, i)

        def getRuleIndex(self):
            return WorkspaceSymbolParser.RULE_constant_bit_select

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterConstant_bit_select" ):
                listener.enterConstant_bit_select(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitConstant_bit_select" ):
                listener.exitConstant_bit_select(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitConstant_bit_select" ):
                return visitor.visitConstant_bit_select(self)
            else:
                return visitor.visitChildren(self)




    def constant_bit_select(self):

        localctx = WorkspaceSymbolParser.Constant_bit_selectContext(self, self._ctx, self.state)
        self.enterRule(localctx, 40, self.RULE_constant_bit_select)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 256
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==WorkspaceSymbolParser.OpenBracket:
                self.state = 251
                self.match(WorkspaceSymbolParser.OpenBracket)
                self.state = 252
                self.match(WorkspaceSymbolParser.Word)
                self.state = 253
                self.match(WorkspaceSymbolParser.CloseBracket)
                self.state = 258
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx





